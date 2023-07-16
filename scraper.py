from datetime import datetime
from pprint import pprint
from os import getenv
import requests, traceback

# an attempt at an api scraper to grab my matches from ancestry DNA

# need to copy all the cookies to this env var.
COOKIES = getenv('MY_COOKIES')
MY_UUID = getenv('REFERENCE_USER_UUID')

if not COOKIES or not MY_UUID:
    raise Exception("please set the environmental variables in env.sh")

def get_page(page_index):
    # ancestry paging is weird:
    other_url = ''
    if page_index > 0:
        other_url = 'bookmarkdata={%22moreMatchesAvailable%22:true,%22lastMatchesServicePageIdx%22:' + str(page_index) + '}'
    page = 1 + page_index * 4

    unix_time = int(datetime.now().timestamp())
    url = f'https://www.ancestry.com/discoveryui-matchesservice/api/samples/{MY_UUID}/matches/list?page={page}&sortby=RELATIONSHIP&_t={unix_time}&{other_url}'

    # debug information for the url:
    # print(url)

    headers = {
        'cookie': COOKIES,
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
    }
    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        raise Exception(f"Failed to get a 200 response\n: {response}")
    return response.json()


if __name__ == '__main__':
    results = {}
    page_index = 0
    all_matches = []
    try:
        # CSV header
        print("match index, shared centimorgans, display name, user uuid, ")
        while True:
            page_json = get_page(page_index)
            page_index += 1

            # failure criteria, json response either doesn't have a matchGroup, or its empty:
            if not (page_json.get('matchGroups', False) and len(page_json['matchGroups']) > 0):
                break
            # append a match:
            for match_group in page_json['matchGroups']:
                for match_user in match_group['matches']:

                    # display the raw data
                    # print(match_user)

                    all_matches.append(match_user)
                    print(f'{len(all_matches)}, {match_user["relationship"]["sharedCentimorgans"]},{match_user["publicDisplayName"]},{match_user["testGuid"]}')

                # below a minimum relationship rate, you dont care about the results anymore:
                if match_user["relationship"]["sharedCentimorgans"] < 25:
                    exit(0)

        # pprint(all_matches)
    except Exception:
        traceback.print_exc()


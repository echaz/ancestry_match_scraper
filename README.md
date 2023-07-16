# Ancestry Match Scraper

Copy your ancestry matches in a CSV format

## Installation

1. Clone the repository.
2. Install python 3, if it isn't already installed
3. the following instructions presume you have access to a linux terminal
4. python3 -m ensurepip --upgrade
5. cd ${CLONED_DIRECTORY}
6. pip3 install -r ./requirements.txt
7. configure the file env.sh
    - go to my matches url -> all matches
    - copy the UUID in the url, save it off in env.sh
        - "REFERENCE_USER_UUID={uuid value copied}"
    - open developer tools
    - refresh page
    - in the network pane search for 'list?':
        - there will be one result. right click it
        - copy -> copy as cURL
        - open a text editor
        - paste
        - find the cookie header
        - copy the cookie header value: it will look like "-H 'cookie: <this is the thing to capture>'
            - save it off in env.sh (this will be a large value)
                - "MY_COOKIES={cookie value}"

## Usage

1. source ./env.sh
7. python3 ./scraper.py
8. results will go to stdout, and can be redirected to a file

## License

This project is licensed under the [MIT License](LICENSE).
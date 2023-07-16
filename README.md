# Ancestry Match Scraper

Copy your ancestry matches in a CSV format

## Installation

1. Clone the repository.
2. Install docker.



## Usage

1. go to ancestry my dna page on chrome
    - configure the file env.sh
        - go to my matches url -> all matches
        - copy the UUID in the url, save it off in env.sh
            - "REFERENCE_USER_UUID=<uuid value copied>"
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
                    - "MY_COOKIES=<cookie value>"
2. from a terminal, type "docker compose up" 
    - this kind of presumes a linux-like environment
3. results will display to stdout, and can be copied or redirected to a file

## Usage without docker
 1.  install python (I'm using 3.8, but you shouldn't be limited to it)
 2. install pip
 3. cd ${CLONED_DIRECTORY}
 4. pip3 install -r ./requirements.txt
 5. export REFERENCE_USER_UUID='<UUID from docker instructions>'
 6. export MY_COOKIES='<cookies from docker instructions>'
 7. python3 ./scraper.py
 8. results will go to stdout, and can be redirected to a file

## License

This project is licensed under the [MIT License](LICENSE).
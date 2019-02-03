# Jelly Notes on UnalloSlackBot
- Pulled in latest upstream code overwriting local changes to README.md in root
- 8ball.py 
    - Trigger: Any message containing "!ball"
    - Response: ill listen for any message containing "!ball", and respond with a random 8ball response
- about.py
    - Trigger: Any message ending in "!about"
    - Response: About, mission statment and brief message about the space
- address.py 
    - Trigger: Any message ending in "!address"
    - Response: address
- donate.py
    - Trigger: Any message endning in "!donate"
    - Response: Message containing paypall address and link to UAS Contribute web page
- help.py
    - Trigger: Any message containing "!help"
    - Response: A static message of menu options we want to present to users
- info.py
    - Trigger: Any message ending in "!info"
    - Response: Space status (open/closed) and link to The Wall
- phone.py
    - Trigger: Any message ending in "!phone"
    - Response: Space phone number
- quote.py
    - Trigger: Any message ending in "!quote"
    - Response: Random quote
- status.py
    - Trigger: Any message ending in "!status"
    - Resonse: Pull status txt from UAS website, past text in chat
- upload.py 
    - Trigger: 
    - Response: 
- wall.py
    - Trigger: Any message ending in "!wall"
    - Response: Post link to wall image URL appending with random string. This ensures Slack clients load preview of image as the URL is now "unique"


### Modifying help menu
- When modifying help, you must modify help menu list in two places:
    - ./slackbot_settings.py which is in the root of this git repository
    - ./slackbot/plugins/help.py

- Note: ./slackbot_settings.py is the GENERIC error message for all unknown commands per the README.md file in the root directory


# Notes on Docker
- To build this in docker run:
```
$ sudo docker build . -t unallobot
```

- To run in docker after building do:
```sh
$ sudo docker run -d --restart unless-stopped -e SLACKBOT_API_TOKEN=MY_SECRET_TOKEN unallobot
```



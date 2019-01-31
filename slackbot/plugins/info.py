#coding: UTF-8
from slackbot.bot import listen_to
from slackbot.bot import respond_to
import urllib3
import re
# thank you https://stackoverflow.com/questions/2257441/random-string-generation-with-upper-case-letters-and-digits-in-python
import random
import string

WEBURL = 'https://www.unallocatedspace.org/status'
HTTPS = urllib3.PoolManager()
ANSWER = HTTPS.request('GET', WEBURL)
STATUS = ANSWER.data.decode("utf-8") 

WALL = "https://www.unallocatedspace.org/thewall/thewall.jpg?" + ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))

@respond_to('!info$', re.IGNORECASE)
def status_reply(message):
    message.reply(STATUS + '\n' + WALL)

@listen_to('!info$', re.IGNORECASE)
def status(message):
    message.send(STATUS + '\n' + WALL)

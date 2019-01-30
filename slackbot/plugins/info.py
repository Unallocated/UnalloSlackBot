#coding: UTF-8
from slackbot.bot import listen_to
from slackbot.bot import respond_to
import urllib3
import re
# thank you https://stackoverflow.com/questions/2257441/random-string-generation-with-upper-case-letters-and-digits-in-python
import random
import string

url = 'https://www.unallocatedspace.org/status'
http = urllib3.PoolManager()

WALL = "https://www.unallocatedspace.org/thewall/thewall.jpg?" + ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))

r = http.request('GET', url)


@respond_to('!info$', re.IGNORECASE)
def status_reply(message):
    message.reply(r.data + b'\n' + WALL)

@listen_to('!info$', re.IGNORECASE)
def status(message):
    message.send(r.data + b'\n' + WALL)

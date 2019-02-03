#coding: UTF-8
# thank you https://stackoverflow.com/questions/2257441/random-string-generation-with-upper-case-letters-and-digits-in-python
import re
import random
import string
from slackbot.bot import respond_to
from slackbot.bot import listen_to

WALL = "https://www.unallocatedspace.org/thewall/thewall.jpg?" + ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))

@respond_to('!wall$', re.IGNORECASE)
def hello_reply(message):
    message.reply(WALL)

@listen_to('!wall$', re.IGNORECASE)
def hello_send(message):
    message.send(WALL)



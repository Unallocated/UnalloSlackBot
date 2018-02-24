#coding: UTF-8
import re
from slackbot.bot import respond_to
from slackbot.bot import listen_to

@respond_to('!rollcall', re.IGNORECASE)
def rollcall(message):
    pass
    #message.reply('hello sender!')

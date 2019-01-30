#coding: UTF-8
import re
from slackbot.bot import respond_to
from slackbot.bot import listen_to

@respond_to('!help$', re.IGNORECASE)
def hello_reply(message):

@listen_to('!help$', re.IGNORECASE)
def hello_send(message):
    


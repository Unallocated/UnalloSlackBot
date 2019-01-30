#coding: UTF-8
import re
from slackbot.bot import respond_to
from slackbot.bot import listen_to


ADDRESS = "512 Shaw Court #105, Severn MD, 21144"


@respond_to('!address$', re.IGNORECASE)
def hello_reply(message):
    message.reply(ADDRESS)


@listen_to('!address$', re.IGNORECASE)
def hello_send(message):
    message.send(ADDRESS)



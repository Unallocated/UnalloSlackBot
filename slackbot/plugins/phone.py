#coding: UTF-8
import re
from slackbot.bot import respond_to
from slackbot.bot import listen_to


PHONE = "(410) 921-9410"


@respond_to('phone$', re.IGNORECASE)
def hello_reply(message):
    message.reply(PHONE)


@listen_to('phone$', re.IGNORECASE)
def hello_send(message):
    message.send(PHONE)



#coding: UTF-8
import re
from slackbot.bot import respond_to
from slackbot.bot import listen_to


DONATE = "Donate directly via PayPal to 'finance@unallocatedspace.org' \n or learn about other ways to contribute at: https://www.unallocatedspace.org/contribute/"


@respond_to('!donate$', re.IGNORECASE)
def hello_reply(message):
    message.reply(DONATE)


@listen_to('!donate$', re.IGNORECASE)
def hello_send(message):
    message.send(DONATE)



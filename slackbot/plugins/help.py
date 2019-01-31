#coding: UTF-8
import re
from slackbot.bot import respond_to
from slackbot.bot import listen_to

DEFAULT = ["Help Menu:\n",
        "!8ball - predicts the future\n",
        "!about - Provide basic information about Unallocated Space\n",
        "!address - Paste address for Unallocated Space\n",
        "!donate - provide Paypal address and link to contribute web page\n",
        "!hello - Hello!\n",
        "!help - this menu\n",
        "!info - post picture of wall and open/closed status of space\n",
        "!phone - Phone number for space\n",
        "!quote - Tells you a random quote\n",
        "!randomquote - same thing as !quote\n",
        "!status - Is the space open or closed?\n",
        "!upload - no idea\n",
        "!wall - picture of the Wall of Needs\n"]

DEFAULT_REPLY = ''

for item in DEFAULT:
        DEFAULT_REPLY+=item

@respond_to('!help$', re.IGNORECASE)
def hello_reply(message):
    message.reply(DEFAULT_REPLY)


@listen_to('!help$', re.IGNORECASE)
def hello_send(message):
    message.send(DEFAULT_REPLY)



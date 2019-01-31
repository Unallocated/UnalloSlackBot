#coding: UTF-8
import re
from slackbot.bot import respond_to
from slackbot.bot import listen_to
import random

QUOTES = [
	"quote1",
	"quote2",
	"quote3",
	"quote4",
	"quote5",
	"You rolled a 6",
       ] 


@respond_to('!quotes$', re.IGNORECASE)
def hello_reply(message):
    message.reply(str(random.choice(QUOTES)))


@listen_to('!quotes$', re.IGNORECASE)
def hello_send(message):
    message.send(str(random.choice(QUOTES)))



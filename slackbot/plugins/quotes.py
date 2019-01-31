#coding: UTF-8
import re
from slackbot.bot import respond_to
from slackbot.bot import listen_to
import random

QUOTES = [
	"Dai dunno! -- Usako",
	"...",
	"quote3",
	"quote4",
	"quote5",
	"You rolled a 6",
       ] 


@respond_to('!quote$', re.IGNORECASE)
def hello_reply(message):
    message.reply(str(random.choice(QUOTES)))


@listen_to('!quote$', re.IGNORECASE)
def hello_send(message):
    message.send(str(random.choice(QUOTES)))

@respond_to('!randomquote$', re.IGNORECASE)
def hello_reply(message):
    message.reply(str(random.choice(QUOTES)))


@listen_to('!randomquote$', re.IGNORECASE)
def hello_send(message):
    message.send(str(random.choice(QUOTES)))

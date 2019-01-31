#coding: UTF-8
import re
from slackbot.bot import respond_to
from slackbot.bot import listen_to
import random

ANSWERS = [
	"As I see it, yes",
	"It is certain",
	"It is decidedly so",
	"Most likely",
	"Outlook good",
	"Signs point to yes",
	"Without a doubt",
	"Yes",
	"Yes - definitely",
	"You may rely on it",
	"Reply hazy, try again",
	"Ask again later",
	"Better not tell you now",
	"Cannot predict now",
	"Concentrate and ask again",
	"Don't count on it",
	"My reply is no",
	"My sources say no",
	"Outlook not so good",
	"Very doubtful",
       ] 

@respond_to('!8ball$', re.IGNORECASE)
def hello_reply(message):
    message.reply(str(random.choice(ANSWERS)))


@listen_to('!8ball$', re.IGNORECASE)
def hello_send(message):
    message.sendstr(random.choice(ANSWERS)))



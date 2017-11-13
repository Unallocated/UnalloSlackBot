#coding: UTF-8
from slackbot.bot import listen_to
from slackbot.bot import respond_to
import urllib3
import re

url = 'https://www.unallocatedspace.org/status'
http = urllib3.PoolManager()

r = http.request('GET', url)


@respond_to('!status', re.IGNORECASE)
def status_reply(message):
    message.reply(r.data)

@listen_to('!status$')
def status(message):
    message.send(r.data)


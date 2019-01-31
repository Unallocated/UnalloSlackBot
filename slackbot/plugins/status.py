#coding: UTF-8
from slackbot.bot import listen_to
from slackbot.bot import respond_to
import urllib3
import re

def checkstatus():
    url = 'https://www.unallocatedspace.org/status'
    http = urllib3.PoolManager()
    r = http.request('GET', url)
    return r.data

@respond_to('!status$', re.IGNORECASE)
def status_reply(message):
    message.reply(checkstatus())

@listen_to('!status$', re.IGNORECASE)
def status(message):
    message.send(checkstatus())


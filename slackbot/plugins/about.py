#coding: UTF-8
import re
from slackbot.bot import respond_to
from slackbot.bot import listen_to


ABOUT = "Unallocated Space is a technology-based community center, based out of a 1600+ SF space located in Severn, MD.  While our community shares a diverse range of interests, from electronics to woodworking, our primary focus tends to lie in Information Security.  Our members offer a steady stream of talks, classes, and other events which are all free of charge and open to the public at large. Our motto is: \"Teach, Learn, Build.\" \n Mission Statement: To foster creative and technical growth through open collaboration by providing tools and resources within the greater Baltimore-Washington Metro area."


@respond_to('!about$', re.IGNORECASE)
def hello_reply(message):
    message.reply(ABOUT)


@listen_to('!about$', re.IGNORECASE)
def hello_send(message):
    message.send(ABOUT)



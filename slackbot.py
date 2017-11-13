#!/usr/bin/env python3

from slackclient import SlackClient

slack_token = os.environ["SLACK_API_TOKEN"]
sc = SlackClient(slack_token)

sc.api_call(
  "chat.postMessage",
  channel="#python",
  text="Hello from Python! :tada:"
)

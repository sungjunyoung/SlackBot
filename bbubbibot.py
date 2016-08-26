#-*- coding: utf-8 -*-

import os
import time
from slackclient import SlackClient


# starterbot's ID as an environment variable
BOT_ID = os.environ.get("BOT_ID")

EXAMPLE_COMMAND = "안녕".decode('utf-8')

# instantiate Slack & Twilio clients
slack_client = SlackClient(os.environ.get('SLACK_BOT_TOKEN'))

def handle_command(command, channel):
    response = "못알아먹겟다 쀼ㅃ쀼삐".decode('utf-8')
    if command.startswith(EXAMPLE_COMMAND):
        response = "쀼삐쀼쀼쀼삐안녕안녕하이하이".decode('utf-8')
    slack_client.api_call("chat.postMessage", channel=channel,
                          text=response, as_user=True)


def parse_slack_output(slack_rtm_output):
    print "call parse_slack_output!"
    """
        The Slack Real Time Messaging API is an events firehose.
        this parsing function returns None unless a message is
        directed at the Bot, based on its ID.
    """
    output_list = slack_rtm_output
    if output_list and len(output_list) > 0:

        for output in output_list:
            print output
            if output and 'text' in output and output['user'] != BOT_ID:
                # return text after the @ mention, whitespace removed
                return output['text'], output['channel']
    return None, None


if __name__ == "__main__":
    READ_WEBSOCKET_DELAY = 1 # 1 second delay between reading from firehose
    if slack_client.rtm_connect():
        print("StarterBot connected and running!")
        while True:
            command, channel = parse_slack_output(slack_client.rtm_read())
            if command and channel:
                handle_command(command, channel)
            time.sleep(READ_WEBSOCKET_DELAY)
    else:
        print("Connection failed. Invalid Slack token or bot ID?")

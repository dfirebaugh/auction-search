
import json
import requests

# Set the webhook_url to the one provided by Slack when you create the webhook at https://my.slack.com/services/new/incoming-webhook/
class SlackHook:
    def __init__(self, hook):
        self.hook_url = hook
    def send(self, text):
        slack_data = {'text': "Auctions: ```{}```".format(text)}

        response = requests.post(
            self.hook_url, data=json.dumps(slack_data),
            headers={'Content-Type': 'application/json'}
        )

        if response.status_code != 200:
            raise ValueError(
                'Request to slack returned an error %s, the response is:\n%s'
                % (response.status_code, response.text)
            )

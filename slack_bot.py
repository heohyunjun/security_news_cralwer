from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler

class SlackBot:
    def __init__(self, token):
        self.app = App(token=token)

    def send_message_to_slack_channel(self, channel, text):
        try:
            self.app.client.chat_postMessage(
                channel=channel,
                text=text
            )
        except Exception as e:
            print(f"Error sending message to Slack: {e}")

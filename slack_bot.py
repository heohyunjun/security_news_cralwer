"""
Author: [Heo Hyun Jun]
Description: A SlackBot class that allows sending messages to a specified Slack channel using the Slack Bolt library.
Creation Date: 2023-04-09
"""

from slack_bolt import App
from typing import Optional

class SlackBot:
    def __init__(self, token: str):
        self.app = App(token=token)

    def send_message_to_slack_channel(self, channel: str, text: str) -> Optional[bool]:
        """
        Send a message to a specified Slack channel.
        
        Args:
            channel (str): The ID of the Slack channel to send the message to.
            text (str): The content of the message to send.
            
        Returns:
            Optional[bool]: True if the message was sent successfully, None if an error occurred.
        """
        
        try:
            self.app.client.chat_postMessage(
                channel=channel,
                text=text
            )
            return True
        except Exception as e:
            print(f"Error sending message to Slack: {e}")
            return None

import requests
from bs4 import BeautifulSoup
import urllib3
from config import SLACK_CHANNEL_ID, SLACK_BOT_TOKEN
from utils import extract_href_and_text, get_date_about_news, is_within_time_range
from slack_bot import SlackBot

def main():
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    main_url = 'https://www.boannews.com'
    url = 'https://www.boannews.com/media/t_list.asp'
    response = requests.get(url, verify=False)
    soup = BeautifulSoup(response.text, "html.parser")

    news_area = soup.select_one('#news_area')
    news_items = news_area.select('div.news_list')

    # Initialize SlackBot instance
    SLACK_BOT_TOKEN = os.environ.get("SLACK_BOT_TOKEN")
    SLACK_CHANNEL_ID = os.environ.get("SLACK_CHANNEL_ID")
    slack_bot = SlackBot(SLACK_BOT_TOKEN)

    news_found = False

    for news_item in news_items:
        is_today_news = False
        if 'news_list' in news_item['class']:
            # ... 이전 코드 ...

            is_today_news = is_within_time_range(news_date)
            href, text = extract_href_and_text(news_item)
            if is_today_news:
                news_found = True
                message = f"Date: {news_date}\nLink: {main_url + href}\nTitle: {text}"
                slack_bot.send_message_to_slack_channel(SLACK_CHANNEL_ID, message)
                print(message)
            else:
                print("오늘 아님")

    if not news_found:
        slack_bot.send_message_to_slack_channel(SLACK_CHANNEL_ID, "뉴스가 없습니다.")

if __name__ == "__main__":
    main()

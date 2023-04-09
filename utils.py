import re
import datetime

def send_message_to_slack_channel(channel, text):
    try:
        app.client.chat_postMessage(
            channel=channel,
            text=text
        )
    except Exception as e:
        print(f"Error sending message to Slack: {e}")
        
def extract_href_and_text(news_item):
    link = None
    text = None

    a_tag = news_item.select_one('a')
    if a_tag:
        link = a_tag['href']
        text = a_tag.text.strip()

    return link, text


def get_date_about_news(date_element):
    if date_element:
        date_pattern = r"(\d{4})년 (\d{2})월 (\d{2})일 (\d{2}:\d{2})"
        match = re.search(date_pattern, date_element)
        
        if match:
            # Extract and return the date
            date_str = match.group()
            return date_str
        else:
            print("Date not found")
            return None
    else:
        print("Date element not found")
        return None

def is_time_between(target, start, end):
    if start <= end:
        return start <= target <= end
    else:
        return start <= target or target <= end

def is_within_time_range(date_info):
    # Set the current_datetime to April 8, 2023, 04:50 for testing
    current_datetime = datetime.datetime(2023, 4, 8, 14, 50)
    # current_datetime = datetime.datetime.now()
    current_time = current_datetime.time()

    start_range_1 = datetime.time(4, 0)
    end_range_1 = datetime.time(5, 0)
    start_range_2 = datetime.time(14, 0)
    end_range_2 = datetime.time(15, 0)

    date_time_obj = datetime.datetime.strptime(date_info, '%Y년 %m월 %d일 %H:%M')
    target_time = date_time_obj.time()

    if is_time_between(current_time, start_range_1, end_range_1):
        previous_day_end_range = current_datetime - datetime.timedelta(days=1)
        previous_day_end_range_time = previous_day_end_range.time()

        if date_time_obj.date() == previous_day_end_range.date() and is_time_between(target_time, datetime.time(15, 0), datetime.time(23, 59, 59)):
            return True
        elif date_time_obj.date() == current_datetime.date() and is_time_between(target_time, datetime.time(0, 0), current_time):
            return True
        else:
            return False
    elif is_time_between(current_time, start_range_2, end_range_2):
        if is_time_between(target_time, datetime.time(5, 0), datetime.time(15, 0)):
            return True
        else:
            return False
    else:
        return False
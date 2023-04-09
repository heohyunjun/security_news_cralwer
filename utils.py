"""
Author: [Heo Hyun Jun]
Description: A script to send a list of recent news articles to a specified Slack channel, based on the given time range.
Creation Date: 2023-04-09
"""


import re
import datetime

from bs4.element import Tag
from typing import Optional, Tuple


def extract_href_and_text(news_item: Tag) -> Tuple[Optional[str], Optional[str]]:
    link = None
    title = None

    a_tag = news_item.select_one('a')
    if a_tag:
        link = a_tag['href']
        title = a_tag.text.strip()

    return link, title


def extract_date_from_element(date_element: str) -> Optional[str]:
    if date_element:
        date_pattern = r"(\d{4})년 (\d{2})월 (\d{2})일 (\d{2}:\d{2})"
        match = re.search(date_pattern, date_element)
        
        if match:
            date_str = match.group()
            return date_str
        else:
            print("Date not found")
            return None
    else:
        print("Date element not found")
        return None

def is_time_between(target: datetime.time, start: datetime.time, end: datetime.time) -> bool:
    if start <= end:
        return start <= target <= end
    else:
        return start <= target or target <= end


def is_within_specified_time_range(date_info: str) -> bool:
    current_datetime = datetime.datetime.now()
    current_time = current_datetime.time()

    start_range_1 = datetime.time(4, 0)
    end_range_1 = datetime.time(5, 0)
    start_range_2 = datetime.time(14, 0)
    end_range_2 = datetime.time(15, 0)

    date_time_obj = datetime.datetime.strptime(date_info, '%Y년 %m월 %d일 %H:%M')
    target_time = date_time_obj.time()

    if is_time_between(current_time, start_range_1, end_range_1):
        previous_day_end_range = current_datetime - datetime.timedelta(days=1)

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

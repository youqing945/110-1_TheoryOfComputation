import os

from linebot import LineBotApi, WebhookParser
from linebot.models import *
from linebot.models.send_messages import *
import urllib
import re
import random

channel_access_token = os.getenv("LINE_CHANNEL_ACCESS_TOKEN", None)


def send_text_message(reply_token, text):
    line_bot_api = LineBotApi(channel_access_token)
    line_bot_api.reply_message(reply_token, TextSendMessage(text=text))

    return "OK"

def send_image_url(reply_token, img_url):
    line_bot_api = LineBotApi(channel_access_token)
    line_bot_api.reply_message(reply_token, ImageSendMessage(
        original_content_url=img_url,
        preview_image_url=img_url
    ))

def add_text(text):
    return TextSendMessage(text=text)

def add_image(url):
    return ImageSendMessage(
        original_content_url=url,
        preview_image_url=url
    )

def send_all_message(reply_token, message):
    line_bot_api = LineBotApi(channel_access_token)
    line_bot_api.reply_message(reply_token, message)


def get_random_google_image(search_text):
    img_list = []
    random_img_url = 'https://image-cdn.hypb.st/https%3A%2F%2Fhk.hypebeast.com%2Ffiles%2F2021%2F08%2Fnever-gonna-give-you-up-passes-one-billion-views-01.jpg?w=960&cbr=1&q=90&fit=max'

    try:
        img_search = {'tbm': 'isch', 'q': search_text}
        #img_search = {'tbm': 'isch', 'q': '讚 手勢'}
        query = urllib.parse.urlencode(img_search)
        base  = "https://www.google.com/search?"
        url   = str(base+query)

        headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'}

        res  = urllib.request.Request(url, headers=headers)
        con  = urllib.request.urlopen(res)
        data = con.read()

        pattern = '"(https://encrypted-tbn0.gstatic.com[\S]*)"'

        for match in re.finditer(pattern, str(data, "utf-8")):
            if len(match.group(1)) < 150:
                img_list.append(match.group(1))
    
        random_img_url = img_list[random.randint(0, len(img_list)+1)]
    except:
        random_img_url = 'https://image-cdn.hypb.st/https%3A%2F%2Fhk.hypebeast.com%2Ffiles%2F2021%2F08%2Fnever-gonna-give-you-up-passes-one-billion-views-01.jpg?w=960&cbr=1&q=90&fit=max'

    return random_img_url

"""
def send_image_url(id, img_url):
    pass

def send_button_message(id, text, buttons):
    pass
"""

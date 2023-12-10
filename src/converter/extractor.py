import pandas as pd
import json


def extract_offset_time(dat: dict) -> int:
    offset_time = int(dat["replayChatItemAction"]["videoOffsetTimeMsec"])
    return offset_time


def extract_live_chat_text_message_render(dat: dict) -> dict:
    actions = dat["replayChatItemAction"]["actions"]
    return actions[0]["addChatItemAction"]["item"]["liveChatTextMessageRenderer"]


def extract_message_text(message_render: dict) -> str:
    return message_render["message"]["runs"][0]["text"]


def extract_author_ch_id(message_render: dict) -> str:
    return message_render["authorExternalChannelId"]


def extract_author_name(message_render: dict) -> str:
    return message_render["authorName"]["simpleText"]


def extract_timestamp_text(message_render: dict):
    return message_render["timestampText"]["simpleText"]

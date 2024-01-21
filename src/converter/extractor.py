import pandas as pd
import json


def extract_offset_time(dat: dict) -> int:
    offset_time = int(dat["replayChatItemAction"]["videoOffsetTimeMsec"])
    return offset_time


def extract_live_chat_text_message_render(dat: dict) -> dict:
    actions = dat["replayChatItemAction"]["actions"]
    return actions[0]["addChatItemAction"]["item"]["liveChatTextMessageRenderer"]


def extract_message_text(message_render: dict) -> str:
    number_of_messages = len(message_render["message"]["runs"])
    connected_text = ""
    for i in range(number_of_messages):
        connected_text += extract_partial_text(message_render["message"]["runs"][i])
    return connected_text


def extract_partial_text(partial_text_dict):
    if "text" in partial_text_dict.keys():
        return partial_text_dict["text"]
    elif "emoji" in partial_text_dict.keys():
        return convert_emoji_to_emoji_text(partial_text_dict["emoji"])


def convert_emoji_to_emoji_text(emoji_dict):
    # TODO: emoji_textとsvgの対応関係を辞書にする.
    if "shortcuts" in emoji_dict.keys():
        emoji_text = "emoji_" + emoji_dict["shortcuts"][0]
        return emoji_text
    else:
        return emoji_dict["emojiId"]


def extract_author_ch_id(message_render: dict) -> str:
    return message_render["authorExternalChannelId"]


def extract_author_name(message_render: dict) -> str:
    return message_render["authorName"]["simpleText"]


def extract_timestamp_text(message_render: dict):
    return message_render["timestampText"]["simpleText"]

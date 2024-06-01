import pandas as pd
from box import Box


def _convert_emoji_to_emoji_text(emoji_dict):
    # TODO: emoji_textとsvgの対応関係を辞書にする.
    if "shortcuts" in emoji_dict.keys():
        emoji_text = "emoji_" + emoji_dict["shortcuts"][0]
        return emoji_text
    else:
        return emoji_dict["emojiId"]


def _extract_partial_text(partial_text_dict):
    if "text" in partial_text_dict.keys():
        return partial_text_dict["text"]
    elif "emoji" in partial_text_dict.keys():
        return _convert_emoji_to_emoji_text(partial_text_dict["emoji"])


class TextBox:
    def __init__(self, dat):
        self.box = Box(dat)
        self.message_render = self.box.replayChatItemAction.actions[
            0
        ].addChatItemAction.item.liveChatTextMessageRenderer

    def extract_offset_time(self):
        offset_time = self.box.replayChatItemAction.videoOffsetTimeMsec
        return int(offset_time)

    def extract_timestamp_text(self):
        return self.message_render.timestampText.simpleText

    def extract_message_text(self):
        number_of_messages = self.message_render.message.runs
        connected_text = ""
        for message in number_of_messages:
            connected_text += _extract_partial_text(message)
        return connected_text

    def extract_author_ch_id(self) -> str:
        return self.message_render.authorExternalChannelId

    def extract_author_name(self) -> str:
        return self.message_render.authorName.simpleText


class SuperChatBox:
    def __init__(self, dat):
        self.box = Box(dat)
        self.paid_message = self.box.replayChatItemAction.actions[
            0
        ].addChatItemAction.item.liveChatPaidMessageRenderer

    def extract_supacha(self) -> str:
        return self.paid_message.purchaseAmountText.simpleText

    def extract_offset_time(self) -> str:
        return self.box.replayChatItemAction.videoOffsetTimeMsec

    def extract_timestamp_text(self):
        return self.paid_message.timestampText.simpleText

    def extract_message_text(self):
        if not "message" in self.paid_message.keys():
            return ""
        number_of_messages = self.paid_message.message.runs
        connected_text = ""
        for message in number_of_messages:
            connected_text += _extract_partial_text(message)
        return connected_text

    def extract_author_ch_id(self):
        return self.paid_message.authorExternalChannelId

    def extract_author_name(self):
        return self.paid_message.authorName.simpleText

import os
import json
from types import *
from src.converter import extractor
import pytest


@pytest.fixture
def dat():
    dat = json.loads(
        '{"replayChatItemAction": {"actions": [{"addChatItemAction": {"item": {"liveChatTextMessageRenderer": {"message": {"runs": [{"text": "実権だよ実権"}]}, "authorName": {"simpleText": "ばぼー"}, "authorPhoto": {"thumbnails": [{"url": "https://yt4.ggpht.com/ytc/APkrFKan9lFRJ-SvQQzHyafMBkd46NRWFNVSA9NFnbgq=s32-c-k-c0x00ffffff-no-rj", "width": 32, "height": 32}, {"url": "https://yt4.ggpht.com/ytc/APkrFKan9lFRJ-SvQQzHyafMBkd46NRWFNVSA9NFnbgq=s64-c-k-c0x00ffffff-no-rj", "width": 64, "height": 64}]}, "contextMenuEndpoint": {"commandMetadata": {"webCommandMetadata": {"ignoreNavigation": true}}, "liveChatItemContextMenuEndpoint": {"params": "Q2g0S0hBb2FRMHBVTlY5S1N6TjJiMGxFUmxsWVEzZG5VV1F0UkdkTk1XY2FLU29uQ2hoVlEwbGtSVWxJY0ZNd1ZHUnJjVkpyU0V3MVQydE1kRUVTQ3kweWNpMTZaa1ZKZG5CVklBRW9BVElhQ2hoVlF6QjFkMGw2YnpFdFZXaENNekpuZDFCamJtOUhRbmM0QWtnQlVBRSUzRA=="}}, "id": "ChwKGkNKVDVfSkszdm9JREZZWEN3Z1FkLURnTTFn", "timestampUsec": "1699791060827284", "authorExternalChannelId": "UC0uwIzo1-UhB32gwPcnoGBw", "contextMenuAccessibility": {"accessibilityData": {"label": "Chat actions"}}, "timestampText": {"simpleText": "6:44"}}}, "clientId": "CJT5_JK3voIDFYXCwgQd-DgM1g"}}], "videoOffsetTimeMsec": "404469"}}'
    )
    return dat


def test_extract_live_chat_text_message_render(dat):
    message_render = extractor.extract_live_chat_text_message_render(dat)
    assert len(message_render.keys()) > 0


def test_extract_offset_time(dat):
    offset_time = extractor.extract_offset_time(dat)
    assert type(offset_time) == int


def test_extract_message_text(dat):
    message_render = extractor.extract_live_chat_text_message_render(dat)
    message_text = extractor.extract_message_text(message_render)
    assert type(message_text) == str


def test_extract_author_ch_id(dat):
    message_render = extractor.extract_live_chat_text_message_render(dat)
    author_ch_id = extractor.extract_author_ch_id(message_render)
    assert len(author_ch_id) > 5
    assert type(author_ch_id) == str


def test_extract_author_name(dat):
    message_render = extractor.extract_live_chat_text_message_render(dat)
    author_name = extractor.extract_author_name(message_render)
    assert len(author_name) > 0
    assert type(author_name) == str


def test_extract_timestamp_text(dat):
    message_render = extractor.extract_live_chat_text_message_render(dat)
    timestamp_text = extractor.extract_timestamp_text(message_render)
    assert len(timestamp_text) > 0
    assert type(timestamp_text) == str

import os
import json
from types import *
from src.converter import extractor
import pytest


class TestTextExtract:
    @pytest.fixture
    def dat(self):
        dat = json.loads(
            '{"replayChatItemAction": {"actions": [{"addChatItemAction": {"item": {"liveChatTextMessageRenderer": {"message": {"runs": [{"text": "実権だよ実権"}]}, "authorName": {"simpleText": "ばぼー"}, "authorPhoto": {"thumbnails": [{"url": "https://yt4.ggpht.com/ytc/APkrFKan9lFRJ-SvQQzHyafMBkd46NRWFNVSA9NFnbgq=s32-c-k-c0x00ffffff-no-rj", "width": 32, "height": 32}, {"url": "https://yt4.ggpht.com/ytc/APkrFKan9lFRJ-SvQQzHyafMBkd46NRWFNVSA9NFnbgq=s64-c-k-c0x00ffffff-no-rj", "width": 64, "height": 64}]}, "contextMenuEndpoint": {"commandMetadata": {"webCommandMetadata": {"ignoreNavigation": true}}, "liveChatItemContextMenuEndpoint": {"params": "Q2g0S0hBb2FRMHBVTlY5S1N6TjJiMGxFUmxsWVEzZG5VV1F0UkdkTk1XY2FLU29uQ2hoVlEwbGtSVWxJY0ZNd1ZHUnJjVkpyU0V3MVQydE1kRUVTQ3kweWNpMTZaa1ZKZG5CVklBRW9BVElhQ2hoVlF6QjFkMGw2YnpFdFZXaENNekpuZDFCamJtOUhRbmM0QWtnQlVBRSUzRA=="}}, "id": "ChwKGkNKVDVfSkszdm9JREZZWEN3Z1FkLURnTTFn", "timestampUsec": "1699791060827284", "authorExternalChannelId": "UC0uwIzo1-UhB32gwPcnoGBw", "contextMenuAccessibility": {"accessibilityData": {"label": "Chat actions"}}, "timestampText": {"simpleText": "6:44"}}}, "clientId": "CJT5_JK3voIDFYXCwgQd-DgM1g"}}], "videoOffsetTimeMsec": "404469"}}'
        )
        return dat

    def test_extract_offset_time(self, dat):
        box = extractor.TextBox(dat)
        offset_time = box.extract_offset_time()
        assert type(offset_time) == int

    def test_extract_timestamp_text(self, dat):
        box = extractor.TextBox(dat)
        timestamp_text = box.extract_extract_timestamp_text()
        assert len(timestamp_text) > 0
        assert type(timestamp_text) == str

    def test_extract_message_text(self, dat):
        box = extractor.TextBox(dat)
        message_text = box.extract_message_text()
        assert type(message_text) == str

    def test_extract_author_ch_id(self, dat):
        box = extractor.TextBox(dat)
        author_ch_id = box.extract_author_ch_id()
        assert len(author_ch_id) > 5
        assert type(author_ch_id) == str

    def test_extract_author_name(self, dat):
        box = extractor.TextBox(dat)
        author_name = box.extract_author_name()
        assert len(author_name) > 0
        assert type(author_name) == str

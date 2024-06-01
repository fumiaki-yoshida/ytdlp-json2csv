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


class TestSuparchatExtractor:
    @pytest.fixture
    def dat(self):
        dat = json.loads(
            '{"clickTrackingParams": "CAEQl98BIhMI4bHM36iEgwMVStY0Bx1_ngeP", "replayChatItemAction": {"actions": [{"clickTrackingParams": "CAEQl98BIhMI4bHM36iEgwMVStY0Bx1_ngeP", "addChatItemAction": {"item": {"liveChatPaidMessageRenderer": {"id": "ChwKGkNOX205ZlhoXzRJREZlREN3Z1FkVXRNREdB", "timestampUsec": "1702035936310277", "authorName": {"simpleText": "Elegy"}, "authorPhoto": {"thumbnails": [{"url": "https://yt4.ggpht.com/ytc/APkrFKY9fleb21ELh-a9N7khP1UQKw4vpEmhG672zwV9EA=s32-c-k-c0x00ffffff-no-rj", "width": 32, "height": 32}, {"url": "https://yt4.ggpht.com/ytc/APkrFKY9fleb21ELh-a9N7khP1UQKw4vpEmhG672zwV9EA=s64-c-k-c0x00ffffff-no-rj", "width": 64, "height": 64}]}, "purchaseAmountText": {"simpleText": "¥370"}, "headerBackgroundColor": 4278237396, "headerTextColor": 4278190080, "bodyBackgroundColor": 4278248959, "bodyTextColor": 4278190080, "authorExternalChannelId": "UCld0xQDcgJ4cijHI4DgSLIg", "authorNameTextColor": 3003121664, "contextMenuEndpoint": {"clickTrackingParams": "CAIQ7rsEIhMI4bHM36iEgwMVStY0Bx1_ngeP", "commandMetadata": {"webCommandMetadata": {"ignoreNavigation": true}}, "liveChatItemContextMenuEndpoint": {"params": "Q2g0S0hBb2FRMDVmYlRsbVdHaGZORWxFUm1WRVEzZG5VV1JWZEUxRVIwRWFLU29uQ2hoVlEwbGtSVWxJY0ZNd1ZHUnJjVkpyU0V3MVQydE1kRUVTQzI1RkxWQjVOMU5XT0VsUklBRW9BVElhQ2hoVlEyeGtNSGhSUkdOblNqUmphV3BJU1RSRVoxTk1TV2M0QWtnQlVBOCUzRA=="}}, "timestampColor": 2147483648, "contextMenuAccessibility": {"accessibilityData": {"label": "Chat actions"}}, "timestampText": {"simpleText": "45:29"}, "trackingParams": "CAIQ7rsEIhMI4bHM36iEgwMVStY0Bx1_ngeP", "textInputBackgroundColor": 822083583, "creatorHeartButton": {"creatorHeartViewModel": {"creatorThumbnail": {"sources": [{"url": "https://yt3.ggpht.com/Qj-lyidMW6xtEdnv6rDYscGE1kO6K06-i4v8Eiij96YOTo_WdBboLVlEKeE3749ywpyqTec2=s48-c-k-c0x00ffffff-no-rj"}]}, "heartedIcon": {"sources": [{"clientResource": {"imageName": "full_heart-filled"}}]}, "unheartedIcon": {"sources": [{"clientResource": {"imageName": "full_heart"}}], "processor": {"borderImageProcessor": {"imageTint": {"color": 4278190080}}}}, "heartedHoverText": "❤ by さなちゃんねる", "heartedAccessibilityLabel": "Remove heart", "unheartedAccessibilityLabel": "Heart", "engagementStateKey": "EktsaXZlLWNoYXQtbWVzc2FnZS1lbmdhZ2VtZW50LXN0YXRlLUNod0tHa05PWDIwNVpsaG9YelJKUkVabFJFTjNaMUZrVlhSTlJFZEIgLCgB"}}, "isV2Style": true}}, "clientId": "CN_m9fXh_4IDFeDCwgQdUtMDGA"}}], "videoOffsetTimeMsec": "2729188"}}'
        )
        return dat

    def test_extract_supacha_money(self, dat):
        box = extractor.SuperChatBox(dat)
        assert "¥370" == box.extract_supacha()

    def test_extract_offset_time(self, dat):
        box = extractor.SuperChatBox(dat)
        assert "2729188" == box.extract_offset_time()

    def test_extract_extract_timestamp_text(self, dat):
        box = extractor.SuperChatBox(dat)
        assert "45:29" == box.extract_timestamp_text()

    def test_extract_message_text(self, dat):
        box = extractor.SuperChatBox(dat)
        assert "" == box.extract_message_text()
        # TODO: スパチャでメッセージが入っているケースのデータを用意する。

    def test_extract_author_ch_id(self, dat):
        box = extractor.SuperChatBox(dat)
        assert "UCld0xQDcgJ4cijHI4DgSLIg" == box.extract_author_ch_id()

    def test_extract_author_name(self, dat):
        box = extractor.SuperChatBox(dat)
        assert "Elegy" == box.extract_author_name()

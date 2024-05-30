import json
from src.converter import extractor
import pandas as pd


def open_files2list(file_path):
    with open(file_path, encoding="utf-8") as f:
        lines = f.readlines()
    return lines


def split_comment_and_clickTrackingParams(lines):
    comments = []
    click_tp = []
    for dat in lines:
        dat = json.loads(dat)
        if "clickTrackingParams" in dat:
            click_tp.append(dat)
        else:
            comments.append(dat)
    return comments, click_tp


def make_dataframe(file_path):
    lines = open_files2list(file_path)
    comments, _ = split_comment_and_clickTrackingParams(lines)
    message_dict = {
        "offset_time": [],
        "timestamp_text": [],
        "message_text": [],
        "author_ch_id": [],
        "author_name": [],
    }

    for dat in comments:
        if (
            "removeBannerForLiveChatCommand"
            in dat["replayChatItemAction"]["actions"][0].keys()
        ):
            # おそらくslow_modeを配信者が設定したお知らせ。
            continue

        elif (
            "addBannerToLiveChatCommand"
            in dat["replayChatItemAction"]["actions"][0].keys()
        ):
            # ピン止めされたコメントについての行
            continue
        elif (
            "liveChatTextMessageRenderer"
            in dat["replayChatItemAction"]["actions"][0]["addChatItemAction"][
                "item"
            ].keys()
        ):
            # message_render = extractor.extract_live_chat_text_message_render(dat)
            box = extractor.Box(dat)
        elif (
            "liveChatPlaceholderItemRenderer"
            in dat["replayChatItemAction"]["actions"][0]["addChatItemAction"][
                "item"
            ].keys()
        ):
            continue

        elif "removeBannerForLiveChatCommand" in dat["replayChatItemActionda"].keys():
            continue
        else:
            message_dict["offset_time"].append(box.extract_offset_time())
            message_dict["timestamp_text"].append(
                box.extract_timestamp_text()
            )
            message_dict["message_text"].append(
                box.extract_message_text()
            )
            message_dict["author_ch_id"].append(
                box.extract_author_ch_id()
            )
            message_dict["author_name"].append(
                box.extract_author_name()
            )
    return pd.DataFrame(message_dict)

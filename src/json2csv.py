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


def make_dict_with_TextBox(dat, message_dict):
    box = extractor.TextBox(dat)
    message_dict["offset_time"].append(box.extract_offset_time())
    message_dict["timestamp_text"].append(box.extract_timestamp_text())
    message_dict["message_text"].append(box.extract_message_text())
    message_dict["author_ch_id"].append(box.extract_author_ch_id())
    message_dict["author_name"].append(box.extract_author_name())
    message_dict["fee"].append("")
    return message_dict


def make_dict_with_SuperChatBox(dat, message_dict):
    box = extractor.SuperChatBox(dat)
    message_dict["offset_time"].append(box.extract_offset_time())
    message_dict["timestamp_text"].append(box.extract_timestamp_text())
    message_dict["message_text"].append(box.extract_message_text())
    message_dict["author_ch_id"].append(box.extract_author_ch_id())
    message_dict["author_name"].append(box.extract_author_name())
    message_dict["fee"].append(box.extract_fee_str())
    return message_dict


def _has_addChatItemAction(dat):
    return "addChatItemAction" in dat["replayChatItemAction"]["actions"][0].keys()


def _has_addLiveChatTickerItemAction(dat):
    return (
        "addLiveChatTickerItemAction"
        in dat["replayChatItemAction"]["actions"][0].keys()
    )


def _has_liveChatViewerEngagementMessageRenderer(dat):
    return (
        "liveChatViewerEngagementMessageRenderer"
        in dat["replayChatItemAction"]["actions"][0]["addChatItemAction"]["item"].keys()
    )


def _has_liveChatPlaceholderItemRenderer(dat):
    return (
        "liveChatPlaceholderItemRenderer"
        in dat["replayChatItemAction"]["actions"][0]["addChatItemAction"]["item"].keys()
    )


def _has_removeBannerForLiveChatCommand(dat):
    return "removeBannerForLiveChatCommand" in dat["replayChatItemAction"].keys()


def _has_liveChatPaidMessageRenderer(dat):
    return (
        "liveChatPaidMessageRenderer"
        in dat["replayChatItemAction"]["actions"][0]["addChatItemAction"]["item"].keys()
    )


def _has_liveChatTextMessageRenderer(dat):
    if _has_addChatItemAction(dat):
        return (
            "liveChatTextMessageRenderer"
            in dat["replayChatItemAction"]["actions"][0]["addChatItemAction"][
                "item"
            ].keys()
        )
    # has_clickTrackingParams()


def _has_clickTrackingParams(dat):
    return "clickTrackingParams" in dat


def make_dataframe(file_path):
    lines = open_files2list(file_path)
    # comments, click_tp = split_comment_and_clickTrackingParams(lines)
    message_dict = {
        "offset_time": [],
        "timestamp_text": [],
        "message_text": [],
        "author_ch_id": [],
        "author_name": [],
        "fee": [],
    }

    # TODO:addChatItemActionとclickTrackingParamsで場合分けする
    # replayChatItemAction のkey以降を渡せばうまく動くはずという仮説がある
    for dat in lines:
        dat = json.loads(dat)

        # おそらくslow_modeを配信者が設定したお知らせ。
        if (
            "removeBannerForLiveChatCommand"
            in dat["replayChatItemAction"]["actions"][0].keys()
        ):
            continue

        # ピン止めされたコメントについての行
        elif (
            "addBannerToLiveChatCommand"
            in dat["replayChatItemAction"]["actions"][0].keys()
        ):
            continue

        # 「ライブチャット再生中」というyoutube上の表示
        elif _has_addChatItemAction(dat):
            if _has_liveChatViewerEngagementMessageRenderer(dat):
                continue

            if _has_liveChatTextMessageRenderer(dat):
                message_dict = make_dict_with_TextBox(dat, message_dict)

        elif _has_addLiveChatTickerItemAction(dat):
            if (
                "liveChatTextMessageRenderer"
                in dat["replayChatItemAction"]["actions"][0][
                    "addLiveChatTickerItemAction"
                ]["item"].keys()
            ):
                message_dict = make_dict_with_TextBox(dat, message_dict)

        elif (_has_addChatItemAction(dat)) and (_has_liveChatPaidMessageRenderer(dat)):
            message_dict = make_dict_with_SuperChatBox(dat, message_dict)
        elif _has_addChatItemAction(dat) and _has_liveChatPlaceholderItemRenderer(dat):
            continue

        elif _has_removeBannerForLiveChatCommand(dat):
            continue

    return pd.DataFrame(message_dict)

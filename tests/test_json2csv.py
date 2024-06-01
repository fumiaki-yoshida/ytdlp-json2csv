import os
from src import json2csv


sample_file_path = os.path.join(
    os.path.dirname(__file__), "sample_folder/20231112_ch-name_title.live_chat.json"
)


def test_open_files2lists():
    lines = json2csv.open_files2list(sample_file_path)
    assert len(lines) > 10


def test_split_comment_and_clickTrackingParams():
    lines = json2csv.open_files2list(sample_file_path)
    comments, click_tp = json2csv.split_comment_and_clickTrackingParams(lines)
    assert len(comments) > len(click_tp)


def test_make_dataframe():
    df = json2csv.make_dataframe(sample_file_path)
    assert "offset_time" in df.columns
    assert "timestamp_text" in df.columns
    assert "message_text" in df.columns
    assert "author_ch_id" in df.columns
    assert "author_name" in df.columns
    assert df.shape[0] > 1
    assert df.isnull().values.sum() == 0

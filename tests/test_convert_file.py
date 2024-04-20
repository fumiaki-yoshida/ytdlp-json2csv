import convert_file


def test_convert_file_path():
    assert "hoge.csv" == convert_file.convert_file_path("hoge.live_chat.json")
    assert "converted" == convert_file.convert_file_path("raw")
    assert "./data/converted/hoge.csv" == convert_file.convert_file_path(
        "./data/raw/hoge.live_chat.json"
    )

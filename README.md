# ytdlp-json2csv

This program convert yt-dlp's `live_chat.json` to csv.


## definition

- `offset_time`: livechatが送信された時間。単位は ms。
- `timestamp_text`: 人が見やすいように変換したoffset_time。
- `message`: 送信されたlivechatの文章。
- `author_ch_id`: livechatを書いた人のID。変更されることはない。
- `author_name`: livechatを書いた人が名乗っている名前。変更される可能性がある。
  
## How To USE

1. 拡張子が`live_chat.json`の変換したいファイルを`data/raw`フォルダーに入れる。rawフォルダーの拡張子が`.live_chat.json`ファイルはすべてcsvファイルに変換されるので注意する。
2. `convert_file.py` を実行する。
3. 出力結果が`data/converted`にcsvファイルとして出力されるので確認をする。

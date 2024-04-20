import os
from glob import glob
from concurrent.futures import ProcessPoolExecutor
from tqdm import tqdm
from src import json2csv


def convert_file_path(raw_path):
    converted_path = raw_path.replace("raw", "converted").replace(
        "live_chat.json", "csv"
    )
    return converted_path


def make_converted_folder(converted_path):
    if os.path.exists(os.path.dirname(converted_path)):
        pass
    else:
        os.makedirs(os.path.dirname(converted_path))


def exec_convert(raw_path):
    converted_path = convert_file_path(raw_path)
    if not os.path.exists(converted_path):
        make_converted_folder(converted_path)
        df = json2csv.make_dataframe(raw_path)
        df.to_csv(converted_path, encoding="utf_8_sig")
    else:
        return


def main():
    raw_paths = glob("./data/raw/*/*.live_chat.json")
    with ProcessPoolExecutor(max_workers=os.cpu_count() // 2) as executor:
        tqdm(executor.map(exec_convert, raw_paths), total=len(raw_paths))


if __name__ == "__main__":
    __spec__ = None
    main()

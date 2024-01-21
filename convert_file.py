import os
from glob import glob
import pandas as pd
from src import json2csv


def convert_file_path(raw_path):
    converted_path = raw_path.replace("raw","converted").replace("live_chat.json","csv")
    return converted_path


def make_converted_folder(converted_path):
    if os.path.exists(os.path.dirname(converted_path)):
        pass
    else:
        os.makedirs(os.path.dirname(converted_path))


def main():
    raw_paths = glob("./data/raw/*.live_chat.json")
    for raw_path in raw_paths:
        converted_path = convert_file_path(raw_path)
        if not os.path.exist(converted_path):
            make_converted_folder(converted_path)
            df = json2csv.make_dataframe(raw_path)
            df.to_csv(converted_path)
        else:
            continue


if __name__ == "__main__":
    main()

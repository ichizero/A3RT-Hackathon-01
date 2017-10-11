"""
データ整形や保存ファイルのサイズ確認を行う
"""

import os
import re

def format_tweet(tweet):
    """
    取得した文章のデータ整形を行う。
    """
    tweet = re.sub(r"https*://[A-Za-z0-9.-/?=&]*", "", tweet)   # URL削除
    tweet = re.sub(r"@[A-Za-z0-9-_]*:*", "", tweet)     # ID削除
    tweet = re.sub("[(RT)・…\n(https)(http)]", "", tweet)
    tweet = re.sub(" {2,}", " ", tweet)     # 2つ以上のスペースを1つに
    tweet = re.sub("^ ", "", tweet)         # 文頭のスペースを削除
    tweet += "\n"
    return tweet

def get_line_numbers(file_path):
    """
    指定ファイルの行数を返す。
    """
    _file = open(file_path)
    line_num = sum(1 for line in _file)
    _file.close()
    return line_num


def is_max_file_size(file_path):
    """
    保存先のファイルが4MBを超えているか確認する。
    """
    return os.path.getsize(file_path) >= 4000000

"""
ズボラった〜
"""

import sys

from app.suggest import get_suggestion
from app.post import post_tweet


def main(argv):
    """
    app main function
    """

    if len(argv) < 2:
        print("2つ以上の引数が必要です。")
        sys.exit()

    tweet = ""

    # ツイート文生成
    for source_txt in argv:
        result_array = get_suggestion(source_txt)
        result_txt = source_txt + result_array[0]
        print(result_txt)
        tweet += result_txt
        tweet += "\n"

    tweet += "\nズボラった〜(https://github.com/ichizero/A3RT-Hackathon-01)より"

    # Twitterへ投稿
    post_tweet(tweet)

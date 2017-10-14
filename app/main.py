"""
main
"""

import sys

from app.suggest import get_suggestion
from app.post import post_tweet


def main(argv):
    """
    main
    """

    if len(argv) < 3:
        print("3つ以上の引数が必要です。")
        sys.exit()

    tweet = ""

    for source_txt in argv:
        result_array = get_suggestion(source_txt)
        result_txt = source_txt + result_array[0]
        print(result_txt)
        tweet += result_txt
        tweet += "\n"

    # 要約API

    # 画像検索API

    # Twitter投稿
    # post_tweet(result_txt)

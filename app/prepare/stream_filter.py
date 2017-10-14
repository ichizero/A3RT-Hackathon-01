"""
学習データセット用のテキストをTwitter Streaming APIのstatuses/fliterから取得する
"""

import os
import sys

import requests
from requests_oauthlib import OAuth1

from save import save_tweet


def main(file_path):
    """
    TwitterのStreaming APIを用いてツイートを取得し、txtファイルに保存する。

    Args:
        file_path(str): 保存先のファイル名
    """

    auth = OAuth1(os.environ['TWITTER_CSM_KEY'],
                  os.environ['TWITTER_CSM_SEC'],
                  os.environ['TWITTER_ACS_KEY'],
                  os.environ['TWITTER_ACS_SEC'])

    params = {"track": "ハロウィン"}

    # POST
    stream = requests.post(
        "https://stream.twitter.com/1.1/statuses/filter.json",
        auth=auth,
        stream=True,
        params=params
    )

    save_tweet(stream, file_path)


if __name__ == '__main__':
    if len(sys.argv) == 1:
        print("保存先のファイル名を入力してください。")
        main(input())
    else:
        main(sys.argv[1])

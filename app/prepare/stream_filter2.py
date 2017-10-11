"""
学習データセット用のテキストをTwitter Streaming APIのstatuses/fliterから取得する
"""

import os
import sys
import json

import requests
from requests_oauthlib import OAuth1

from format import format_tweet, is_max_file_size, get_line_numbers

def main():
    """
    TwitterのStreaming APIを用いてツイートを取得し、txtファイルに保存する。
    """

    auth = OAuth1(os.environ['TWITTER_CSM_KEY'],
                  os.environ['TWITTER_CSM_SEC'],
                  os.environ['TWITTER_ACS_KEY'],
                  os.environ['TWITTER_ACS_SEC'])

    params = {"track": "ハロウィン"}

    stream = requests.post(
        "https://stream.twitter.com/1.1/statuses/filter.json",
        auth=auth,
        stream=True,
        params=params
    )

    file_path = "tweet.txt"
    save_file = open(file_path, 'a')
    line_num = get_line_numbers(file_path)

    try:
        for line in stream.iter_lines():
            try:
                doc = json.loads(line.decode("utf-8"))
            except json.JSONDecodeError as e:
                print('JSONDecodeError: ', e)
                continue # JSONDecodeエラーが生じた場合、無視して次へ

            line_num += 1
            print(line_num)

            tweet = format_tweet(doc["text"])
            print(tweet)
            save_file.write(tweet)

            if line_num == 9999:
                print("max text lines")
                break

            if is_max_file_size(file_path):
                print("break")
                break

    except KeyboardInterrupt:
        save_file.close()
        sys.exit()

    save_file.close()


if __name__ == '__main__':
    main()

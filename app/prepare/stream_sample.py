"""
学習データセット用のテキストをTwitter Streaming APIのstatuses/sampleから取得する
"""

import os
import sys
import json

import requests
from requests_oauthlib import OAuth1

from format import format_tweet, is_max_file_size, get_line_numbers


def main(file_name):
    """
    TwitterのStreaming APIを用いてツイートを取得し、txtファイルに保存する。

    Args:
        file_name(str): 保存先のファイル名
    """

    auth = OAuth1(os.environ['TWITTER_CSM_KEY'],
                  os.environ['TWITTER_CSM_SEC'],
                  os.environ['TWITTER_ACS_KEY'],
                  os.environ['TWITTER_ACS_SEC'])

    # GET
    stream = requests.get(
        "https://stream.twitter.com/1.1/statuses/sample.json?language=ja",
        auth=auth,
        stream=True,
    )

    file_path = file_name
    save_file = open(file_path, 'a')
    line_num = get_line_numbers(file_path)

    # ツイートの読み込み、保存処理
    try:
        for line in stream.iter_lines():
            try:
                doc = json.loads(line.decode("utf-8"))
            except json.JSONDecodeError as e:
                print('JSONDecodeError: ', e)
                continue # JSONDecodeエラーが生じた場合、無視して次へ

            line_num += 1
            print(line_num)

            tweet = format_tweet(doc["text"]) # ツイートの整形

            # 50文字以上でファイルに保存
            if len(tweet) >= 50:
                print(tweet)
                save_file.write(tweet)
            else:
                line_num -= 1

            # 行数制限のチェック
            if line_num == 9999:
                print("max text lines")
                break

            # ファイルサイズ制限のチェック
            if is_max_file_size(file_path):
                print("over 4MB")
                break

    except KeyboardInterrupt: # Ctrl + C で処理中断。ファイルクローズする。
        save_file.close()
        sys.exit()

    save_file.close()


if __name__ == '__main__':
    if len(sys.argv) == 1:
        print("保存先のファイル名を入力してください。")
        main(input())
    else:
        main(sys.argv[1])

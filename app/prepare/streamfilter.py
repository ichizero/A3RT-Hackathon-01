"""
データセットに用いるテキストをTwitter Streaming APIのstatuses/filterから取得する
"""

import sys
import os

import twitter

from format import format_tweet
from format import is_max_file_size

def main(args):
    """
    TwitterのStreaming APIを用いてツイートを取得し、txtファイルに保存する。
    """

    api = twitter.Api(consumer_key=os.environ['TWITTER_CSM_KEY'],
                      consumer_secret=os.environ['TWITTER_CSM_SEC'],
                      access_token_key=os.environ['TWITTER_ACS_KEY'],
                      access_token_secret=os.environ['TWITTER_ACS_SEC'])

    if len(args) != 2:
        print("Usage: python prep.py #tag1,#tag2")
        return 1

    track = args[1].split(',')

    file_path = "tweet.txt"
    save_file = open(file_path, 'a')

    i = 0
    try:
        for item in api.GetStreamFilter(track=track):
            if 'text' in item:
                text = format_tweet(item['text'])
                print(str(i) + " : " + text)
                save_file.write(text)
            if is_max_file_size(file_path):
                print("break")
                break
            i += 1

    except KeyboardInterrupt:
        save_file.close()
        sys.exit()

    save_file.close()


if __name__ == '__main__':
    main(sys.argv)

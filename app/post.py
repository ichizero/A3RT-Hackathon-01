"""
Twitterに投稿する
"""

import os
import sys

from requests_oauthlib import OAuth1Session


def post_tweet(tweet):
    """
    Twitterに投稿する。

    Args:
        tweet(str): 投稿文
    """

    url = "https://api.twitter.com/1.1/statuses/update.json"

    session = OAuth1Session(os.environ['TWITTER_CSM_KEY'],
                            os.environ['TWITTER_CSM_SEC'],
                            os.environ['TWITTER_ACS_KEY'],
                            os.environ['TWITTER_ACS_SEC'])

    params = {"status": tweet}

    request = session.post(url, params=params)

    if request.status_code == 200:
        print("OK, tweet posted!")
    else:
        print("Error: %d" % request.status_code)

if __name__ == '__main__':
    post_tweet(sys.argv[1])

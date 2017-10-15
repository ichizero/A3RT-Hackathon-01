"""
Twitterアカウントの「ズボラった〜」に対する認証
"""

import os

import webbrowser
import requests
from requests_oauthlib import OAuth1


def auth_account():
    """
    アカウント認証
    """

    request_url = "https://api.twitter.com/oauth/request_token"
    auth_url = "https://api.twitter.com/oauth/authenticate?oauth_token="
    access_url = "https://api.twitter.com/oauth/access_token"

    # リクエストトークンを取得
    auth = OAuth1(os.environ['TWITTER_CSM_KEY'],
                  os.environ['TWITTER_CSM_SEC'])

    req = requests.post(request_url, auth=auth)

    # jsonにデコードできなかったので、テキストから値を取得
    req_token = req.text.split("&")
    req_token[0] = req_token[0].replace("oauth_token=", "")
    req_token[1] = req_token[1].replace("oauth_token_secret=", "")

    # ブラウザでアプリの認証
    auth_url += req_token[0]
    print("ブラウザで認証してください。")
    webbrowser.open(auth_url)

    # webアプリではないため、人力で認証後のoauth_verifierの値を取得
    print("リダイレクト先URLの末尾にあるoauth_verifierの値を入力してください。")
    oauth_verifier = input()

    # アクセストークンを取得
    params = {"oauth_verifier": oauth_verifier}
    auth = OAuth1(os.environ['TWITTER_CSM_KEY'],
                  os.environ['TWITTER_CSM_SEC'],
                  req_token[0],
                  oauth_verifier)
    req = requests.post(access_url, auth=auth, params=params)

    # リクエストトークン同様、テキストから値を取得
    acs_token = req.text.split("&")
    acs_token[0] = acs_token[0].replace("oauth_token=", "")
    acs_token[1] = acs_token[1].replace("oauth_token_secret=", "")

    # アクセストークンの表示
    print("Twitter Access Token : " + acs_token[0])
    print("Twitter Access Token Secret : " + acs_token[1])


if __name__ == '__main__':
    auth_account()

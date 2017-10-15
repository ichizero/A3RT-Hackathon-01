"""
A3RT Text Suggest APIを用いて、テキストを自動生成する
"""

import os
import requests


def get_suggestion(prev_desc):
    """
    A3RT Text Suggest APIを用いて、テキストを自動生成する。

    Args:
        prev_desc: 文生成に必要なキーフレーズ

    Returns:
        Text Suggest APIで生成した文(1~3文)の配列を返す。
    """

    url = "https://api.a3rt.recruit-tech.co.jp/text_suggest/v2/predict"
    apikey = os.environ["A3RT_API_KEY"]
    style = os.environ["MODEL_ID"]
    separation = 2 # 2: センテンスを生成

    # GET parameter
    params = {
        "apikey":               apikey,     # API KEY
        "previous_description": prev_desc,  # 生成に用いる入力文
        "style":                style,      # 生成文のスタイル
        "separation":           separation  # 生成形式
    }

    # Get Json
    data = requests.get(url, params=params).json()
    if data["status"] != 0:
        return data["status"]

    return data["suggestion"]


if __name__ == '__main__':
    print(get_suggestion(input()))

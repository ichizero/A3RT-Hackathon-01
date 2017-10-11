"""
main
"""

import os
from app.suggester import Suggester
from app.post import post_tweet

def main(argv):
    """
    main
    """

    apikey = os.environ['A3RT_API_KEY']
    source_txt = argv[0]

    sugg = Suggester(apikey)
    result_array = sugg.get_suggestion(source_txt)
    print(result_array)
    result_txt = source_txt + result_array[0]
    print(result_txt)

    # 要約API

    # 画像検索API

    # Twitter投稿
    # post_tweet(result_txt)

    return 0

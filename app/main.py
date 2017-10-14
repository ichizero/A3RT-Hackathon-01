"""
main
"""

from app.suggest import get_suggestion
from app.post import post_tweet

def main(argv):
    """
    main
    """

    if len(argv) == 0:
        source_txt = "今日は"
    else:
        source_txt = argv[0]

    result_array = get_suggestion(source_txt)
    print(result_array)
    result_txt = source_txt + result_array[0]
    print(result_txt)

    # 要約API

    # 画像検索API

    # Twitter投稿
    # post_tweet(result_txt)

import os
from app.suggester import Suggester

def main(argv):
    """
    main
    """

    apikey = os.environ['A3RT_API_KEY']
    hitokoto = argv[0]

    sugg = Suggester(apikey)
    print(sugg.get_suggestion(hitokoto))

    # 要約API

    # 画像検索API

    # Twitter投稿

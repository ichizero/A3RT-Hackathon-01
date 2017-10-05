import sys
import json
import urllib
import urllib.parse
import urllib.request

class Suggester:
    """
    A3RT Text Suggest APIを用いて、テキストを自動生成するクラス
    """

    def __init__(self, apikey):
        """
            Constructor
        """
        self.url = "https://api.a3rt.recruit-tech.co.jp/text_suggest/v2/predict"
        self.apikey = apikey

    def getSuggestion(self, prev_desc):
        """
        APIから得たテキストを返します。

        Args:
            prev_desc: 文生成に必要なキーフレーズ

        Returns:
            Text Suggest APIで生成した文が戻り値となる。
        """

        # GET パラメータ
        params = {
            "apikey": self.apikey, # API KEY
            "previous_description": prev_desc, # 生成に用いる入力文
            "style": 0,       # 現代文
            "separation": 2   # センテンスを生成
        }

        # URL末尾にパラメータを追加
        self.url += "?" + urllib.parse.urlencode(params)

        res = urllib.request.urlopen(self.url)
        data = json.loads(res.read().decode('utf-8'))
        if data["status"] != 0:
            return data["status"]

        return data["suggestion"]

if __name__ == '__main__':
    sugg = Suggester(sys.argv[1])
    print(sugg.getSuggestion(input()))

# ズボラった〜

## 概要

「みんなSNSやってるよねー」

「でも毎日投稿するの面倒じゃない？」

そんな悩みを解決するのが「ズボラった〜」！

投稿したいタイミングにあったワードを2つ思いつくだけで、文章を生成してSNSへ投稿してくれる。


## 利用したAPI

| 用途 | API名 |
| ---- | ---- |
| 投稿文生成 | A3RT Text Suggest API |
| SNS投稿 | Twitter REST API |
| データセット準備 | Twitter Streaming API |

## 実行環境

言語：Python3

ライブラリ：Requests、Requests-OAuthLib

(./app/auth/auth.pyにてwebbrowserを利用)

環境変数

| 変数名 | 説明 |
| ---- | ---- |
| A3RT\_API\_KEY | A3RT Text Suggest APIのAPIキー|
| MODEL\_ID | 文章生成モデルのID |
| TWITTER\_CSM\_KEY | Twitter Consumer Key |
| TWITTER\_CSM\_SEC | Twitter Consumer Secret |
| TWITTER\_ACS\_KEY | Twitter Access Token Key |
| TWITTER\_ACS\_SEC | Twitter Access Token Secret |

## 実行方法

### 1. 環境変数の設定

事前に上記の環境変数を設定しておく。

自身のTwitterアカウントを用いる場合、「./app/auth/auth.py」を実行し、アクセストークンキー・シークレットを取得する。

### 2. アプリの実行

リポジトリのルートディレクトリに配置された、index.pyに引数を2ワード与えて実行する。

CodeCheck上ではデバッグ画面で実行する。

```
python index.py 引数1 引数2
```

生成結果はCLI上に表示される他、Twitterにて確認することができる。

CodeCheckに設定したAccess Tokenでは、[@ichizero_01](https://twitter.com/ichizero_01)アカウントへ投稿される。

## ファイル構成

| ファイル名 | 機能 |
| ---- | ---- |
| ./ | |
| ./index.py | アプリケーションの起動 |
| ./requirements.txt | 依存パッケージ管理 |
| ./app/ | |
| ./app/main.py | アプリケーションのメイン |
| ./app/post.py | Twitterへの投稿 |
| ./app/suggest.py | 投稿文生成 |
| ./app/auth | |
| ./app/auth/auth.py | Twitterのアプリ認証 |
| ./app/prepare/ | |
| ./app/prepare/format.py | データセット用ツイートの整形 |
| ./app/prepare/save.py | データセット用ツイートの保存 |
| ./app/prepare/stream_filter.py | データセット用ツイート取得(statuses/filter) |
| ./app/prepare/stream_sample.py | データセット用ツイート取得(statuses/sample) |



## 工夫

文章生成モデルの学習データセットに、Twitterから取得したツイートを用いた。

しかし、ツイートにはタグやアカウントIDなどのノイズが多数含まれていたため、学習後の生成文が文としての形を成していなかった。

そのため、取得ツイートをフィルタリングすることで、どうにか文章のようなものを生成することができた。

## 問題

### 1. 自分のTwitterへしか投稿できない

Access TokenにTwitterアプリケーション登録時に生成したキーを利用したため、自身の鍵アカウントでしか投稿できなかった。

急遽、Access Tokenを取得するコードを追加。

### 2. 文章の生成精度

データセットを作成する際にフィルタリングは行ったものの、なかなか文章の生成精度が上がらなかった。

短文ツイート、単語の羅列、ボットによる投稿などが影響しているものと思われる。

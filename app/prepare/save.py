"""
ツイートをファイルに保存する。
"""

import sys
import json

from format import format_tweet, get_line_numbers, is_max_file_size


def save_tweet(stream, file_path):
    """
    ツイートをファイルに保存する。

    Args:
        stream: Twitter Stream
        file_path(str): 保存先のファイル名
    """
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
        print("中断します。")
        save_file.close()
        sys.exit()

    save_file.close()

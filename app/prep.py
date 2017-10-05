import sys
import twitter

def main(args):
    """
    TwitterのStreaming APIを用いてツイートを取得し、txtファイルに保存します。
    """

    if len(args) != 6:
        print("Usage")
        print("arg1: consumer_key     | arg2: consumer_secret")
        print("arg3: access_token_key | arg4: access_token_secret")
        print("arg5: #tag1,#tag2")
        return 1

    consumer_key = args[1]
    consumer_secret = args[2]
    access_token_key = args[3]
    access_token_secret = args[4]

    track = args[5].split(',')

    api = twitter.Api(consumer_key=consumer_key,
                      consumer_secret=consumer_secret,
                      access_token_key=access_token_key,
                      access_token_secret=access_token_secret)

    save_file = open('tweet.txt', 'a')

    for item in api.GetStreamFilter(api, track=track, languages="ja"):
        if 'text' in item:
            print(item['text'])
            save_file.write(item['text'])

    save_file.close()

if __name__ == '__main__':
    main(sys.argv)

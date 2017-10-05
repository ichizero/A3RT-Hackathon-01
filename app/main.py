from app.suggester import Suggester

def main(argv):
    """
    main
    """

    apikey = argv[0]

    print("一言入力してね！")
    hitokoto = input()

    suggester = Suggester(apikey)
    print(suggester.getSuggestion(hitokoto))

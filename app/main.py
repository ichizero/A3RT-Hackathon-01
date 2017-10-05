from app.suggester import Suggester

def main(argv):
    """
    main
    """

    apikey = argv[0]
    hitokoto = argv[1]

    print(apikey)
    
    suggester = Suggester(apikey)
    print(suggester.getSuggestion(hitokoto))

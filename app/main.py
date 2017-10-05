from app.suggester import Suggester

def main(argv):
    """
    main
    """

    apikey = argv[0]
    hitokoto = argv[1]
    
    suggester = Suggester(apikey)
    print(suggester.getSuggestion(hitokoto))

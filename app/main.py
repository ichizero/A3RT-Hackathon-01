import os
from app.suggester import Suggester

def main(argv):
    """
    main
    """

    apikey = os.environ['A3RT_API_KEY']
    hitokoto = argv[0]
    
    suggester = Suggester(apikey)
    print(suggester.getSuggestion(hitokoto))

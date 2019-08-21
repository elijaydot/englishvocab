'''
This is an Interactive English Language Vocabulary
Author  : Elijah Aremu
Date    : 18/08/2019
'''

import json
from difflib import get_close_matches

#import the Vocabulary File (a .json file that contains all vocabularies and their meanings)
# A Data file of Words and Definitions
data = json.load(open("classworks\\python_mega\\interactive_dictionary\\data.json"))

def translate(word):
    return data[word]


word = input("Enter the Word: ").lower()

try:
    if word not in data.keys():
        yn = input(f"Did you mean {get_close_matches(word, data.keys())[0]} instead ? Y/N: ").lower()
        if yn == 'y':
            word = get_close_matches(word, data.keys())[0]
        elif yn == 'n':
            print("What would the entry be?")
        else:
            print("I don't understand!")
        
    # translation = data.get(word)
    translation = translate(word)
    
    #Print a readable meaning 
    if len(translation) > 1:
        print(f'\nThe word {word.upper()} have {len(translation)} meanings.\n')
    else:
        print(f'\nThe word {word.upper()} has {len(translation)} meaning.\n')

    for item in translation:
        print(item)
# KeyError: 'j hbg'
except KeyError:
    print("\nPlease check the word and try again.\n")
# TypeError: object of type 'NoneType' has no len()
# TypeError: input expected at most 1 arguments, got 3
except TypeError:
    print("pass")
# IndexError: list index out of range
except IndexError:
    print("\nThe word doesn't exist.\n")
# AttributeError: 'function' object has no attribute 'get'

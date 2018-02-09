
"""
Created on Tue Feb  6 16:47:46 2018

@author: nayan
"""
import json
from difflib import get_close_matches

dictionary = json.load(open("data.json","r")) # loading the file which contains words and their meanings.

def searchInDic(string):
    if string in dictionary: 
        return dictionary[string]
    elif string.title() in dictionary: # for proper nouns like name of places eg. Paris
        return dictionary[string.title()]
    elif string.upper() in dictionary: # for acronyms eg. USA
        return dictionary[string.upper()]
    elif len(get_close_matches(string, dictionary.keys())) > 0: # for checking typos
        print("Did you mean any of the following?")
        cntr = 1
        for item in get_close_matches(string, dictionary.keys()):
            print(cntr," - "+item)
            cntr += 1
        response = input("If yes press the number of the correct word \nElse press n: ")
        if response == 'n' or response == 'N':
            return "Word does not exist!"
        else:
            try:
                response = int(response)
                # Checking if the number entered by the user is correct
                if response >= 1 and response <= len(get_close_matches(string, dictionary.keys())):
                     return dictionary[get_close_matches(string, dictionary.keys())[response-1]]
                else:
                    return "You entered wrong option."
            except:
                return "You entered wrong input."
    else:
        return "Word doesn't exist!"

word = input("Enter your word -> ")

output = searchInDic(word.lower())

if type(output) == list: # when searchInDic finds a word and returns the meaning(s) in a list
    for op in output:
        print(op)
else:
    print(output)

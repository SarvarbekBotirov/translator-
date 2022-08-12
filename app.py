import json
from difflib import get_close_matches #this function gives us a possible similar words 

#create data variable for json 
data = json.load(open("data.json"))

#create a function which finds defintions of a word that user inputs
def translate(word):
    
    if word in data:
        return data[word]
    elif len(get_close_matches(word, data.keys(), cutoff=0.8)) > 0:
        user_answer = input("Did you mean %s instead? Enter 'Y' if yes, 'N' if no!: " % get_close_matches(word,data.keys())[0]).lower()
        if user_answer == "y":
            return data[get_close_matches(word,data.keys())[0]]
        elif user_answer == "n":
            return "The word doesn't exist"
        else:
            return "We didn't understand your entry."
    else:
        print(f"Opps, {word} doesn't exist :(")
    
#ask user to input word
user_word = input("Enter a word: ").lower()


result = translate(user_word)
if type(result) == list:
    for item in result:
        print(item)
else:
    print(result)
    

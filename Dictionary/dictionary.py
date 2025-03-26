import json
from difflib import SequenceMatcher, get_close_matches

file_path = r"Dictionary\data.json"
words = json.load(open(file_path))

def translate(word):
    if word not in words:
        word = word.lower()
    if word in words:
        return words[word]
    elif len(get_close_matches(word, words.keys())) > 0:
        inp = input("Did you mean %s? Y or N: " %get_close_matches(word, words.keys())[0])
        if inp == "Y":
            return words[get_close_matches(word, words.keys())[0]]
        elif inp == "N":
            return "The word doesn't exist. Please double check it."
        else:
            return "We didn't understand the entry"
    else:
        return "The word doesn't exist. Please double check it."


word = input("Enter word: ")
while word != "/exit":
    meaning = translate(word)
    if type(meaning) == list:
        for definition in meaning:
            print(definition)
    else:
        print(meaning)
    word = input("Enter word: ")


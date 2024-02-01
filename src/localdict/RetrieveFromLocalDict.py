import json
import sys


class RetrieveFromLocalDict:
    def __init__(self, path = None):
        if path is None:
            path = sys.path[0]
        with open(f"{path}/words_dictionary.json", "r") as file:
            self.dictionary_of_english_words = json.load(file)

    def retrieveFromLocalDict(self, word):
        return True if word in self.dictionary_of_english_words else False
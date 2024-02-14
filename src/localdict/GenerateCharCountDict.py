from multiprocessing.spawn import prepare
from operator import ge
import os, sys, json

import RetrieveFromLocalDict

class GenerateCharCountDict:
    def __init__(self, generate = False, read = False):

        if not generate and not read:
            raise ValueError("At least one of the optional arguments must be True")

        if generate:
            local_dict = RetrieveFromLocalDict.RetrieveFromLocalDict(path = f"{os.path.dirname(os.path.dirname(os.path.abspath(__file__)))}/localdict/")
            self.generateCharCountDictionaryFile(local_dict)

        if read:
            extracted_dict_from_file = self.readCharCountDictFromFile()
            self.char_count_dict = self.convertExtractedDictKeysToTuple(extracted_dict_from_file)

    def generateCharCountForWord(self, word: str) -> str:
        char_count_dict = {
            "a" : 0,
            "b" : 0,
            "c" : 0,
            "d" : 0,
            "e" : 0,
            "f" : 0,
            "g" : 0,
            "h" : 0,
            "i" : 0,
            "j" : 0,
            "k" : 0,
            "l" : 0,
            "m" : 0,
            "n" : 0,
            "o" : 0,
            "p" : 0,
            "q" : 0,
            "r" : 0,
            "s" : 0,
            "t" : 0,
            "u" : 0,
            "v" : 0,
            "w" : 0,
            "x" : 0,
            "y" : 0,
            "z" : 0,
            "-" : 0,
        }

        for char in word:
            char_count_dict[char] += 1

        alphabet_list = list(char_count_dict.keys())

        prepared_string = ""

        for letter in alphabet_list:
            if char_count_dict[letter] > 0:
                prepared_string += f"{letter}{char_count_dict[letter]} "

        return prepared_string
    
    def convertCharCountToTupleForLookup(self, char_count: str) -> tuple:
        char_count_as_list = char_count.split(" ")
        char_count_as_list.pop()
        # print(char_count_as_list)
        return tuple(char_count_as_list)



    def generateCharCountDict(self, local_dict) ->  dict:
        char_count_dict = {}
        for word in local_dict.dictionary_of_english_words:
            char_count_key = self.generateCharCountForWord(word)

            if char_count_key in char_count_dict:
                char_count_dict[char_count_key].append(word)
            else:
                char_count_dict[char_count_key] = [word]

        return char_count_dict

    
    def writeCharCountDictToFile(self, prepared_dict_for_file) -> None:
        with open(f"{os.path.dirname(os.path.dirname(os.path.abspath(__file__)))}/localdict/char_count_dictionary.json", "w") as file:
            file.truncate(0)
            json.dump(prepared_dict_for_file, file)

        file.close()


    def generateCharCountDictionaryFile(self, local_dict) -> None:
        char_count_dict = self.generateCharCountDict(local_dict)
        self.writeCharCountDictToFile(char_count_dict)


    def readCharCountDictFromFile(self) -> dict:
        with open(f"{os.path.dirname(os.path.dirname(os.path.abspath(__file__)))}/localdict/char_count_dictionary.json", "r") as file:
            extracted_dict_from_file = json.load(file)
        
        file.close()
        return extracted_dict_from_file


    def convertExtractedDictKeysToTuple(self, extracted_dict_from_file: dict) -> dict:
        converted_dict = {}
        for key, value in extracted_dict_from_file.items():
            key_tuple = tuple(key.split())
            converted_dict[key_tuple] = value
        
        return converted_dict

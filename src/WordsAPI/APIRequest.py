import requests, os, sys, hashlib, time
sys.path.append(f"{os.path.dirname(os.path.dirname(os.path.abspath(__file__)))}/anagramsolver/")
from AnagramSolverHelperFunctions import countLetterFrequencyInAnagram

url = "https://wordsapiv1.p.rapidapi.com/words/"

headers = {
    "X-RapidAPI-Key": "3fb0ee51c2msh6073d409167c633p134312jsnb691f10594bf",
	"X-RapidAPI-Host": "wordsapiv1.p.rapidapi.com"
}

query_string = {
    "letterPattern" : "",
    "limit" : "100",
    "page" : "1"
}

def makeRequest(pattern: str, anagram:str = None):
    query_string["letterPattern"] = pattern

    response = requests.get(url, headers=headers, params=query_string)

    return response.json()


def trimNonMatchingResponses(anagram: str, data_set: list):
    anagram_list = list(anagram)
    valid_responses = []

    anagram_char_count = countLetterFrequencyInAnagram(anagram_list)

    for word in data_set:

        if set(list(word)) != set(anagram_list):
            continue
        word_char_count = countLetterFrequencyInAnagram(list(word))

        if word_char_count == anagram_char_count:
            valid_responses.append(word)

    return valid_responses


print(hashlib.sha256(f"{time.time()}hello".encode()).hexdigest())
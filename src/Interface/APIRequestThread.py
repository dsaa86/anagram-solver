from threading import Thread
import os, sys
sys.path.append(f"{os.path.dirname(os.path.dirname(os.path.abspath(__file__)))}/WordsAPI/")
sys.path.append(f"{os.path.dirname(os.path.dirname(os.path.abspath(__file__)))}/RegEx/")
from APIRequest import makeRequest, trimNonMatchingResponses
from regex import sanitiseAnagramString, prepareLettersOnlyForMatching

class APIRequestThread(Thread):
    def __init__(self, anagram):
        Thread.__init__(self)
        self.sanitised_anagram = sanitiseAnagramString(anagram)
        print(self.sanitised_anagram)
        anagram_list = [char for char in self.sanitised_anagram]
        print(anagram_list)
        self.prepared_pattern = prepareLettersOnlyForMatching(anagram_list)
        print(self.prepared_pattern)
        

    def run(self):
        api_results = makeRequest(self.prepared_pattern)
        trimmed_api_results = trimNonMatchingResponses(self.sanitised_anagram, api_results["results"]["data"])

        self.results = {
            "type" : "api",
            "results" : trimmed_api_results
        }

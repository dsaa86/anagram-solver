from threading import Thread
import os, sys, time
sys.path.append(f"{os.path.dirname(os.path.dirname(os.path.abspath(__file__)))}/localdict/")
from GenerateCharCountDict import GenerateCharCountDict

class HashmapLookupThread(Thread):
    def __init__(self, anagram):
        Thread.__init__(self)
        self.char_count_dict = GenerateCharCountDict(read = True)
        self.anagram = anagram
        self.results = []

    def run(self):
        start_time = time.time()
        word_map = self.char_count_dict.generateCharCountForWord(self.anagram)
        word_map_tuple = self.char_count_dict.convertCharCountToTupleForLookup(word_map)
        run_time = time.time() - start_time
        try:
            self.results = {
                "type" : "hashmap",
                "algorithm" : "Hashmap Lookup",
                "results" : {
                    "input" : self.anagram,
                    "type" : "Hashmap Lookup",
                    "input_len": len(self.anagram),
                    "permutations": "No Permutations Generated",
                    "perm_count": 0,
                    "results" : self.char_count_dict.char_count_dict[word_map_tuple],
                    "run_time" : run_time
                }
            }
        except KeyError:
            self.results = {
                "type" : "hashmap",
                "results" : "No Results Found",
            }
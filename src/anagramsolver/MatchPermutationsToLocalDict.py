import os, sys
sys.path.append(f"{os.path.dirname(os.path.dirname(os.path.abspath(__file__)))}/permutations/")
sys.path.append(f"{os.path.dirname(os.path.dirname(os.path.abspath(__file__)))}/localdict/")

from RetrieveFromLocalDict import RetrieveFromLocalDict

class MatchPermutationsToLocalDict:
    def __init__(self, permutations: list, localDict = None):
        if localDict is None:
            localDict = RetrieveFromLocalDict(path=f"{os.path.dirname(os.path.dirname(os.path.abspath(__file__)))}/localdict/")
        self.localDict = localDict
        self.permutations = permutations

    def matchPermutationsToLocalDict(self):
        return [word for word in self.permutations if self.localDict.retrieveFromLocalDict(word)]
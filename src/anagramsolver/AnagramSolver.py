import os
import re
import sys

sys.path.append(f"{os.path.dirname(os.path.dirname(os.path.abspath(__file__)))}/localdict/")
sys.path.append(f"{os.path.dirname(os.path.dirname(os.path.abspath(__file__)))}/permutations/")

import HeapRecursive
import RetrieveFromLocalDict
from HelperFunctions import (countIndividualLettersInAnagram,
                             getUniqueLettersInAnagram, preparePattern,
                             sanitiseAnagramString, splitAnagramToList)


class AnagramSolver:
    def __init__(self, anagram = None, local = False, remote = False, match_pattern = False):
        self.anagram = self.setAnagram(anagram)
        self.anagram_length = None if anagram is None else len(anagram)
        self.local = local
        self.remote = remote
        self.match_pattern = match_pattern
        self.permutations_list = None
        self.local_dict = RetrieveFromLocalDict.RetrieveFromLocalDict(path = f"{os.path.dirname(os.path.dirname(os.path.abspath(__file__)))}/localdict/")


    # Getters & Setters
    def getAnagram(self) -> str:
        return self.anagram
    
    def getAnagramLength(self) -> int:
        return self.anagram_length
    
    def getLocal(self) -> bool:
        return self.local
    
    def getRemote(self) -> bool:
        return self.remote
    
    def getMatchPattern(self) -> bool:
        return self.match_pattern
    
    def getPermutationsList(self) -> list:
        return self.permutations_list
    
    def setAnagram(self, anagram):

        if anagram is None:
            return None

        try:
            return sanitiseAnagramString(anagram)
        except ValueError as e:
            raise ValueError("Anagram must only contain letters (a-z, A-Z)") from e
        except TypeError as e:
            raise TypeError("Anagram must be a string") from e
            

    def setAnagramLength(self, anagram_length) -> None:
        self.anagram_length = anagram_length

    def setLocal(self, local) -> None:
        self.local = local

    def setRemote(self, remote) -> None:
        self.remote = remote

    def setMatchPattern(self, match_pattern) -> None:
        self.match_pattern = match_pattern


    def buildRegexForRemote(self) -> str:

        """
            For an algorithm of: "LOEHL" (hello),
            we're returning a regex of: "[L|O|E|H]{5}".
            Notice the lack of two "L" characters in the regex.
        """

        if self.remote != True:
            raise NotImplementedError

        anagram_unique_chars = getUniqueLettersInAnagram(self.anagram)
        anagram_unique_chars_length = countIndividualLettersInAnagram(self.anagram)
        word_constructor = "["

        for index, char in enumerate(anagram_unique_chars):

            word_constructor += char

            # We only want the logical "or" operator inserting BETWEEN chars,
            # not after the last char
            if index != anagram_unique_chars_length - 1:
                word_constructor += "|"

        word_constructor += f"]{{{self.anagram_length}}}"
        return word_constructor

    def searchRemote(self) -> None:
        return None


    def generatePermutations(self) -> list:

        if self.local != True:
            raise NotImplementedError

        if self.anagram is None:
            raise ValueError("No anagram provided")

        list_anagram = splitAnagramToList(self.anagram)
        self.permutations_list = HeapRecursive.heapRecursive(list_anagram)

        return self.permutations_list


    def searchLocalNoPattern(self, permutations_list = None, force_custom_permutations = False) -> list:

        if self.local != True:
            raise NotImplementedError

        if self.permutations_list is None and permutations_list is None:
            raise ValueError("No permutations list provided")
        
        if self.permutations_list is None and permutations_list is None:
            raise ValueError("No permutations list provided")
        elif self.permutations_list is None or force_custom_permutations:
            self.permutations_list = permutations_list

        valid_permutations_list = []

        for permutation in self.permutations_list:
            if self.local_dict.retrieveFromLocalDict(permutation):
                valid_permutations_list.append(permutation)

        return valid_permutations_list
    
    def searchLocalWithPattern(self, permutations_list = None, force_custom_permutations = False, pattern: str = None) -> list:

        if pattern is None:
            raise ValueError("No pattern provided")
        
        if len(pattern) != self.anagram_length:
            raise ValueError("Pattern length must match anagram length")
        
        try:
            sanitiseAnagramString(pattern, r"[^a-z-_]+", "Pattern match can only contain letters (a-z, A-Z), hyphens (-), and underscores (_)")
        except TypeError as e:
            raise TypeError("Pattern must be a string") from e
        except ValueError as e:
            raise ValueError("Pattern match can only contain letters (a-z, A-Z), hyphens (-), and underscores (_)") from e

        try:
            valid_permutations_list = self.searchLocalNoPattern(permutations_list = permutations_list, force_custom_permutations = force_custom_permutations)
        except NotImplementedError as e:
            raise NotImplementedError("Local search with pattern matching not implemented") from e
        except ValueError as e:
            raise ValueError("No permutations list provided") from e
        
        prepared_pattern = preparePattern(pattern)

        print(prepared_pattern)

        pattern_matches = []

        for permutation in valid_permutations_list:
            if re.match(prepared_pattern, permutation):
                pattern_matches.append(permutation)

        return pattern_matches

from math import factorial

length = len("getbargee")

print(factorial(length) / factorial((length - length)))


solver = AnagramSolver(anagram="getbargee", local = True)
solver.generatePermutations()
print(solver.searchLocalWithPattern(pattern="-g-----e-"))
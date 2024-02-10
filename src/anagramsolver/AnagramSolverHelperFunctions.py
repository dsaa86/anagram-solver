import re
from multiprocessing.spawn import prepare

def countIndividualLettersInAnagram(anagram: str) -> int:
    """
        To account for duplicate chars when building
        a regex, we need to know the number of UNIQUE
        chars in an anagram.

        e.g. "HELLO" would return 4.
        e.g. "AARDVARK" would return 5.
    """
    if type(anagram) != str:
        raise TypeError("Anagram must be a string")
    return len(set(anagram))


def getUniqueLettersInAnagram(anagram) -> list:
    return list(set(anagram))

def splitAnagramToList(anagram) -> list:
    return list(anagram)

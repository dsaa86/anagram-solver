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

    char_count_tracker = {}

    for char in anagram:
        if char in char_count_tracker:
            char_count_tracker[char] += 1
        else:
            char_count_tracker[char] = 1

    return len(char_count_tracker)

def getUniqueLettersInAnagram(anagram) -> list:
    duplicate_char_tracker = []

    for char in anagram:
        if char in duplicate_char_tracker:
            continue
        duplicate_char_tracker.append(char)

    return duplicate_char_tracker

def splitAnagramToList(anagram) -> list:
    return [char for char in anagram]


def sanitiseAnagramString(anagram: str, pattern: str = r"[^a-z]+", err_msg: str = "Anagram must only contain letters (a-z, A-Z)") -> str:
    if type(anagram) != str:
        raise TypeError("Anagram must be a string")
    
    anagram = anagram.lower()

    regex_search = re.findall(pattern, anagram)
    if regex_search:
        raise ValueError("Anagram must only contain letters (a-z, A-Z)")

    return anagram


def preparePattern(pattern:str) -> str:
    
    if type(pattern) != str:
        raise TypeError("Pattern must be a string")
    
    prepared_pattern = r"^"
    
    for char in pattern:
        if char == "_" or char == "-":
            prepared_pattern += r"[a-z]"
        else:
            prepared_pattern += char

    prepared_pattern += r"$"

    return prepared_pattern
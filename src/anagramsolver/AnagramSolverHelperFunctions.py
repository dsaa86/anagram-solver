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

def countLetterFrequencyInAnagram(anagram) -> dict:
    if type(anagram) != list:
        anagram = list(anagram)

    frequency_count = {}

    for char in anagram:
        if char not in frequency_count:
            frequency_count[char] = 1
        else:
            frequency_count[char] += 1

    return frequency_count
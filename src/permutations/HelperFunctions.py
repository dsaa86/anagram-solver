from math import factorial
import re


def calculatePermutations(anagram: str) -> int:
    length = len(anagram)

    if length == 1:
        return 1
    
    permutations = factorial(length) / factorial((length - length))
    return permutations

def checkInputListCharValidity(input_list:list) -> bool:
    char_only = False
    digit_only = False
    spec_char_presence = False

    for x in input_list:
        x = str(x)
        if re.search(r'[^a-z]', x) is None:
            char_only = True
        elif re.search(r'[^0-9]', x) is None:
            digit_only = True
        elif re.search(r'[^a-z0-9]', x) is not None:
            spec_char_presence = True

    return char_only, digit_only, spec_char_presence
from math import factorial


def calculatePermutations(anagram: str) -> int:
    length = len(anagram)

    if length == 1:
        return 1
    
    permutations = factorial(length) / factorial((length - length))
    return permutations
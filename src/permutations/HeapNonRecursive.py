from CalculatedPermutationsException import CalculatedPermutationsException, ExceededPermittedPermutationCountException

from HelperFunctions import checkInputListCharValidity


mapped_char_to_int = {
    "a" : 0,
    "b" : 1,
    "c" : 2,
    "d" : 3,
    "e" : 4,
    "f" : 5,
    "g" : 6,
    "h" : 7,
    "i" : 8,
    "j" : 9,
    "k" : 10,
    "l" : 11,
    "m" : 12,
    "n" : 13,
    "o" : 14,
    "p" : 15,
    "q" : 16,
    "r" : 17,
    "s" : 18,
    "t" : 19,
    "u" : 20,
    "v" : 21,
    "w" : 22,
    "x" : 23,
    "y" : 24,
    "z" : 25
}

mapped_int_to_char = {
    0 : "a",
    1 : "b",
    2 : "c",
    3 : "d",
    4 : "e",
    5 : "f",
    6 : "g",
    7 : "h",
    8 : "i",
    9 : "j",
    10 : "k",
    11 : "l",
    12 : "m",
    13 : "n",
    14 : "o",
    15 : "p",
    16 : "q",
    17 : "r",
    18 : "s",
    19 : "t",
    20 : "u",
    21 : "v",
    22 : "w",
    23 : "x",
    24 : "y",
    25 : "z"
}

def mapCharToInt(char: str) -> int:
    return mapped_char_to_int[char]

def mapIntToChar(int: int) -> str:
    return mapped_int_to_char[int]

def swap(input_list: list, index1: int, index2: int):
    temp = input_list[index1]
    input_list[index1] = input_list[index2]
    input_list[index2] = temp

    return input_list


def heapNonRecursive(input_list: list, output_list: list = None, perm_size : int = None, threaded: bool = False):
    if not input_list:
        raise CalculatedPermutationsException("Empty input list")
    
    if len(input_list) > 7 and not threaded:
        raise ExceededPermittedPermutationCountException()
    
    char_only, digit_only, spec_char_presence = checkInputListCharValidity(input_list)

    if spec_char_presence:
        raise ValueError("Special characters not permitted in input list")
    
    if char_only and digit_only:
        raise ValueError("Input list can only contain one data type: char OR int, not both")
    
    if perm_size is None:
        perm_size = len(input_list)

    if perm_size == 1:
        output_list.append(input_list.copy())
        return output_list
    
    if output_list is None:
        output_list = []
    
    int_mapped_input_list = input_list if digit_only else [mapCharToInt(char) for char in input_list]

    check_list = [0] * perm_size
    iterator_count = 1

    while iterator_count < perm_size:
        if check_list[iterator_count] < iterator_count:
            if iterator_count % 2 == 0:
                int_mapped_input_list = swap(int_mapped_input_list, 0, iterator_count)

            else:
                int_mapped_input_list = swap(int_mapped_input_list, check_list[iterator_count], iterator_count)

            output_list.append(int_mapped_input_list.copy())
            check_list[iterator_count] += 1
            iterator_count = 1
        else:
            check_list[iterator_count] = 0
            iterator_count += 1

    if char_only:
        for index, elem in enumerate(output_list):
            output_list[index] = "".join([mapIntToChar(int) for int in elem])
        output_list.append("".join(input_list))
    else:
        output_list.append(int_mapped_input_list)

    return output_list

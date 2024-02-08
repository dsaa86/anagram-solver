from GeneratePermutationsBaseClass import GeneratePermutationsBaseClass

class GeneratePermutationsHeapNonRecursive(GeneratePermutationsBaseClass):

    def __init__(self, input_list: list, output_list = None, perm_size : int = None, *args, **kwargs):
        super().__init__(input_list, output_list, perm_size, *args, **kwargs)
        self.mapped_char_to_int = {
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

        self.mapped_int_to_char = {
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
        
        if self.char_only:
            self.output_list = ["".join(self.input_list)]
        else:
            self.output_list = [self.input_list.copy()]

    def performPermutationGeneration(self):
        return self.heapNonRecursive(self.input_list)


    def mapCharToInt(self, char: str) -> int:
        return self.mapped_char_to_int[char]

    def mapIntToChar(self, int: int) -> str:
        return self.mapped_int_to_char[int]

    def swap(self, input_list: list, index1: int, index2: int):
        temp = input_list[index1]
        input_list[index1] = input_list[index2]
        input_list[index2] = temp

        return input_list


    def heapNonRecursive(self, input_list):

        if self.perm_size == 1:
            return self.output_list
        
        int_mapped_input_list = input_list if self.digit_only else [self.mapCharToInt(char) for char in input_list]

        check_list = [0] * self.perm_size
        iterator_count = 1

        while iterator_count < self.perm_size:
            if check_list[iterator_count] < iterator_count:
                if iterator_count % 2 == 0:
                    int_mapped_input_list = self.swap(int_mapped_input_list, 0, iterator_count)

                else:
                    int_mapped_input_list = self.swap(int_mapped_input_list, check_list[iterator_count], iterator_count)

                self.output_list.append(int_mapped_input_list.copy())
                check_list[iterator_count] += 1
                iterator_count = 1
            else:
                check_list[iterator_count] = 0
                iterator_count += 1

        if self.char_only:
            for index, elem in enumerate(self.output_list):
                int_only_list = all(type(int_value) == int for int_value in elem)
                if int_only_list:
                    self.output_list[index] = "".join([self.mapIntToChar(int_value) for int_value in elem])


        return self.output_list


input_list = [1, 2, 3]

heap_non_recursive_permutations = GeneratePermutationsHeapNonRecursive(input_list)
result = heap_non_recursive_permutations.performPermutationGeneration()
print(result)
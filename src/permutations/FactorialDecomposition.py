from math import floor, factorial
import time
from GeneratePermutationsBaseClass import GeneratePermutationsBaseClass

class GeneratePermutationsFactorialDecomposition(GeneratePermutationsBaseClass):
    def __init__(self, input_list: list, output_list = None, perm_size : int = None, threaded: bool = False, index_range = None, max_perm_size: int = 11, *args, **kwargs):
        super().__init__(input_list, output_list, perm_size, max_perm_size=max_perm_size, *args, **kwargs)
        self.threaded = threaded

        if self.threaded:
            self.start_index = index_range[0]
            self.end_index = index_range[1]

    def performPermutationGeneration(self):

        if self.perm_size == 1:
            return self.output_list
        
        total_permutation_count = factorial(self.perm_size)

        if self.threaded:
            total_permutation_count = self.end_index - self.start_index
            for i in range(self.start_index, self.end_index):
                self.output_list.append(self.factorialDecomposition(self.input_list.copy(), self.perm_size, i))
        else:
            for i in range(total_permutation_count):
                self.output_list.append(self.factorialDecomposition(self.input_list.copy(), self.perm_size, i))
        
        return self.processResult(self.output_list)
        
    def factorialDecomposition(self, input_list, perm_size, index = 0):

        permutation = []

        while perm_size > 0:
            perm_size_fact = factorial(perm_size - 1)
            position = int(index / perm_size_fact)

            permutation.append(input_list[position])
            del input_list[position]
            index = floor(index % perm_size_fact)
            perm_size -= 1

        return permutation
    

    def processResult(self, output_list) -> list:
        if self.char_only:
            return ["".join(x) for x in output_list]
        elif self.digit_only:
            return [[int(x) for x in y] for y in output_list]
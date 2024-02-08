from threading import Thread
from itertools import permutations
from unittest import result
# from HeapRecursive import heapRecursive
# from HeapNonRecursive import heapNonRecursive
from FactorialDecomposition import GeneratePermutationsFactorialDecomposition


class ThreadedPermutations(Thread):
    def __init__(self, data_set: list, prefix: str, char_only: bool, digit_only: bool):
        Thread.__init__(self)
        self.char_only = char_only
        self.digit_only = digit_only
        self.data_set = data_set
        self.prefix = prefix
        self.result = []

    def generateResultToAppendFromList(self, perm_list: list):
        if self.char_only:
            return "".join(perm_list)
        elif self.digit_only:
            return [int(x) for x in perm_list]

    def construct_results(self, permutations_list, prefix_used: bool = True):
        result_builder = []
        for permutation in permutations_list:
            perm_list = list(permutation)
            if prefix_used:
                perm_list.insert(0, self.prefix)
            result_builder.append(self.generateResultToAppendFromList(perm_list))

        return result_builder
    

class StandardPermutationsThread(ThreadedPermutations):
    def __init__(self, data_set: list, prefix: str, char_only: bool, digit_only: bool):
        ThreadedPermutations.__init__(self, data_set, prefix, char_only, digit_only)

    def run(self):
        permutations_list = list(permutations(self.data_set))
        self.result = self.construct_results(permutations_list)


class HeapRecursivePermutationsThread(ThreadedPermutations):
    def __init__(self, data_set: list, prefix: str, char_only: bool, digit_only: bool):
        ThreadedPermutations.__init__(self, data_set, prefix, char_only, digit_only)

    def run(self):
        permutations_list = heapRecursive(self.data_set, threaded = True)
        self.result = self.construct_results(permutations_list)


class HeapNonRecursivePermutationsThread(ThreadedPermutations):
    def __init__(self, data_set: list, prefix: str, char_only: bool, digit_only: bool):
        ThreadedPermutations.__init__(self, data_set, prefix, char_only, digit_only)

    def run(self):
        permutations_list = heapNonRecursive(self.data_set, threaded = True)
        self.result = self.construct_results(permutations_list)

class FactorialDecompositionPermutationsThread(ThreadedPermutations):
    def __init__(self, data_set: list, char_only: bool, digit_only: bool, index_range: tuple):
        ThreadedPermutations.__init__(self, data_set, None, char_only, digit_only)
        self.index_range = index_range

    def run(self):
        generator = GeneratePermutationsFactorialDecomposition(self.data_set, threaded = True, index_range = self.index_range)
        self.result = generator.performPermutationGeneration()
        self.result = self.construct_results(self.result, False)
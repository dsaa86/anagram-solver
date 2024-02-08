from threading import Thread
from itertools import permutations
from unittest import result
from HeapRecursive import heapRecursive
from HeapNonRecursive import heapNonRecursive


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

    def construct_results(self, permutations_list):
        result_builder = []
        for permutation in permutations_list:
            perm_list = list(permutation)
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
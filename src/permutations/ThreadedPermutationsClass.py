from threading import Thread
from itertools import permutations
from HeapRecursive import heapRecursive


class ThreadedPermutations(Thread):
    def __init__(self, data_set: list, prefix: str):
        Thread.__init__(self)
        self.data_set = data_set
        self.prefix = prefix
        self.result = []

class ThreadedStandardPermutations(ThreadedPermutations):
    def __init__(self, data_set: list, prefix: str):
        ThreadedPermutations.__init__(self, data_set, prefix)

    def run(self):
        permutations_list = list(permutations(self.data_set))
        
        for permutation in permutations_list:
            perm_list = list(permutation)
            perm_list.insert(0, self.prefix)
            self.result.append("".join(perm_list))


class ThreadedHeapRecursivePermutations(ThreadedPermutations):
    def __init__(self, data_set: list, prefix: str):
        ThreadedPermutations.__init__(self, data_set, prefix)

    def run(self):
        permutations_list = heapRecursive(self.data_set, threaded = True)
        
        for index, permutation in enumerate(permutations_list):
            permutations_list[index] = self.prefix + permutation
            
        print(permutations_list)

        self.result = permutations_list
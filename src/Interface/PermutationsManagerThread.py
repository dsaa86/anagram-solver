from threading import Thread
import os, sys
sys.path.append(f"{os.path.dirname(os.path.dirname(os.path.abspath(__file__)))}/permutations/")
from PermutationsManager import PermutationsManager

class PermutationsManagerThread(Thread):
    def __init__(self, anagram, algorithm):
        Thread.__init__(self)
        self.anagram = anagram
        self.algorithm = algorithm
        self.permutations_manager = PermutationsManager()
        self.results = []

    def run(self):

        algorithm_map = ["Factorial Decomposition", "Heap's Non-Recursive", "Heap's Recursive", "Standard Permutations", "Threaded Factorial Decomposition", "Threaded Heap's Non-Recursive", "Threaded Heap's Recursive", "Threaded Standard Permutations"]

        self.results = {
            "type" : "permutations",
            "algorithm" : algorithm_map[self.algorithm],
            "results" : "No Results Found"
        }


        if self.algorithm == 0:
            self.results['results'] = self.permutations_manager.factorialDecomposition(self.anagram)
        elif self.algorithm == 1:
            self.results['results'] = self.permutations_manager.heapNonRecursive(self.anagram)
        elif self.algorithm == 2:
            self.results['results'] = self.permutations_manager.heapRecursive(self.anagram)
        elif self.algorithm == 3:
            self.results['results'] = self.permutations_manager.standardPermutations(self.anagram)
        elif self.algorithm == 4:
            self.results['results'] = self.permutations_manager.threadedFactorialDecomposition(self.anagram, max_perm_size = 12)
        elif self.algorithm == 5:
            self.results['results'] = self.permutations_manager.threadedHeapNonRecursive(self.anagram, max_perm_size = 12)
        elif self.algorithm == 6:
            self.results['results'] = self.permutations_manager.threadedHeapRecursive(self.anagram, max_perm_size = 12)
        elif self.algorithm == 7:
            self.results['results'] = self.permutations_manager.threadedStandardPermutations(self.anagram, max_perm_size = 12)
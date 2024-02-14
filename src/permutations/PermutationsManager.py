import time
from FactorialDecomposition import GeneratePermutationsFactorialDecomposition
from HeapNonRecursive import GeneratePermutationsHeapNonRecursive
from HeapRecursive import GeneratePermutationsHeapRecursive
from StandardPermutations import GeneratePermutationsStandard
from ThreadedFactorialDecomposition import PermutationsThreadedFactorialDecompositionClass
from ThreadedHeapNonRecursivePermutations import PermutationsThreadedHeapNonRecursiveClass
from ThreadedHeapRecursivePermutations import PermutationsThreadedHeapRecursiveClass
from ThreadedStandardPermutations import PermutationsThreadedStandardClass

class PermutationsManager:
    def __init__(self, *args, **kwargs):
        self.record = {}

    def outputRecords(self):
        return self.record

    def convertInputToList(self, anagram) -> list:
        anagram = [anagram]
        return list(anagram[0]) if type(anagram[0]) is str else list(map(int, str(anagram[0])))
    
    def buildResponse(self, data: list) -> dict:
        self.record[data[0]] = {
            "type"              : data[1],
            "input"             : data[2],
            "input_length"      : len(data[2]),
            "permutations"      : data[3],
            "permutation_count" : len(data[3]),
            "run_time"          : data[4]
            }
        
        return self.record[data[0]]
    

    def sanitiseAnagramInput(self, anagram, max_perm_size):

        if type(anagram) not in [list, str, int]:
            raise TypeError("Input is not of type str, int, or list")

        if len(anagram) > max_perm_size+1:
            raise ValueError(f"Anagram must be no longer than {max_perm_size} characters")

        if type(anagram) is not list:
            anagram = [anagram]
            return list (anagram[0]) if type(anagram[0]) is str else list(map(int, str(anagram[0])))

        return anagram

    def factorialDecomposition(self, anagram, max_perm_size = 7):

        try:
            anagram = self.sanitiseAnagramInput(anagram, max_perm_size)
        except TypeError as e:
            raise TypeError("Anagram is not of type str or int") from e
        except ValueError as e:
            raise ValueError(f"Anagram must be no longer than {max_perm_size} characters") from e

        generator = GeneratePermutationsFactorialDecomposition(anagram, max_perm_size = max_perm_size)
        start_time = time.time()
        results = generator.performPermutationGeneration()
        run_time = time.time() - start_time
        
        return self.buildResponse([start_time, "Factorial Decomposition", anagram, results, run_time])
        

    def heapNonRecursive(self, anagram, max_perm_size = 7):

        try:
            anagram = self.sanitiseAnagramInput(anagram, max_perm_size)
        except TypeError as e:
            raise TypeError("Anagram is not of type str, int, or list") from e
        except ValueError as e:
            raise ValueError(f"Anagram must be no longer than {max_perm_size} characters") from e

        generator = GeneratePermutationsHeapNonRecursive(anagram, max_perm_size = max_perm_size)
        start_time = time.time()
        results = generator.performPermutationGeneration()
        run_time = time.time() - start_time
        
        return self.buildResponse([start_time, "Heap's Non-Recursive", anagram, results, run_time])


    def heapRecursive(self, anagram, max_perm_size = 7):
        try:
            anagram = self.sanitiseAnagramInput(anagram, max_perm_size)
        except TypeError as e:
            raise TypeError("Anagram is not of type str, int, or list") from e
        except ValueError as e:
            raise ValueError(f"Anagram must be no longer than {max_perm_size} characters") from e

        generator = GeneratePermutationsHeapRecursive(anagram, max_perm_size = max_perm_size)
        start_time = time.time()
        results = generator.performPermutationGeneration()
        run_time = time.time() - start_time
        
        return self.buildResponse([start_time, "Heap's Recursive", anagram, results, run_time])


    def standardPermutations(self, anagram, max_perm_size = 7):
        try:
            anagram = self.sanitiseAnagramInput(anagram, max_perm_size)
        except TypeError as e:
            raise TypeError("Anagram is not of type str, int, or list") from e
        except ValueError as e:
            raise ValueError(f"Anagram must be no longer than {max_perm_size} characters") from e

        generator = GeneratePermutationsStandard(anagram, max_perm_size = max_perm_size)
        start_time = time.time()
        results = generator.performPermutationGeneration()
        run_time = time.time() - start_time
        
        return self.buildResponse([start_time, "Standard", anagram, results, run_time])


    def threadedFactorialDecomposition(self, anagram, max_perm_size = 11):
        try:
            anagram = self.sanitiseAnagramInput(anagram, max_perm_size)
        except TypeError as e:
            raise TypeError("Anagram is not of type str, int, or list") from e
        except ValueError as e:
            raise ValueError(f"Anagram must be no longer than {max_perm_size} characters") from e

        generator = PermutationsThreadedFactorialDecompositionClass(anagram)
        start_time = time.time()
        results = generator.performPermutationGeneration()
        run_time = time.time() - start_time
        
        return self.buildResponse([start_time, "Threaded Factorial Decomposition", anagram, results, run_time])


    def threadedHeapNonRecursive(self, anagram, max_perm_size = 11):
        try:
            anagram = self.sanitiseAnagramInput(anagram, max_perm_size)
        except TypeError as e:
            raise TypeError("Anagram is not of type str, int, or list") from e
        except ValueError as e:
            raise ValueError(f"Anagram must be no longer than {max_perm_size} characters") from e

        generator = PermutationsThreadedHeapNonRecursiveClass(anagram)
        start_time = time.time()
        results = generator.performPermutationGeneration()
        run_time = time.time() - start_time
        
        return self.buildResponse([start_time, "Threaded Heap's Non-Recursive", anagram, results, run_time])


    def threadedHeapRecursive(self, anagram, max_perm_size = 11):
        try:
            anagram = self.sanitiseAnagramInput(anagram, max_perm_size)
        except TypeError as e:
            raise TypeError("Anagram is not of type str, int, or list") from e
        except ValueError as e:
            raise ValueError(f"Anagram must be no longer than {max_perm_size} characters") from e

        generator = PermutationsThreadedHeapRecursiveClass(anagram)
        start_time = time.time()
        results = generator.performPermutationGeneration()
        run_time = time.time() - start_time
        
        return self.buildResponse([start_time, "Threaded Heap's Recursive", anagram, results, run_time])


    def threadedStandardPermutations(self, anagram, max_perm_size = 11):
        try:
            anagram = self.sanitiseAnagramInput(anagram, max_perm_size)
        except TypeError as e:
            raise TypeError("Anagram is not of type str, int, or list") from e
        except ValueError as e:
            raise ValueError(f"Anagram must be no longer than {max_perm_size} characters") from e

        generator = PermutationsThreadedStandardClass(anagram)
        start_time = time.time()
        results = generator.performPermutationGeneration()
        run_time = time.time() - start_time
        
        return self.buildResponse([start_time, "Threaded Standard", anagram, results, run_time])

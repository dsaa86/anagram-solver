# from ThreadedPermutationsClass import HeapRecursivePermutationsThread
from PermutationsThreadedBaseClass import PermutationsThreadedBaseClass
from math import factorial
from ThreadedPermutationsClass import FactorialDecompositionPermutationsThread
import time

"""

    We generate permutations using a threaded approach.
    The algorithm used to generate permutations is Factorial Decomposition.
    This permits a faster generation of permutations at the expense
    of system resources.

    We extend the Thread class, overriding the run() function to generate
    a list of permutations for a given data set.

    The basis for generating all permutations is as follows:

    For an input list of ["r", "t", "b", "a", "n", "i", "i"] (britain), in a 
    linear solution, the complexity would be of O(n!). In this instance,
    we would need to generate 5040 permutations.

    If we could reduce this set from n=7 to n=6, we would only need to generate
    720 permutations. This is a 7x improvement.

    To achieve this, we can remove one element from the set, reducing the set to 6
    elements, and then generate permutations for the remaining 6 elements. We then
    prepend the removed element to each permutation.

    Performing this process of removing an element, generating permutations, and
    prepending the removed element to each permutation for each element in the set
    will yield all permutations for the original set.

    This lends itself to threading as each round of permutation generation is independent
    of the others. Therefore it is relatively trivial to parallelize the process.

    The result is a significant improvement in the time complexity of the algorithm.

    This is limited to an input size of no more than 11 elements due to most home computers
    maximum permissible thread counts and available system resources. The time complexity
    also increases to an unfeasible level for input sizes greater than 11.

"""

class PermutationsThreadedFactorialDecompositionClass(PermutationsThreadedBaseClass):
    def __init__(self, input_list: list, output_list = None, perm_size : int = None, *args, **kwargs):
        super().__init__(input_list, output_list, perm_size, *args, **kwargs)
        # For this single edge-case, we do not need the instantiation of data_for_threading as in the other
        # threaded permutation classes.
        # To save hassle for this one instance, it is easier to modify after the super().__init__ call.
        
        self.data_for_threading = self.prepareDataForThreadedFactorialDecomposition()

    def prepareDataForThreadedFactorialDecomposition(self):

        data_for_threading = []

        total_permutation_count = factorial(self.perm_size)
        number_of_threads = min(total_permutation_count, 10)

        total_perm_for_each_thread = total_permutation_count // number_of_threads
        remainder = total_permutation_count % number_of_threads

        for i in range(number_of_threads):
            start = i * total_perm_for_each_thread
            end = (i + 1) * total_perm_for_each_thread
            if i == number_of_threads - 1:
                end += remainder
            data_for_threading.append((start, end))

        return data_for_threading





    def performThreadedPermutationGeneration(self) -> list:
        if self.perm_size == 1:
            return self.output_list

        for data in self.data_for_threading:
            thread = FactorialDecompositionPermutationsThread(self.input_list, self.char_only, self.digit_only, index_range = data)
            self.threads.append(thread)

        for thread in self.threads:
            thread.start()

        for thread in self.threads:
            thread.join()
            self.output_list.extend(thread.result)

        return self.output_list


# data_set = [ [1, 2, 3], [1, 2, 3, 4], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5, 6, 7], [1, 2, 3, 4, 5, 6, 7, 8], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]  ]
# for elem in data_set:
#     generatorObj = PermutationsThreadedFactorialDecompositionClass(elem)
#     start_time = time.time()
#     result_list = generatorObj.performThreadedPermutationGeneration()
#     end_time = time.time()
#     perm_flag = False
#     if len(result_list) == factorial(len(elem)):
#         perm_flag = True

#     print(f"Data set of len {len(elem)} executed in {end_time - start_time} seconds. All permutations generated: {perm_flag}")
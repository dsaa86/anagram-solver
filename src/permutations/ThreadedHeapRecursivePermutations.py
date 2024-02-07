from CalculatedPermutationsException import CalculatedPermutationsException, ExceededPermittedPermutationCountException
import ThreadedHeapRecursivePermutations

"""

    We generate permutations using a threaded approach.
    The algorithm used to generate permutations is Heap's algorithm in recursive format.
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


def generatePermutationsThreaded(input_list: list, output_list = None, perm_size : int = None):
    if output_list is None:
        output_list = []

    if not input_list:
        raise CalculatedPermutationsException("Empty input list")
    
    if len(input_list) > 11:
        raise ExceededPermittedPermutationCountException("Input list too large for threaded permutations")
    
    if perm_size is None:
        perm_size = len(input_list)

    if perm_size == 1:
        output_list.append(input_list.copy())
        return output_list

    data_for_threading = []

    for index, _ in enumerate(input_list):
        list_copy = input_list.copy()
        prefix = list_copy.pop(index)
        data_for_threading.append((list_copy, prefix))

    threads = []

    for data in data_for_threading:
        thread = ThreadedHeapRecursivePermutations(data[0], data[1])
        threads.append(thread)

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()
        output_list.extend(thread.result)

    threads = []

    return output_list
from imaplib import Int2AP
from operator import indexOf

from CalculatedPermutationsException import CalculatedPermutationsException, ExceededPermittedPermutationCountException


def heapRecursive(input_list: list, output_list = None, perm_size : int = None, prefix: str = None):
    
    if output_list is None:
        output_list = []
    
    if not input_list:
        raise CalculatedPermutationsException("Empty input list")
    
    if len(input_list) > 7 and prefix is None:
        raise ExceededPermittedPermutationCountException()
    
    if perm_size is None:
        perm_size = len(input_list)

    if perm_size == 1:
        output_list.append(input_list.copy())
        return output_list
    
    heapRecursive(input_list, output_list, perm_size - 1, prefix)

    for i in range(perm_size - 1):
        if perm_size % 2 == 0:
            input_list[i], input_list[perm_size - 1] = input_list[perm_size - 1], input_list[i]
        else:
            input_list[0], input_list[perm_size - 1] = input_list[perm_size - 1], input_list[0]
        
        heapRecursive(input_list, output_list, perm_size - 1, prefix)

    for index, elem in enumerate(output_list):
        output_list[index] = "".join(elem)

    return output_list

from CalculatedPermutationsException import CalculatedPermutationsException, ExceededPermittedPermutationCountException

from HelperFunctions import checkInputListCharValidity
from GeneratePermutationsBaseClass import GeneratePermutationsBaseClass

class PermutationsThreadedBaseClass(GeneratePermutationsBaseClass):
    def __init__(self, input_list: list, output_list = None, perm_size : int = None, *args, **kwargs):
        super().__init__(input_list, output_list, perm_size, *args, **kwargs)
        
        if self.perm_size > 1:
            self.data_for_threading = self.initiateDataForThreading(self.input_list)
            self.threads = []
        

    def initiateOutputList(self, output_list):
        if output_list is None:
            output_list = []
        return output_list
    
    def initiateInputList(self, input_list):
        if not input_list:
            raise CalculatedPermutationsException("Empty input list")
        if len(input_list) > 11:
            raise ExceededPermittedPermutationCountException("Input list too large for threaded permutations")

        for index, elem in enumerate(input_list):
            if type(elem) == str:
                input_list[index] = elem.lower()

        return input_list
    
    def initiatePermSize(self, perm_size, input_list):
        if perm_size is None:
            perm_size = len(input_list)
        return perm_size
    
    def testInputValidity(self, input_list):
        char_only, digit_only, spec_char_presence = checkInputListCharValidity(input_list)

        if spec_char_presence:
            raise ValueError("Special characters not permitted in input list")
        
        if char_only and digit_only:
            raise ValueError("Input list can only contain one data type: char OR int, not both")
        
        return char_only, digit_only, spec_char_presence
    
    def initiateDataForThreading(self, input_list):
        
        data_for_threading = []

        for index, _ in enumerate(input_list):
            list_copy = input_list.copy()
            prefix = list_copy.pop(index)
            data_for_threading.append((list_copy, prefix))

        return data_for_threading

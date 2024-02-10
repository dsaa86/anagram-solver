from CalculatedPermutationsException import CalculatedPermutationsException, ExceededPermittedPermutationCountException

from HelperFunctions import checkInputListCharValidity

import copy

class GeneratePermutationsBaseClass:

    def __init__(self, input_list: list, output_list = None, perm_size : int = None, max_perm_size: int = 11, *args, **kwargs):

        self.output_list = self._initiateOutputList(output_list)
        try:
            self.input_list = self._initiateInputList(input_list, max_perm_size)
        except CalculatedPermutationsException as e:
            raise CalculatedPermutationsException("Empty input list") from e
        except ExceededPermittedPermutationCountException as e:
            raise ExceededPermittedPermutationCountException("Input list too large for threaded permutations") from e
        self.perm_size = self._initiatePermSize(perm_size, self.input_list)
        try:
            self.char_only, self.digit_only, self.spec_char_presence = self._testInputValidity(self.input_list)
        except ValueError as e:
            raise ValueError(e) from e

        if self.perm_size == 1:
            if self.char_only:
                self.output_list = self.input_list.copy()
            else:
                self.output_list.append(self.input_list.copy())



    def _initiateOutputList(self, output_list):
        if output_list is None:
            output_list = []
        return output_list

    def _initiateInputList(self, input_list, max_perm_size):
        if not input_list:
            raise CalculatedPermutationsException("Empty input list")
        if len(input_list) > max_perm_size:
            raise ExceededPermittedPermutationCountException("Input list too large for threaded permutations")

        for index, elem in enumerate(input_list):
            if type(elem) == str:
                input_list[index] = elem.lower()

        return input_list
    
    def _initiatePermSize(self, perm_size, input_list):
        if perm_size is None:
            perm_size = len(input_list)
        return perm_size
    
    def _testInputValidity(self, input_list):
        char_only, digit_only, spec_char_presence = checkInputListCharValidity(input_list)

        if spec_char_presence:
            raise ValueError("Special characters not permitted in input list")
        
        if char_only and digit_only:
            raise ValueError("Input list can only contain one data type: char OR int, not both")
        
        return char_only, digit_only, spec_char_presence
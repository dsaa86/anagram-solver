from GeneratePermutationsBaseClass import GeneratePermutationsBaseClass
from itertools import permutations

class GeneratePermutationsStandard(GeneratePermutationsBaseClass):
    def __init__(self, input_list: list, output_list = None, perm_size : int = None, *args, **kwargs):
        super().__init__(input_list, output_list, perm_size, *args, **kwargs)
        

    def performPermutationGeneration(self):

        if self.perm_size == 1:
            return self.output_list

        # we copy the input_list and output_list to avoid pass-by-reference issues
        permutated_list = list(permutations(self.input_list))

        for permutation in permutated_list:
            if self.char_only:
                self.output_list.append("".join(permutation))
            else:
                self.output_list.append([int(x) for x in permutation])

        return self.output_list

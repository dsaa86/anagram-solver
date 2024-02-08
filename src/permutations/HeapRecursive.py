from GeneratePermutationsBaseClass import GeneratePermutationsBaseClass

class GeneratePermutationsHeapRecursive(GeneratePermutationsBaseClass):
    def __init__(self, input_list: list, output_list = None, perm_size : int = None, threaded: bool = False, *args, **kwargs):
        super().__init__(input_list, output_list, perm_size, *args, **kwargs)
        self.threaded = threaded

    def performPermutationGeneration(self):

        if self.perm_size == 1:
            return self.output_list

        # we copy the input_list and output_list to avoid pass-by-reference issues
        return self.heapRecursive(self.input_list.copy(), self.output_list.copy(), self.perm_size, self.threaded)
    
    def heapRecursive(self, input_list, output_list, perm_size, threaded):

        if perm_size == 1:
            output_list.append(input_list.copy())
            return
        
        self.heapRecursive(input_list, output_list, perm_size-1, threaded)

        for i in range(perm_size - 1):
            if perm_size % 2 == 0:
                input_list[i], input_list[perm_size - 1] = input_list[perm_size - 1], input_list[i]
            else:
                input_list[0], input_list[perm_size - 1] = input_list[perm_size - 1], input_list[0]

            self.heapRecursive(input_list, output_list, perm_size-1, threaded)

        if self.char_only:
            for index, elem in enumerate(output_list):
                output_list[index] = "".join(elem)


        return output_list

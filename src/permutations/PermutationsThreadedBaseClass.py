from GeneratePermutationsBaseClass import GeneratePermutationsBaseClass

class PermutationsThreadedBaseClass(GeneratePermutationsBaseClass):
    def __init__(self, input_list: list, output_list = None, perm_size : int = None, *args, **kwargs):
        super().__init__(input_list, output_list, perm_size, *args, **kwargs)
        if self.perm_size > 1:
            self.data_for_threading = self.initiateDataForThreading(self.input_list)
            self.threads = []
    
    def initiateDataForThreading(self, input_list):
        
        data_for_threading = []

        for index, _ in enumerate(input_list):
            list_copy = input_list.copy()
            prefix = list_copy.pop(index)
            data_for_threading.append((list_copy, prefix))

        return data_for_threading
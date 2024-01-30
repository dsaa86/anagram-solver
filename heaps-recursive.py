def heapRecursive(perm_length: int, input_list: list, output_list: list):
    if perm_length == 1:
        output_list.append(input_list.copy())
    else:
        for i in range(perm_length):
            heapRecursive(perm_length - 1, input_list, output_list)
            if perm_length % 2 == 0:
                input_list[i], input_list[perm_length - 1] = input_list[perm_length - 1], input_list[i]
            else:
                input_list[0], input_list[perm_length - 1] = input_list[perm_length - 1], input_list[0]
    return output_list  # return output_list after the for loop

sample_list = [1, 2, 3]
print(heapRecursive(len(sample_list), sample_list, []))

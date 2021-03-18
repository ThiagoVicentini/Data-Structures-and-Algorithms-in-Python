def binary_search(input_array, value):
    lenght = len(input_array)
    index = lenght//2
    inf = 0
    sup = lenght
    while(sup > inf):
        if input_array[index] == value:
            return index
        elif input_array[index] > value:
            sup = index
            index = (sup + inf)//2
        else:
            inf = index + 1
            index = (sup + inf)//2
    return -1

test_list = [1,3,9,11,15,19,29]
test_val1 = 25
test_val2 = 15
print(binary_search(test_list, test_val1))
print(binary_search(test_list, test_val2))
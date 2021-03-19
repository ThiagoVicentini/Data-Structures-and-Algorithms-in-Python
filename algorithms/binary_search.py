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

def binary_search2(input_array, value):
    low = 0
    high = len(input_array) - 1
    while(low <= high):
        mid = (low + high)//2
        if input_array[mid] == value:
            return mid
        elif input_array[mid] < value:
            low = mid + 1
        else:
            high = mid - 1
    return -1

test_list = [1,3,9,11,15,19,29]

test_val1 = 25
test_val2 = 15

print(binary_search(test_list, test_val1))
print(binary_search(test_list, test_val2))

print(binary_search2(test_list, test_val1))
print(binary_search2(test_list, test_val2))
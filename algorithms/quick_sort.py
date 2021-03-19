def quick_sort(input_array, low=0, high=None):
    if high is None:
        high = len(input_array)-1
    if low < high:
        p = partition(input_array, low, high)
        quick_sort(input_array, low, p-1)
        quick_sort(input_array, p+1, high)

def partition(input_array, low, high):
    pivot = input_array[high]
    divider = low
    for i in range(low, high):
        if input_array[i] <= pivot:
            input_array[i], input_array[divider] = input_array[divider], input_array[i]
            divider += 1
    input_array[divider], input_array[high] = input_array[high], input_array[divider]
    return divider


#Test cases
test_lists = []
test_lists.append( [0, 1, 2, 3, 4, 5] )
test_lists.append( [5, 4, 3, 2, 1, 0] )
test_lists.append( [4, 3, 5, 2, 0, 1] )
test_lists.append( [3, 7, 3, 7, 3, 7] )

for test in test_lists:    
    print("Original: " + str(test))
    quick_sort(test)
    print("Ordenada: " + str(test))
    print()

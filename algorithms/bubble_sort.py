def bubble_sort(input_array):
    length = len(input_array)
    for j in range(length-1):
        for i in range(length-1): 
            if input_array[i] > input_array[i + 1]: # Troca
                temp = input_array[i]
                input_array[i] = input_array[i+1]
                input_array[i+1] = temp
    return input_array


#Test cases
test_lists = []
test_lists.append( [0, 1, 2, 3, 4, 5] )
test_lists.append( [5, 4, 3, 2, 1, 0] )
test_lists.append( [4, 3, 5, 2, 0, 1] )
test_lists.append( [3, 7, 3, 7, 3, 7] )

for test in test_lists:    
    print("Original: " + str(test))
    bubble_sort(test)
    print("Ordenada: " + str(test))
    print()

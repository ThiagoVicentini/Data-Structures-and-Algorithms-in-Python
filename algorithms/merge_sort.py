def merge_sort(input_array, low=0, high=None):
    if high is None:
        high = len(input_array)
    if high - low > 1:
        mid = (low + high)//2
        merge_sort(input_array, low, mid)
        merge_sort(input_array, mid, high)
        merge(input_array, low, mid, high)

def merge(input_array, low, mid, high):
    left = input_array[low:mid]
    right = input_array[mid:high]
    top_left, top_right = 0, 0

    for i in range(low, high):
        # Check if it hasn't get out of bound
        if top_left >= len(left):
            input_array[i] = right[top_right]
            top_right += 1
        elif top_right >= len(right):
            input_array[i] = left[top_left]
            top_left += 1
        # Choose between the two divided arrays
        elif left[top_left] < right[top_right]:
            input_array[i] = left[top_left]
            top_left += 1
        else:
            input_array[i] = right[top_right]
            top_right += 1

#Test cases
test_lists = []
test_lists.append( [0, 1, 2, 3, 4, 5] )
test_lists.append( [5, 4, 3, 2, 1, 0] )
test_lists.append( [4, 3, 5, 2, 0, 1] )
test_lists.append( [3, 7, 3, 7, 3, 7] )

for test in test_lists:    
    print("Original: " + str(test))
    merge_sort(test)
    print("Ordenada: " + str(test))
    print()

def bubble_sort(arr):
    n = len(arr)
    # Traverse through all array elements 
    for i in range(n): 
        swapped = False
        # Last i elements are already 
        # in place 
        for j in range(n- i - 1):
            # traverse the array from 0 to 
            # n-i-1. Swap if the element  
            # found is greater than the 
            # next element 
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        # IF no two elements were swapped 
        # by inner loop, then break 
        if swapped == False:
            break
    return arr

print("\t\t**BUBBLE SORT**")
for x in range(5):
    print("*"*x)

# worst case scenario. array is in descending order
arr = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1] # or generate array using range(10, 0, -1)
print(f"Worst case scenario with input arr = {arr}\nResult:\t{bubble_sort(arr)}\n")

# average case scenario.
arr = [2, 1, 4, 3, 6, 5, 8, 7, 10, 9]
print(f"Average case scenario with input arr = {arr}\nResult:\t{bubble_sort(arr)}\n")

# best case scenario. array is already sorted
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] # or generate array using range(1, 11)
print(f"Best case scenario with input arr = {arr}\nResult:\t{bubble_sort(arr)}\n")
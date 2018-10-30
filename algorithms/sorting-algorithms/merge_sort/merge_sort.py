def merge_sort(arr):
    if len(arr) == 1:
        return arr

    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    return merge(merge_sort(left), merge_sort(right))

def merge(arr_left, arr_right):
    res = []
    left_index = 0
    right_index = 0

    while(left_index < len(arr_left) and right_index < len(arr_right)):

        if arr_left[left_index] < arr_right[right_index]:
            res.append(arr_left[left_index])
            left_index += 1
        else:
            res.append(arr_right[right_index])
            right_index += 1

    return res + arr_left[left_index:] + arr_right[right_index:]

print("\t\t**MERGE SORT**")
for x in range(5):
    print("*"*x)

# worst case scenario. array is in descending order
arr = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1] # or generate array using range(10, 0, -1)
print(f"Worst case scenario with input arr = {arr}\nResult:\t{merge_sort(arr)}\n")

# average case scenario.
arr = [5, 4, 3, 2, 1, 10, 9, 8, 7, 6] 
print(f"Average case scenario with input arr = {arr}\nResult:\t{merge_sort(arr)}\n")

# best case scenario. array is already sorted
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] # or generate array using range(1, 11)
print(f"Best case scenario with input arr = {arr}\nResult:\t{merge_sort(arr)}\n")
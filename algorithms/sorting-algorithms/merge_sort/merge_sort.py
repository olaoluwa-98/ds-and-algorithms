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

# arr = [1,4,5,6,2,3, 2, 10000]
# print(merge_sort(arr))
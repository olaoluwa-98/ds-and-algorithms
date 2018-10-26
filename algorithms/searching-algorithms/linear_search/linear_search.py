def linear_search(arr, item):
    for x in arr:
        if item == x:
            return arr.index(x)
    return -1

print(linear_search(["awo", "emma"], "awo"))
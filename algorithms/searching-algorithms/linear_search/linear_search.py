def linear_search(arr, item):
    for x in arr:
        if item == x:
            return arr.index(x)
    return -1

print(linear_search(["awo", "emma"], "awo"))

print("\t\t**LINEAR SEARCH**")
for x in range(5):
    print("*"*x)

array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] # or generate array using range(1, 11)

# worst case scenario. item is in last index
print(f"Worst case scenario with input array = {array}\nResult: index {linear_search(array, array[ len(array) - 1])}\n")

# average case scenario. item is in middle index
print(f"Average case scenario with input array = {array}\nResult: index {linear_search(array, array[ len(array) //2 ])}\n")

# best case scenario. item is in first index
print(f"Best case scenario with input array = {array}\nResult: index {linear_search(array, array[0])}\n")
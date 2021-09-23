def binary_search(arr, item):
    """
        This searches by repeatedly splitting an array in two and searches each side.
    """
    first = 0
    last = len(arr) - 1
    while first<= last:
        midpoint = (first + last)//2
        if arr[midpoint] == item:
            return True
        elif item < arr[midpoint]:
            last = midpoint - 1
        else:
            first = midpoint + 1
    return False

print("\t\t**BINARY SEARCH**")
for x in range(5):
    print("*"*x)

array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] # or generate array using range(1, 11)

# worst case scenario. item is in last index
print(f"Worst case scenario with input array = {array}\nResult:\t{binary_search(array, array[ len(array) - 1 ])}\n")

# average case scenario. item is in middle index
print(f"Average case scenario with input array = {array}\nResult:\t{binary_search(array, array[ len(array) //2 ])}\n")

# best case scenario. item is in first index
print(f"Best case scenario with input array = {array}\nResult:\t{binary_search(array, array[0])}\n")
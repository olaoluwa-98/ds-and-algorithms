def binary_search(arr, item):
    """
        This searches by dividing the work
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

print(binary_search([1,2,3,4,5,6,6], 1))
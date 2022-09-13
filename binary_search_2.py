# Iterative Binary Search Function
# It returns index of x in given array arr if present,
# else returns -1

"""
Binary Search Algorithm: The basic steps to perform Binary Search are:

    Begin with the mid element of the whole array as a search key.
    If the value of the search key is equal to the item then return an index of the search key.
    Or if the value of the search key is less than the item in the middle of the interval, narrow the interval to the lower half.
    Otherwise, narrow it to the upper half.
    Repeatedly check from the second point until the value is found or the interval is empty.

Binary Search Algorithm can be implemented in the following two ways

    Iterative Method
    Recursive Method
    """
def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0

    while low <= high:

        mid = (high + low) // 2

        # If x is greater, ignore left half
        if arr[mid] < x:
            low = mid + 1

        # If x is smaller, ignore right half
        elif arr[mid] > x:
            high = mid - 1

        # means x is present at mid
        else:
            return mid

    # If we reach here, then the element was not present
    return -1


# Test array
arr = [2, 3, 4, 10, 40]
x = 10

# Function call
result = binary_search(arr, x)

if result != -1:
    print("Element is present at index", str(result))
else:
    print("Element is not present in array")
# Time Complexity: O(log n)

# Auxiliary Space: O(1)

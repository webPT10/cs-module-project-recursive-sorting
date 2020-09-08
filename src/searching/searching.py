# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):
    # check base case rule 3
    if end >= start:
        middle = (end + start) // 2

        # if Element is present at Middle itself
        if arr[middle] == target:
            return middle

        # if element is smaller than Middle, can only be present in Start subarray??
        elif arr[middle] > target:
            return binary_search(arr, target, start, middle - 1)
        
        # Else the element can only be present in End subarray?
        else:
            return binary_search(arr, target, middle + 1, end) # rule 1 & 3
    
    else:
        # Element is not present in the array
        return - 1















# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find 
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively 
# or iteratively
# def agnostic_binary_search(arr, target):
    # Your code here
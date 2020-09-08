# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(a, b):
    merged_arr = []
    a_current_index = 0
    b_current_index = 0

    while a_current_index < len(a) or b_current_index < len(b):
        if a_current_index >= len(a):
            merged_arr.append(b[b_current_index])
            b_current_index += 1

        elif b_current_index >= len(b):
            merged_arr.append(a[a_current_index])
            a_current_index += 1

        elif a[a_current_index] <= b[b_current_index]:
            merged_arr.append(a[a_current_index])
            a_current_index += 1
        
        else:
            merged_arr.append(b[b_current_index])
            b_current_index += 1

    return merged_arr


# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    # recursively call merge_sort() on LHS
    # recursively call merge_sort() on RHS
    # merge sorted pieces

    if len( arr ) > 1:
        low = 0
        high = len(arr)
        mid = (low + high) // 2
        lhs = merge_sort(arr[:mid])
        rhs = merge_sort(arr[mid:])
        return merge(lhs, rhs)
    else:
        return arr











# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
# def merge_in_place(arr, start, mid, end):
    # Your code here


# def merge_sort_in_place(arr, l, r):
    # Your code here


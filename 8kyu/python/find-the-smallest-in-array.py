def find_smallest_int(arr):
    a = arr[0]
    for nums in arr:
        if nums < a:
            a = nums
    return a

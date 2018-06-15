def find_second_largest(arr):
    if len(arr) < 2:
        return None
    largest = max(arr[0], arr[1])
    sec_largest = min(arr[0], arr[1])
    for item in arr[2:]:
        if item > largest:
            sec_largest = largest
            largest = item
        elif item <= largest and item > sec_largest:
            sec_largest = item
    return sec_largest

print(find_second_largest([1, 2, 3, 4, 5, 6, 7]))

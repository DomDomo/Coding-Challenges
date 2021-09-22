def find_even_index(arr):
    for i in range(len(arr) + 1):
        
        first = arr[:i]
        second = arr[i + 1:]

        if sum(first) == sum(second):
            return i
        
    return -1
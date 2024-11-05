def fibonacci_search(arr, x):
    n = len(arr)
    fib_m2 = 0 
    fib_m1 = 1  
    fib_m = fib_m2 + fib_m1 
    offset = -1
    while fib_m > 1:
        i = min(offset + fib_m2, n - 1)
        if arr[i] < x: fib_m, fib_m1, fib_m2, offset = fib_m1, fib_m2, fib_m - fib_m1, i
        elif arr[i] > x: fib_m, fib_m1, fib_m2 = fib_m2, fib_m1 - fib_m2, fib_m - fib_m1
        else: return i
    if fib_m1 and offset + 1 < n and arr[offset + 1] == x:
        return offset + 1
    return -1  
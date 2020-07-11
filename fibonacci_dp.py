def fibonacci_dp(n):
    arr = [0]*n
    arr[0] = 0
    arr[1] = 1
    if n ==0:
        return arr[0]
    elif n == 1:
        return arr[1]
    else:
        for i in range(2,n):
            arr[i] = arr[i-1] + arr[i-2]
        return arr[i]
print(fibonacci_dp(6))

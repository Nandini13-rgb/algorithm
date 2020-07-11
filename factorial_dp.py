def factorial_dp(n):
    arr = [0]*(n+1)
    arr[0] = 1
    for i in range(1,n+1):
        arr[i] = i *arr[i-1]
        print(arr)
    return arr[n]
print(factorial_dp(5))

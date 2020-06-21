def fibonacci(n):
    arr = [0,1]
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)
    return arr
term = int(input(print("Enter the number of terms:")))
for i in range(1,term+1):
    print(fibonacci(i))

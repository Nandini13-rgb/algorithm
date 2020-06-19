def sum(arr):
    for i in range(len(arr)-1,-1,-1):
        if arr[i] == 9:
            arr[i] = 0
            if i == 0:
                arr = [1] + arr
        else:
            arr[i] = arr[i] + 1
            return arr
    return arr
arr=[1,2,0,9]
result= sum(arr)
print(result)


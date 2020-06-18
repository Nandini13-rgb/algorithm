def sorting_array(arr):
    left = 0
    right = 0
    for i in range(len(arr)):
        if arr[i] == 0:
            left += 1
        else:
            right += 1
    for i in range(len(arr)):
        if i < left:
            arr[i] = 0
        else:
           arr[i] = 1
    print(arr)
sorting_array([1,0,1,0,1,0,0,1,1,0,1])

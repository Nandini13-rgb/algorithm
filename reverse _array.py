def reverse_array(array):
    #method 1
    arr = arr[::-1]
    print(arr)
    #method 2
    mid = len(arr)/2
    index = 0
    while index<=mid:
        arr[i],arr[len(arr)-index-1] = arr[i],arr[len(arr)-index-1]
    print(arr)
  

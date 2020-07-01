def find_index(arr,element):
    high = len(arr) - 1
    low = 0
    mid = (high + low) // 2
    while low <= high:
        if element == arr[mid]:
            if arr[mid - 1] != arr[mid]:
                print("lowest index is", mid)
                exit()
                break
            if arr[mid-1] == arr[mid]:
                count = 0
                for i in range(mid-1,-1,-1):
                    if arr[i] == arr[mid]:
                        count += 1
                print("lowest index is", mid-count)
                low = high+1
            if arr[mid + 1] != arr[mid]:
                print("highest index is", mid)
                break
            if arr[mid+1] == arr[mid]:
                count = 0
                for i in range(mid+1,len(arr)-1):
                    if arr[i] == arr[mid]:
                        count += 1
                print("highest index is", mid+count)
                low = high +1
        elif element < arr[mid]:
            high = mid - 1
            mid = (high + low) // 2
        elif element > arr[mid]:
            low = mid + 1
            mid = (high + low) // 2
find_index( [1, 2, 2, 3, 4, 4, 4, 5, 6, 6, 6, 6, 7, 8, 9],6)

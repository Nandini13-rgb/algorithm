def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr)//2
        left_arr = arr[:mid]
        right_arr = arr[mid:]
        merge_sort(left_arr)
        merge_sort(right_arr)
        i = 0
        j = 0
        k = 0
        while len(left_arr)>i and len(right_arr)>j:
            if left_arr[i] < right_arr[j]:
                arr[k] = left_arr[i]
                i += 1
                k += 1
            else:
                arr[k] = right_arr[j]
                j += 1
                k += 1
        while len(left_arr)>i:
            arr[k] = left_arr[i]
            i += 1
            k += 1
        while len(right_arr)>j:
            arr[k] = right_arr[j]
            j += 1
            k += 1
    return arr
print(merge_sort([50,10,40,2,1]))

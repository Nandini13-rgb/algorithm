def merge_arr_using_extra_space(arr1,arr2):
    i = 0
    j = 0
    arr3 = []
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            arr3.append(arr1[i])
            i += 1
        else:
            arr3.append(arr2[j])
            j += 1
    while i < len(arr1):
        arr3.append(arr1[i])
        i += 1
    while j < len(arr2):
        arr3.append(arr2[j])
        j += 1
    print(arr3)
def merge_arr(arr1,arr2):
    i = 0
    j = 0
    while j < len(arr2):
        if arr1[i] < arr2[j]:
            i += 1
            if i == len(arr1):
                break
        else:
            #arr1[i], arr2[j] = arr2[j], arr1[i]
            arr1.insert(i,arr2[j])
            i += 1
            j += 1
    while j < len(arr2):
        arr1.append(arr2[j])
        j += 1
    print(arr1)


merge_arr_using_extra_space([1,3,5,7,9],[2,4,6,8])
merge_arr([3,5,7,8],[1,4,9,10])

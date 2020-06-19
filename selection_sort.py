def selection_sort(arr):
    for i in range(len(arr)):
        min_pos = i
        for j in range(i, len(arr)):
            if arr[j] < arr[min_pos]:
                min_pos = j
        arr[i], arr[min_pos] = arr[min_pos], arr[i]
    print(arr)
selection_sort([5, 3, 8, 7, 6, 2])

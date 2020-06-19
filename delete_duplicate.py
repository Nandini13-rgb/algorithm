def deletion(arr):
    real_arr = []
    real_arr.append(arr[0])
    j = 0
    for i in range(1, len(arr)):
        if real_arr[j] != arr[i]:
            real_arr.append(arr[i])
            j += 1
    for i in range(0, (len(arr) - len(real_arr))):
        real_arr.append(0)
    print(real_arr)


arrs = [[1, 2, 2, 3, 3, 4, 4],
        [0, 0, 3, 3, 4, 4, 5, 6],
        [3, 3, 4, 2, 5, 5, 6, 6, 7, 7, 8, 8]
        ]
for arr in arrs:
    deletion(arr)

ef product(arr1, arr2):
    answer = [0] * (len(arr2) + len(arr1))
    for i in range(len(arr2) - 1, -1, -1):
        for j in range(len(arr1) - 1, -1, -1):
            answer[i + j + 1] += arr2[i] * arr1[j]
            if answer[i + j + 1] > 9:
                carry = (answer[i + j + 1]) // 10
                answer[i + j + 1] = answer[i + j + 1] % 10
                answer[i + j + 1 - 1] += carry
    while answer[0] == 0:
        answer = answer[1:]

    return answer


result = product([1, 2,3], [7, 8, 9])
print(result)

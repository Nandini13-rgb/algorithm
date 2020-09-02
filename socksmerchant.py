def sockMerchant(n, ar):
    pair = 0
    for i in range(len(ar)):
        count = 1
        j = i+1
        while j<len(ar):
            if ar[i] == ar[j]:
                ar.pop(j)
                count += 1
                j -= 1
            j += 1
        if count%2 == 0:
            pair += (count // 2)
        elif count%2 != 0:
            pair += ((count-1)//2)
    return pair

print(sockMerchant(9, [10,20,20,10,10,30,50,10,20]))

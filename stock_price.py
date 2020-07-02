def max_profit(arr):
    for i in range(len(arr)):
        buying_price = arr[i]
        if i == len(arr)-1:
            return 0
        else:
            selling_price = max(arr[i + 1:len(arr)])
            if buying_price < selling_price:
                profit = selling_price - buying_price
                return profit
            else:
                continue
    return 0
print(max_profit([]))

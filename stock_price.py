def max_profit(arr):
    max_profit = 0
    for i in range(len(arr)):
        buying_price = arr[i]

        if i == len(arr)-1:
            return max_profit
        else:
            selling_price = max(arr[i + 1:len(arr)])
            if buying_price < selling_price:
                profit = selling_price - buying_price
                if profit > max_profit:
                    max_profit = profit
            else:
                continue


    return 0

print(max_profit([1,2,3,4]))

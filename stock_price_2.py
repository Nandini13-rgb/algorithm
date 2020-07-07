def max_profit(arr):
#def maxProfit(self, arr: List[int]) -> int:
    max_profit = 0
    for i in range(len(arr)):
        buying_price = arr[i]

        if i == len(arr)-1:
            return max_profit
        else:
            selling_price = arr[i+1]
            if buying_price < selling_price:
                profit = selling_price - buying_price
                max_profit += profit
            else:
                continue


    return 0

print(max_profit([4,3,2,1]))

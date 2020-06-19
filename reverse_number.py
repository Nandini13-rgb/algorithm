def reverse(num,digits):
    sum = 0
    place = digits-1
    while num>0: 
        r = num%10
        num = num//10
        sum += r*(10**place)
        place -= 1
    print(sum)
reverse(1234,4)

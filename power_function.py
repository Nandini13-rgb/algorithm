def power(base,p,divisor):
     #method 1
    if p == 0:
        return 1 % divisor
    else:
        result = 1
        n = 1
        while n <= p:
            result = result*base
            n += 1
        return result % divisor
    # method 2
    if p == 0:
        return 1
    else:
        result = base*power(base,p-1,divisor)
    return result%divisor

ans = power(2,0,3)
print(ans)

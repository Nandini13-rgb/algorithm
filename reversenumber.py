    def reverse(self, x: int) -> int:
        sign = 1
        if x<0:
            sign = -1
            x = x*-1
        sum = 0
        while x>0:
            r = x%10
            sum = sum*10+r
            x = x//10
        

        if not -2147483648<sum<2147483648:
            return 0
        return sign*sum

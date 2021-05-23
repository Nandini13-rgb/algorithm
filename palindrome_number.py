    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        else:
            st = str(x)
            pst = st[::-1]
            count = 0
            l = len(st)
            for i in range(len(st)):
                if st[i] == pst[i]:
                    count += 1
            if count == l:
                return True
            else:
                return False

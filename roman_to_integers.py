def romanToInt(self, s: str) -> int:
        result = 0
        i = 0
        roman_numbers = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000,'IV':4,'IX':9,'XL':40,'XC':90,'CD':400,'CM':900 }
        while i+1<=len(s):
            if i+1 == len(s):
                result += roman_numbers.get(s[i])
                i += 1
                return(result)
            else:    
                number = roman_numbers.get(s[i]) 
                number2 = roman_numbers.get(s[i+1])
                if number>=number2:
                    result += roman_numbers.get(s[i])
                    i += 1
                else:
                    result += roman_numbers.get(s[i:i+2]) 
                    i += 2
        return(result)
            

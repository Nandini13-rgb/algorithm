strs = ["flower", "flow"]
#brute force corner cases not accepted
strs = sorted(strs, key=len)

shortest = strs[0]

result = ''
if len(strs) == 1:
    print(strs)
    
j = 0 
while j < len(shortest):
    count = 0
    for i in range(1,len(strs)):
        if  shortest[j] == strs[i][j]:
            count += 1
        else:
            return result
    if count == len(strs)-1:
        result += shortest[j]
        j += 1
    else:
        return result
       
 #all cases accepted       

s = ["",""]
print(len(s))

minlen = len(s[0])
for i in range(1,len(s)):
    minlen = min(minlen, len(s[i]))
        
add = ""
for i in range(0,minlen):
    si = s[0][i]
    print(si)
    for j in range(1,len(s)):
        if si != s[j][i]:
            return add
                  
    add += si
return add
    
    
                

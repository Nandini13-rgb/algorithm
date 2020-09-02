def jumpingOnClouds(c):
    emma = 0 
    jump = 0
    while emma < len(c)-1:
        if emma == len(c)-2:
            if c[len(c)-1] == 0:
                jump += 1
                break
            else:
                break
        if c[emma+2] == 0:
            emma = emma + 2
            jump += 1
        else :
            emma = emma + 1
            jump += 1
    return jump
print(jumpingOnClouds([0,0,0,1,0,0]))

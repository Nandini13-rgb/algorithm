def countingValleys(n, s):
    count = 0
    valley = 0
    for i in range(len(s)):
        if s[i] == "D":
            count -= 1
        else:
            count += 1
            if count == 0:
                valley += 1
    return valley

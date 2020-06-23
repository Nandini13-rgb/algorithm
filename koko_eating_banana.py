def check_speed(piles, speed, given_hour):
    i = 0
    hour = 0
    piles = piles[:]
    while i < len(piles):
        piles[i] -= speed
        hour += 1
        if piles[i] <= 0:
            i += 1
    if hour <= given_hour:
        return True
    else:
        return False
def speed(low,high):
    if len(piles) == hour:
        return max(piles)
    else:
        mid = (low + high) // 2
        while low <= high:
            if check_speed(piles, mid, hour):
                if not check_speed(piles,mid - 1, hour):
                    return mid
                else:
                    return speed(low,mid-1)
            else:
                return speed(mid + 1, high)
piles = [30,11,23,4,20]
hour = 5
print(speed(1,max(piles)))

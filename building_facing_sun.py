def building_facing_sun(arr):
    stack = [arr[0]]
    total_buildings = 1
    for i in range(1,len(arr)):
        building = stack.pop()
        if building < arr[i]:
            total_buildings += 1
            stack.append(arr[i])
        else:
            stack.append(arr[i-1])
    return total_buildings
print(building_facing_sun([7,4,8,2,9]))

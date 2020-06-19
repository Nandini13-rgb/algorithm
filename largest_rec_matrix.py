def maximum_area(arr):
    stack = []
    i = 0
    max_area = 0
    area = 0
    while i<len(arr):
        if not stack:
            stack.append(i)
            i += 1
        elif arr[i] > arr[stack[-1]]:
            stack.append(i)
            i += 1
        else:
            top = stack.pop()
            if not stack:
                height = arr[top]
                width = i
                area = height*width
                max_area = max(area,max_area)
            if stack:
                height = arr[top]
                width = i - stack[-1] - 1
                area = height * width
                max_area = max(area, max_area)
    while stack:
        top = stack.pop()
        height = arr[top]
        if stack:
            width = i - stack[-1] - 1
            area = height * width
            max_area = max(area, max_area)
        else:
            width = i
            area = height * width
            max_area = max(area, max_area)

    return max_area
matrix = [[0,1,1,0],
          [1,1,1,1],
          [1,1,1,1],
          [1,1,0,0]]
rows = len(matrix)
column = len(matrix[0])
temp = 0
area = 0
for i in range(1,rows):
    for j in range(column):
        if matrix[i][j] == 1:
            matrix[i][j] += matrix[i-1][j]
    temp = maximum_area(matrix[i])
    area = max(area,temp)
print(area)




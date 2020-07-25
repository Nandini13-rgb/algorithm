def unique_path(m,n):
    matrix = []
    for i in range(m):
        matrix.append([0]*n)
    x = 0
    for y in range(n):
        matrix[x][y] = 1
    y = 0
    for x in range(m):
        matrix[x][y] = 1
    for row in range(1,m):
        for col in range(1,n):
            matrix[row][col] = matrix[row-1][col] + matrix[row][col-1]
    return matrix[m-1][n-1]
    
    
    print(unique_path(3,7))

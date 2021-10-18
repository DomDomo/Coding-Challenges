def snail(snail_map):
    maxl = len(snail_map) - 1
    minl = 0
    res = []
    x, y = 0, 0
    x_add = 1
    y_add = 0

    if snail_map[0] == []:
        return []
    
    for _ in range(len(snail_map) ** 2):
        res.append(snail_map[y][x])
        if x >= maxl and y == minl:
            x_add = 0
            y_add = 1
        if y >= maxl and x >= maxl:
            x_add = -1
            y_add = 0
        if x == minl and y >= maxl:
            x_add = 0
            y_add = -1
        if x == minl and y == minl and _ != 0:
            x_add = 1
            y_add = 0
            maxl -= 1
            minl += 1
            x += 1
            y += 1
            res[len(res)-1] = snail_map[y][x]
        
        x += x_add
        y += y_add

    return res

array = [[1,2,3],
         [4,5,6],
         [7,8,9]]
array2 = [[1,2],
         [4,5]]
array3 = [[1]]
array4 = [[]]
array5 = [[1,2,3],
         [8,9,4],
         [7,6,5]]
array6 = [[1,2,3,1],
         [4,5,6,4],
         [7,8,9,7],
         [7,8,9,7]]
array6 = [[1,2,3,1,5],
         [4,5,6,4,5],
         [7,8,9,7,5],
         [7,8,9,7,5],
         [1,1,1,1,1]]
print(snail(array6))
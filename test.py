import numpy as np

ARR = [
    [1, 2, 3, 4, 5, 6],
    [1, 2, 3, 4, 5, 6],
    [1, 2, 3, 4, 5, 6],
    [1, 2, 3, 4, 5, 6],
    [1, 2, 3, 4, 5, 6],
    [1, 2, 3, 4, 5, 6]
    ]

data = [
    [1, 2, 3, 4, 5, 6],
    [1, 2, 3, 4, 5, 6],
    [1, 2, 3, 4, 5, 6],
    [1, 2, 3, 4, 5, 6],
    [1, 2, 3, 4, 5, 6],
    [1, 2, 3, 4, 5, 6]
    ]

SIZE = 6


for i in range (0, SIZE):

    for j in range (0, SIZE):
        # if i == 0 and j == 0:
        #     data[i][j] = ARR[i][j]
        #     continue
        # if i == 0:
        #     data[i][j] = ARR[i][j] + data[i][j-1]
        #     continue
        # if j == 0:
        #     data[i][j] = ARR[i][j] + data[i-1][j]
        #     continue
        # data[i][j] = ARR[i][j] + min(data[i-1][j], data[i][j-1])

        left = None
        down = None

        if i != 0:
            left = data[i - 1][j]

        if j != 0:
            down = data[i][j-1]


        if (left == None) and (down == None):
            data[i][j] = ARR[i][j]
            print("None")

        elif left == None:
            data[i][j] = ARR[i][j] + down
            print("Down")

        elif down == None:
            data[i][j] = ARR[i][j] + left
            print("Left")
        
        else:
            data[i][j] = ARR[i][j] + min(left, down)
            print("Both")
    # print(f"{i} \n {ARR}\n {data}")

print(np.matrix(data))


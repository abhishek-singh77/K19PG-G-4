import pandas as pd
import os


def position():
    # ma= Matrix for parking slot
    # T=Taken
    # S=Start
    # E=Empty
    # P=Path
    # Sample format
    '''CSV format:-
    temp=[
    ['S','P','P','P','E'],
    ['P','T','T','P','E'],
    ['P','E','E','P','E'],
    ['P','T','T','P','E'],
    ['P','P','P','P','E'],
    ['E','E','E','E','E']
    ]'''
    # pd.DataFrame(temp).to_csv("map_grid.csv")
    ma = []  # empty temporary matrix
    df = pd.read_csv('Data' + os.path.sep + "map_grid.csv",
                     header=None)  # ,use_cols=range(1,11)) #import matrix map from csv file
    df.dropna(axis=0) # to remove missing value
    temp = df.values.tolist()

    ma = temp
    n1 = df.shape[0]  # gives number of row count
    n2 = df.shape[1]  # gives number of column count

    for x in range(n1):
        for y in range(n2):
            if ma[x][y] == 'S':  # begin at Start
                beg = [0, x, y]

    stack = []
    # Empty stack for storing distance
    stack.append(beg)
    count = 0
    while True:
        p = stack[count]
        count += 1
        x = p[1]
        y = p[2]

        # condition for finding closet empty slot
        if x - 1 >= 0 and ma[x - 1][y] == 'E':
            return (p[0] + 1, x - 1, y, n2, n1)  # return distance,x value,y value, rows, columns
            # temp[x-1][y]='T'
            # print(temp,ma)
            exit()

        if x + 1 < n1 and ma[x + 1][y] == 'E':
            return (p[0] + 1, x + 1, y, n2, n1)  # return distance,x value,y value, rows, columns
            exit()

        if y - 1 >= 0 and ma[x][y - 1] == 'E':
            # temp[x][y-1]='T'
            return (p[0] + 1, x, y - 1, n2, n1)  # return distance,x value,y value, rows, columns
            exit()

        if y + 1 < n2 and ma[x][y + 1] == 'E':
            return (p[0] + 1, x, y + 1, n2, n1)  # return distance,x value,y value, rows, columns
            exit()

        # Using path to increment in 4 direction
        if x - 1 >= 0 and ma[x - 1][y] == 'P':
            stack.append([p[0] + 1, x - 1, y])
            ma[x - 1][y] = p[0] + 1
        if x + 1 < n1 and ma[x + 1][y] == 'P':
            stack.append([p[0] + 1, x + 1, y])
            ma[x + 1][y] = p[0] + 1
        if y - 1 >= 0 and ma[x][y - 1] == 'P':
            stack.append([p[0] + 1, x, y - 1])
            ma[x][y - 1] = p[0] + 1
        if y + 1 < n2 and ma[x][y + 1] == 'P':
            stack.append([p[0] + 1, x, y + 1])
            ma[x][y + 1] = p[0] + 1

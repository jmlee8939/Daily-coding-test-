import pandas as pd


row = [0]*100
arr = []
for i in range(100):
    arr.append(row)


t_x, t_y = (20, 20)
r = 1
direction = [(0, 1), (-1, 0), (0, -1), (1, 0)]
for i in range(10):
    r = i//2 + 1
    d_x, d_y = direction[i % 4 - 1]
    d_x *= r
    d_y *= r
    t_x += d_x
    t_y += d_y
    arr[t_x][t_y] = i+1

import numpy as np

print(arr)
3direction[1%4 - 1]
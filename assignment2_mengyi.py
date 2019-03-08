import matplotlib.pyplot as plt
import array as array
import math as math
import numpy as np
from prettytable import PrettyTable


# problem 2.1 
#input: enter an integer 
#output: The final value for x 

def flowchart():
    x = int(input('Input value in integer: '))
    if x < 100:
        if x < 50:
            x = 0
        else:
            x = 75
    else:
        if x > 500:
            x -= 50
    print("Value of X after the logic:",x)
     
flowchart()    
#end 
#output x; 

# flowchart()

# 2.4

# 2.9

def economic_1(i, n):
    return i * (1 + i)**n


def economic_2(i, n):
    return (1 + i)**n - 1

def economic_formula():
    P = 55000
    i = 0.066
    t = PrettyTable(['year', 'payment'])
    for n in range(1, 6):
        a = [n] * 1
        a.append(P * economic_1(i, n) / economic_2(i, n))
        t.add_row(a)
    print(t)



economic_formula()

# 2.14

from prettytable import PrettyTable


def cal_tan():
    table = PrettyTable(['a', 'b', 'r', 'O'])
    inputs = [[1,0], [1,1], [0,1], [-1,1], [-1,0], [-1,-1], [0,-1], [1,-1], [0,0]]

    for i in inputs:
        a = i[0]
        b = i[1]
        row = [a, b, 0, 0]
        res = 0
        r = math.sqrt((a * a + b * b))
        if a > 0:
            res = math.atan(b / a)
        if a == 0:
            if b > 0:
                res = math.pi / 2
            if b < 0:
                res = -math.pi / 2
        if a < 0:
            if b > 0:
                res = math.atan(b/a) + math.pi
            if b < 0:
                res = math.atan(b/a) - math.pi
            if b == 0:
                res = math.pi
        # res = math.degrees(res)
        row[2] = r
        row[3] = res
        table.add_row(row)

    print(table)


cal_tan()


# 20.27
def cal_tank():
    h = float(input('enter a value between -1 to 16: '))
    height_range = [i for i in np.arange(-1, 17, 1)]
    print(height_range)
    r1 = 4
    r2 = 6.5
    height1 = 10
    height2 = 5
    # x/(x+5) = r1/r2
    height3 = 8
    res = 0
    s1 = math.pi * r1 * r1
    if h > 0 and h <= 16:
        if h <= 10:
            res = s1 * h
        if h > 10:
            h = 15 if h >= 15 else h
            y = h - 10
            # r3 / 6.5 = (8+y)/(8+5)
            r3 = r2 * (8+y) / 13
            res = s1 * height1 + (1/3) * math.pi * r3 * r3 * (y+height3) - (1/3)*s1*height3
    print(res)


cal_tank()



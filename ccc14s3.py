"""CCC '14 S3 - The Geneva Confection
Canadian Computing Competition: 2014 Stage 1, Senior #3
In order to ensure peace and prosperity for future generations, the United Nations is creating the world's largest candy. The ingredients must be taken in railway cars from the top of a mountain and poured into Lake Geneva. The railway system goes steeply from the mountaintop down to the lake, with a T-shaped branch in the middle as shown below.
Right now, each of the N ingredients is in its own railway car. Each railway car is assigned a positive integer from 1 to N. The ingredients must be poured into the lake in the order 1, 2, ..., I but the railway cars are lined up in some random order. The difficulty is that, because of the especially heavy gravity today, you can only move cars downhill to the lake, or sideways on the branch line. Is it still possible to pour the ingredients into the lake in the order 1, 2, ..., N?
For example, if the cars were in the order 2, 3, 1, 4, we can slide these into the lake in order as described below:
Slide car 4 out to the branch
Slide car 1 into the lake
Slide car 3 out to the branch
Slide car 2 into the lake
Slide car 3 from the branch into the lake
Slide car 4 from the branch into the lake
"""
from ccc import input, replace_input
replace_input("ccc14s3.log")

test_cnt = int(input())

def cars_scheduling(cars_list):
    branch = []
    lake_car = 0

    for car in reversed(cars_list):
        if (car == lake_car + 1):
            lake_car += 1
        else:
            branch.append(car)
    for car in reversed(branch):
        if (car == lake_car + 1):
            lake_car += 1
        else:
            return False
    return True

for i in range(0, test_cnt):
    cars_cnt = int(input())
    print(cars_scheduling([int(input()) for k in range(0, cars_cnt)]) and "Y" or "N")
    


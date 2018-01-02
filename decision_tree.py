#!/usr/bin/env python3

import csv
import random

# data = csv.read('data.csv')

# data is A or B class with one deterministic and one stochastic variables

class_list = ['A','B']

def gen_data(n):
    data = []
    for _ in range(n):
        row = []
        row.append(random.choice(['A','B']))
        if row[0] == 'A':
            row.append(random.choice(range(6,11)))
        else:
            row.append(random.choice(range(0,6)))
        row.append(random.choice(range(0,11)))
        data.append(row)
    return(data)
    
print(gen_data(10))

def branch(data,index,cutoff):
    branch_a = []
    branch_b = []
    for i in data:
        if i[index] <= cutoff:
            branch_a.append(i)
        else:
            branch_b.append(i)
    return(branch_a,branch_b)
    

def score(branches,classes):
    n_instances = sum([len(branch) for branch in branches])
    gini = 0
    for branch in branches:
        size = len(branch)
        if size == 0:
            continue
        score = 0
        for cl in classes:
            p = [row[0] for row in branch].count(cl) / size
            score += p * p
        gini += (1 - score) * (size / n_instances)
    return(gini)

def assess_variable(data,index,step):
    col = []
    for i in data:
        col.append(i[index])
    v_max = max(col)
    v_min = min(col)
    midpoint = int((v_max - v_min) / 2)
    left, right = branch(data,index,midpoint)
    gini_one = score([left,right],class_list)
    left, right = branch(data,index,midpoint+(midpoint*step))
    gini_two = score([left,right],class_list)
    gini = gini_two
    if gini_one < gini_two:
        gini = gini_one
        step = step * (-1)
        midpoint += (midpoint*step)
    for _ in range(1000000):
        new_midpoint = midpoint + midpoint*step
        new_left, new_right = branch(data,index,new_midpoint)
        gini_new = score([new_left, new_right],class_list)
        if gini_new < gini:
            gini = gini_new
            midpoint = new_midpoint
            left = new_left
            right = new_right
        else:
            step = step / 2
    return([left,right],gini,midpoint)

final_branches, gini, midpoint = assess_variable(gen_data(20),2,0.001)

print("Gini: ",gini,"\tMidpoint: ",midpoint)
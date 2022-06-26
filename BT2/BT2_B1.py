# -*- coding: utf-8 -*-
"""
Created on Sat Jun 25 22:02:18 2022

@author: elrey0801
"""

import math
pi = math.pi
"""Biểu diễn các cột là các công thức (đỉnh hình chữ nhật).
Các hàng là các yếu tố tam giác (đỉnh hình tròn)."""

name_map = {'a':0, 'b':1, 'c':2, 'alpha':3, 'beta':4, 'delta':5, 'h':6, 'S':7}
formula_map = {'00':0, '10':1, '30':2, '40':3, '11':4, '21':5, '41':6, '51':7, '02':8, '12':9, '22':10, '72':11, '33':12, '43':13, '53':14, '24':15, '64':16, '74':17}
def network_init(a=-1, b=-1, c=-1, alpha=-1, beta=-1, delta=-1, h=-1, S=-1):
#Array biểu diễn mạng ngữ nghĩa
    network = [[a, 0, a, 0, 0],
               [b, b, b, 0, 0],
               [0, c, c, 0, c],
               [alpha, 0, 0, alpha, 0],
               [beta, beta, 0, beta, 0],
               [0, delta, 0, delta, 0],
               [0, 0 ,0, 0, h],
               [0, 0, S, 0, S]]
    return network

def solve_variable(var_arr, f=-1):
    a, b, c, alpha, beta, delta, h, S = var_arr
    if f == 0:
        return b*math.sin(alpha)/math.sin(beta)
    if f == 1:
        return a*math.sin(beta)/math.sin(alpha)
    if f == 2:
        return math.asin(a*math.sin(beta)/b)
    if f == 3:
        return math.asin(b*math.sin(alpha)/a)
    if f == 4:
        return c*math.sin(beta)/math.sin(delta)
    if f == 5:
        return b*math.sin(delta)/math.sin(beta)
    if f == 6:
        return math.asin(b*math.sin(delta)/c)
    if f == 7:
        return math.asin(c*math.sin(beta)/b)
    if f == 8:
        return math.sqrt(b**2 + c**2 - 2*math.sqrt(b**2*c**2 - 4*S**2))
    if f == 9:
        return math.sqrt(a**2 + c**2 - 2*math.sqrt(a**2*c**2 - 4*S**2))
    if f == 10:
        return math.sqrt(b**2 + a**2 - 2*math.sqrt(b**2*a**2 - 4*S**2))
    if f == 11:
        p = (a+b+c)/2
        return math.sqrt(p*(p-a)*(p-b)*(p-c))
    if f == 12:
        return math.pi - beta - delta
    if f == 13:
        return math.pi - alpha - delta
    if f == 14:
        return math.pi - alpha - beta
    if f == 15:
        return 2*S/h
    if f == 16:
        return 2*S/c
    if f == 17:
        return c*h/2

def find_solution(network, a, b, c, alpha, beta, delta, h, S):
    finish = False
    global var_arr
    while not finish:
        finish = True
        #Loop through all formula
        for col in range(len(network[0])):
            #Count for unknown element in a formula
            count_unknown = 0
            unknown_var = -1
            for r in range(len(network)):
                if network[r][col] == -1:
                    count_unknown += 1
                    unknown_var = r
            if count_unknown != 1:
                continue
            #When we can find an element, set finish flag to false
            finish = False
            f = formula_map[str(unknown_var) + str(col)]
            #Find unknown element
            network[unknown_var][col] = solve_variable(var_arr, f)
            #Update new found element
            var_arr[unknown_var] = network[unknown_var][col]
            for cc in range(len(network[0])):
                if network[unknown_var][cc] != 0:
                    network[unknown_var][cc] = network[unknown_var][col]
    return network
            
def print_result(var_arr):
    name_rev = {0:'cạnh a', 1:'cạnh b', 2:'cạnh c', 3:'góc alpha (rad)', 4:'góc beta (rad)', 5:'góc delta (rad)', 6:'h', 7:'S'}
    a, b, c, alpha, beta, delta, h, S = var_arr
    if a != -1 and b != -1 and c != -1:
        if a+b<=c or a+c<=b or b+c<=a:
            print('Không phải là tam giác')
            return
    for i in range(len(var_arr)):
        if var_arr[i] == -1:
            print('Không thể tìm được {}'.format(name_rev[i]))
        else:
            print('Giá trị {} = {}'.format(name_rev[i], var_arr[i]))

#Input dữ liệu đầu vào
a = b = c = alpha = beta = delta = h = S = -1
alpha, beta, a = 30*pi/180, 60*pi/180, 5
var_arr = [a, b, c, alpha, beta, delta, h, S]
network = network_init(a, b, c, alpha, beta, delta, h, S)
find_solution(network, a, b, c, alpha, beta, delta, h, S)
print_result(var_arr)













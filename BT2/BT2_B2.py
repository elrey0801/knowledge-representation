# -*- coding: utf-8 -*-
"""
Created on Sun Jun 26 01:27:17 2022

@author: elrey0801
"""

import json
f = open('data_BT2.json')
data = json.load(f)
f.close()

def is_solvable(input_arr, dest):
    have = set(input_arr)
    used_set = set()
    used_order = []
    finish = False
    from_ele = data['GT']
    to_ele = data['KL']
    while not finish:
        finish = True
        if dest in have:
            return True, used_order
        for i in range(1, len(from_ele)+1):
            if set(from_ele[str(i)]).issubset(have) and i not in used_set:
                used_set.add(i)
                used_order.append(i)
                #for ele in to_ele[str(i)]:
                 #   have.add(ele)
                have.update(to_ele[str(i)])
                finish = False
                break
    
    return False, None
                
            
def backward(input_arr, dest, used):
    used_equa = []
    from_ele = data['GT']
    to_ele = data['KL']
    equa = data['PT']
    have = set(input_arr)
    need_have = set([dest])
    
    for i in range(len(used) - 1, -1, -1):
        join_set = set(to_ele[str(used[i])]).intersection(need_have)
        if len(join_set) == 0:
            continue
        used_equa.append(used[i])
        need_have -= join_set
        need_have.update(set(from_ele[str(used[i])]))
        if need_have.issubset(have):
            used_equa.reverse()
            for e in used_equa:
                print(equa[str(e)])
            return

def solve(input_arr, dest):
    if dest in input_arr:
        print('Đã có {}'.format(dest))
    else:
        flag, used = is_solvable(input_arr, dest)
        if flag:
            print('Có thể điều chế được {}'.format(dest))
            print('Các bước điều chế như sau:')
            backward(input_arr, dest, used)
        else:
            print('Không thể điều chế được {} từ các chất và các tri thức đã cho'.format(dest))
            
            
            
input_arr = ['S', 'H2O', 'NaCl']
dest = 'Na2SO4'
solve(input_arr, dest)

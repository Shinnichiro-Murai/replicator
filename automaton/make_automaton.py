# -*- coding: utf-8 -*-

# built-in module(s)
import sys
import os
from typing import Awaitable
from graphviz import Digraph

# not built-in
try:
    import pandas as pd

except ImportError as ie:
    print(ie.name + " cannot be imported!")
    sys.exit(1)

def make_automaton(num):
    inCsv = pd.read_csv( sys.argv[1], encoding="utf_8", header=None)
    print(num)
    name = str(inCsv.iloc[int(num)-1, 0])
    n = inCsv.iloc[int(num)-1, 1]
    change = inCsv.iloc[int(num)-1, 3]
    init_sit = str(inCsv.iloc[int(num)-1, 4])
    if init_sit == 'C':
        init_sit = 'R'
    elif init_sit == "D":
        init_sit = "P"
    if n > 1:
        ano_sit = str(inCsv.iloc[int(num)-1, 5])
        if ano_sit == "C":
            ano_sit = "R"
        elif ano_sit == "D":
            ano_sit = "P"
    else: 
        ano_sit = 0
    print(init_sit)
    if n > 1:
        print(ano_sit)

    if change == 2:
        result = ['g', 'b']
    elif change == 4:
        result = ['CC', 'CD', 'DC', 'DD']
        
    label_RR = []
    label_RP = []
    label_PR = []
    label_PP = []
    for i in range(0, change):
        if inCsv.iloc[int(num)-1, n*2+4+i] == 0:
            if init_sit == "R":
                label_RR.append(result[i%change])
            elif init_sit == "P":
                label_PP.append(result[i%change])
        if inCsv.iloc[int(num)-1, n*2+4+i] == 1:
            if init_sit == "R":
                label_RP.append(result[i%change])
            elif init_sit == "P":
                label_PR.append(result[i%change])
        if inCsv.iloc[int(num)-1, n*2+4+change+i] == 0:
            if init_sit == "R":
                label_PR.append(result[i%change])
            elif init_sit == "P":
                label_RP.append(result[i%change])
        if inCsv.iloc[int(num)-1, n*2+4+change+i] == 1:
            if init_sit == "R":
                label_PP.append(result[i%change])
            elif init_sit == "P":
                label_RR.append(result[i%change])

    print(label_RR)
    print(label_RP)
    print(label_PR)
    print(label_PP)

    G = Digraph(format="png")
    G.attr('graph', rankdir="LR")
    G.attr("node", shape="circle", style="filled",color="#0000CD", fillcolor="#FFFFFD")
    G.node(init_sit, style="filled", color="#0000CD", fillcolor="#FFFFFD")
    if ano_sit != 0:
        G.node(ano_sit, style="filled", color="#212121", fillcolor="#FFFFFD")
    if len(label_RR) != 0:
        label_RR = ','.join(label_RR)
        G.edge("R","R",label=label_RR)
    if len(label_RP) != 0:
        label_RP = ','.join(label_RP)
        G.edge("R","P",label=label_RP)
    if len(label_PR) != 0:
        label_PR = ','.join(label_PR)
        G.edge("P","R",label=label_PR)
    if len(label_PP) != 0:
        label_PP = ','.join(label_PP)
        G.edge("P","P",label=label_PP)
    G.render('FSA_'+name) #png/直下

if __name__ == '__main__':
    for num in range(1, 483):
        make_automaton(num)
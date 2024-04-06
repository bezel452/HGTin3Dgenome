'''
    Evaluate the model in my project
'''

import cooler
from distance_aly import CenterAndRadius, dis
import matplotlib.pyplot as plt
import numpy as np
from HGTcopy import copy_proc

def pointDistribution(coordinate_file, cool_file, anno_file, resolution):
    center, r, points = CenterAndRadius(coordinate_file)
    ball = {"Center": center,
            "Radius": r,
            "Points": points}
    data = ball['Points']
    c = ball['Center']
    distance = []
    for i in range(len(data)):
        distance.append(dis(data[i], c) / ball['Radius'])
    
    X = sorted(distance)
    
    '''
    axl = plt.subplot()
    axl.set_xlabel('Proportion of Radius')
    axl.set_ylabel('Frequency')
    plt.title('Distribution of Points')
    plt.hist(X, bins = 50)
    plt.show()
    '''
    '''    OUTPUT THE DATA
    output = coordinate_file.split('.')[1] + '.txt'
    with open(output, 'w') as f:
        for d in X:
            f.write(str(d) + '\n')
    '''
    return X

def OutputGeneList(coordinate_file, cool_file, anno_file, resolution):
    center, r, points = CenterAndRadius(coordinate_file)
    ball = {"Center": center,
            "Radius": r,
            "Points": points}
    HGT, gene = copy_proc(cool_file, anno_file, resolution)
    data = np.loadtxt(coordinate_file, delimiter=' ')   
    axl_HGT = list()
    indices = list()
    for idx, _, _, _, cnt in HGT:
        tmp = data[idx]
        x = tmp[0]
        y = tmp[1]
        z = tmp[2]
        for i in range(cnt):
            axl_HGT.append([x, y, z])
            indices.append(idx)
    HGTdIS = list()
    visited = -1
    for idx in range(len(axl_HGT)):
        
        if visited != indices[idx]:
            
            axl = axl_HGT[idx]
            d = dis(axl, ball['Center'])
            visited = indices[idx]
            for g in gene[visited]:
                HGTdIS.append([d / ball['Radius'], g[0], g[1], g[2]])
    population = pointDistribution(coordinate_file, cool_file, anno_file, resolution)
    sample = sorted(HGTdIS, key = lambda x: x[0])
    sample = sample[:-1]
    
    pos = -1
    Mid = np.median(population)
    for i in range(len(sample)):
        if sample[i][0] > Mid:
            pos = i
            break
    G_list1 = sample[:pos]
    G_list2 = sample[pos:]
    outputList(coordinate_file + 'Left', G_list1)
    outputList(coordinate_file + 'Right', G_list2)

def outputList(Target, Gene):
    res = list()
    for d in Gene:
        tmp = 'chr' + d[1]
        tmp = tmp + '\t' + str(d[2]) + '\t' + str(d[3]) + '\n'
        res.append(tmp)
    outputfile = Target.split('.')[1] + '.bed'
    with open(outputfile, 'w') as f:
        f.writelines(res)
        

if __name__ == '__main__':
    coordinate_file = 'PM2.H001_500k'
    cool_file = 'GSM1551550_HIC001.mcool'
    anno_file = "anno_HGTcopy_sorted"   
    resolution = 500000
    #pointDistribution(coordinate_file, cool_file, anno_file, resolution)
    OutputGeneList(coordinate_file, cool_file, anno_file, resolution)
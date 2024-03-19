'''
    analyze the copy of HGT distribution
'''

import numpy as np
import cooler
import math
from distance_aly import CenterAndRadius, dis
from HGTcopy import copy_proc

def analyzeCopy(coordinate_file, cool_file, anno_file, resolution):
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
    cnt1 = 0
    cnt2 = 0
    cnt3 = 0
    cnt4 = 0
    HGTdIS = list()
    visited = -1
    gen_list1 = list()
    gen_list2 = list()
    gen_list3 = list()
    gen_list4 = list()
    for idx in range(len(axl_HGT)):
        axl = axl_HGT[idx]
        d = dis(axl, ball['Center'])
        HGTdIS.append([idx, d])
        if d < ball['Radius'] / 4:
            cnt1 += 1
            if visited != indices[idx]:
                visited = indices[idx]
                for g in gene[visited]:
                    gen_list1.append(g)
        elif d < ball['Radius'] / 2:
            cnt2 += 1
            if visited != indices[idx]:
                visited = indices[idx]
                for g in gene[visited]:
                    gen_list2.append(g)
        elif d < ball['Radius'] * 3 / 4:
            cnt3 += 1
            if visited != indices[idx]:
                visited = indices[idx]
                for g in gene[visited]:
                    gen_list3.append(g)
        else:
            cnt4 += 1
            if visited != indices[idx]:
                visited = indices[idx]
                for g in gene[visited]:
                    gen_list4.append(g)
    print("LESS THAN 1/4 RADIUS: ", cnt1)
    print("LESS THAN 1/2 RADIUS: ", cnt2)
    print("LESS THAN 3/4 RADIUS: ", cnt3)
    print("GREATER THAN 3/4 RADIUS: ", cnt4)
    '''
    print(gen_list1)
    print(gen_list2)
    print(gen_list3)
    print(gen_list4)
    print(len(gen_list1))
    print(len(gen_list2))
    print(len(gen_list3))
    print(len(gen_list4))
    '''
    t = coordinate_file.split('.')[1]
    outputGene(gen_list4, 'GreaterThan3quartersRadius' + '_' + t + '.bed')

def outputGene(gene, outputFile):
    res = list()
    for g in gene:
        tmp = 'chr' + g[0]
        tmp = tmp + '\t' + str(g[1]) + '\t' + str(g[2]) + '\n'
        res.append(tmp)
    with open(outputFile, 'w') as f:
        f.writelines(res)

if __name__ == '__main__':
    coordinate_file = 'PM2.H050_500K'
    cool_file = 'GSM1551599_HIC050.mcool'
    anno_file = "anno_HGTcopy_sorted"
    resolution = 500000
    analyzeCopy(coordinate_file, cool_file, anno_file, resolution)

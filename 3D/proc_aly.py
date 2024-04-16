'''
    analyze the copy of HGT distribution
'''
import matplotlib.pyplot as plt
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
        HGTdIS.append(d / ball['Radius'])
        if d < ball['Radius'] * (0.5 ** (2 / 3)):
            cnt1 += 1
            if visited != indices[idx]:
                visited = indices[idx]
                for g in gene[visited]:
                    gen_list1.append(g)
        elif d < ball['Radius'] * (0.5 ** (1 / 3)):
            cnt2 += 1
            if visited != indices[idx]:
                visited = indices[idx]
                for g in gene[visited]:
                    gen_list2.append(g)
        elif d < ball['Radius'] * ((3 / 4) ** (1 / 3)):
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
    print("LESS THAN 1/4 VOLUME: ", cnt1)
    print("LESS THAN 1/2 VOLUME: ", cnt2)
    print("LESS THAN 3/4 VOLUME: ", cnt3)
    print("GREATER THAN 3/4 VOLUME: ", cnt4)

    output = coordinate_file.split('.')[1] + '_' + anno_file + 'hGT.txt'
    X = sorted(HGTdIS)
    with open(output, 'w') as f:
        for x in X:
            f.write(str(x) + '\n')
    
    
    t = coordinate_file.split('.')[1] + anno_file
    outputGene(gen_list1, 'LessThan1quarterVOLUME' + '_' + t + '.bed')
    outputGene(gen_list2, 'LessThanHalfVOLUME' + '_' + t + '.bed')
    outputGene(gen_list3, 'LessThan3quartersVOLUME' + '_' + t + '.bed')
    outputGene(gen_list4, 'GreaterThan3quartersVOLUME' + '_' + t + '.bed')
#    drawHist(HGTdIS)
    

def drawHist(data):
    X = sorted(data)
    axl = plt.subplot()
    axl.set_xlabel('Proportion of Radius')
    axl.set_ylabel('Frequency')
    plt.title('Distribution of HGT Sequences')
    plt.hist(X, bins = 50)
    plt.show()


def outputGene(gene, outputFile):
    res = list()
    for g in gene:
        tmp = 'chr' + g[0]
        tmp = tmp + '\t' + str(g[1]) + '\t' + str(g[2]) + '\n'
        res.append(tmp)
    with open(outputFile, 'w') as f:
        f.writelines(res)

if __name__ == '__main__':
    coordinate_file = 'PM2.H001_500k'
    cool_file = 'GSM1551550_HIC001.mcool'
    anno_file = "anno_only_sorted"   
    resolution = 500000
    analyzeCopy(coordinate_file, cool_file, anno_file, resolution)

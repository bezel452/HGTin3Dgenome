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
    HGT = copy_proc(cool_file, anno_file, resolution)
    data = np.loadtxt(coordinate_file, delimiter=' ')   
    axl_HGT = list()
    for idx, _, _, _, cnt in HGT:
        tmp = data[idx]
        x = tmp[0]
        y = tmp[1]
        z = tmp[2]
        for i in range(cnt):
            axl_HGT.append([x, y, z])
    cnt1 = 0
    cnt2 = 0
    cnt3 = 0
    cnt4 = 0
    HGTdIS = list()
    for axl in axl_HGT:
        d = dis(axl, ball['Center'])
        HGTdIS.append(d)
        if d < ball['Radius'] / 4:
            cnt1 += 1
        elif d < ball['Radius'] / 2:
            cnt2 += 1
        elif d < ball['Radius'] * 3 / 4:
            cnt3 += 1
        else:
            cnt4 += 1
    print("LESS THAN 1/4 RADIUS: ", cnt1)
    print("LESS THAN 1/2 RADIUS: ", cnt2)
    print("LESS THAN 3/4 RADIUS: ", cnt3)
    print("GREATER THAN 3/4 RADIUS: ", cnt4)


if __name__ == '__main__':
    coordinate_file = 'PM2.H050_500K'
    cool_file = 'GSM1551599_HIC050.mcool'
    anno_file = "anno_HGTcopy_sorted"
    resolution = 500000
    analyzeCopy(coordinate_file, cool_file, anno_file, resolution)

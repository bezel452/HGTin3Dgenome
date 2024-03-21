'''
    calculate the distance and analyse it
    radius of the ball
'''

import numpy as np
from sklearn.neighbors import BallTree
import math
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from HGT_mark import HGTmark
import cooler
from plt_3D import marked, HGTaxl

def dis(point1, point2):
    return math.sqrt((point1[0] - point2[0]) * (point1[0] - point2[0])  + (point1[1] - point2[1]) * (point1[1] - point2[1]) + (point1[2] - point2[2]) * (point1[2] - point2[2]))

def CenterAndRadius(file):
    data = np.loadtxt(file, delimiter=' ')
    points = data[~np.isnan(data).any(axis=1)]
#    print(points)
    np.random.shuffle(points)
#   print(points)
#    print(points[:, 0])
    eps = 1e-8 
    origin = np.array([0.0, 0.0, 0.0])
    delta = 100.0
    r = 9999999
    while delta > eps:
        pos = 0
        for i in range(0, len(points)):
            if dis(points[i], origin) > dis(points[pos], origin):
                pos = i
        r = dis(points[pos], origin)
        origin[0] = origin[0] + (points[pos][0] - origin[0]) / r * delta
        origin[1] = origin[1] + (points[pos][1] - origin[1]) / r * delta
        origin[2] = origin[2] + (points[pos][2] - origin[2]) / r * delta
        delta = delta * 0.98
    return origin, r, points
    
    
def test(center, R, points):
    fig = plt.figure(figsize = (15, 9))
    plt.rcParams['figure.facecolor'] = 'black'
    plt.rcParams['axes.facecolor'] = 'black'
    plt.rcParams['savefig.facecolor'] = 'black'   
    axl = fig.add_subplot(111, projection='3d')
    axl.scatter(points[:, 0], points[:, 1], points[:, 2], c = 'red')
    u = np.linspace(0, 2 * np.pi, 100)
    v = np.linspace(0, np.pi, 50)
    x = center[0] + R * np.outer(np.cos(u), np.sin(v))
    y = center[1] + R * np.outer(np.sin(u), np.sin(v))
    z = center[2] + R * np.outer(np.ones(np.size(u)), np.cos(v))
    axl.plot_surface(x, y, z, alpha = 0.5)

    plt.show()

def analyze1(axl_file, file, res, HGT_file, center, R):
    c = cooler.Cooler(file + '::/resolutions/' + str(res))
    B = c.bins()[:]
    chrom_dic = dict()
    Chro = B['chrom']
    chrom_col = dict()
    pre = ''
    pos = -1
    for i in range(len(Chro)):
        if Chro[i] != pre:
            pos += 1
            pre = Chro[i]
            chrom_dic[i] = 'chr' + Chro[i]
            
    data = np.loadtxt(axl_file, delimiter=' ')    
    x, y, z = marked(data, chrom_dic.keys())
    HGT = HGTmark(res, file, "anno_HGT")   # HGT标记
    H_x, H_y, H_z = HGTaxl(HGT, data)
    dis_m = 0        # more than R/2
    dis_l = 0        # less than R/2
    for i in range(len(H_x)):
        tmp = np.array((H_x[i], H_y[i], H_z[i]))
        if dis(tmp, center) > R * (0.5 ** (1 / 3)):
            dis_m += 1
        else:
            dis_l += 1
    print("THE NUMBER OF POINTS WHICH IS GREATER THAN HALF OF VOLUME: %d" %dis_m)
    print("THE NUMBER OF POINTS WHICH IS LESS THAN HALF OF VOLUME: %d" %dis_l)

if __name__ == '__main__':
    center, r, points = CenterAndRadius('PM2.H050_500K')
    print(center)
    print(r)
#    test(center, r, points)
    analyze1('PM2.H001_500k', 'GSM1551550_HIC001.mcool', 500000, 'ann_HGT', center, r)
    
    
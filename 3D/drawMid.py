'''
    draw the figure for the report of middle
'''
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import math
import cooler
from HGT_mark import HGTmark

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
    

    plt.show()

def marked(data, dic):
    x = list()
    y = list()
    z = list()
    pos = 0
    tmpx = list()
    tmpy = list()
    tmpz = list()
    
    for s in dic:
        if s == 0:
            continue
        while pos <= len(data):
            if s == pos and s != 0:
                x.append(tmpx)
                y.append(tmpy)
                z.append(tmpz)
                tmpx = list()
                tmpy = list()
                tmpz = list()
                break
            tmp = data[pos]
            
            tmpx.append(tmp[0])
            tmpy.append(tmp[1])
            tmpz.append(tmp[2])
            
            pos += 1
    return x, y, z

def HGTaxl(HGT, data):
    x = list()
    y = list()
    z = list()
    for i in HGT:
        x.append(data[i][0])
        y.append(data[i][1])
        z.append(data[i][2])
    return x, y, z

def get_axl(cool_file, resolution, axl_file):
    c = cooler.Cooler(cool_file + '::/resolutions/' + str(resolution))
    B = c.bins()[:]
    chrom_dic = dict()
    Chro = B['chrom']
    colors = plt.get_cmap('RdBu', 24)
    chrom_col = dict()
    pre = ''
    pos = -1
    for i in range(len(Chro)):
        if Chro[i] != pre:
            pos += 1
            pre = Chro[i]
            chrom_dic[i] = 'chr' + Chro[i]
            chrom_col[pos] = colors([pos])
    data = np.loadtxt(axl_file, delimiter=' ')
    x, y, z = marked(data, chrom_dic.keys())
    return x, y, z, chrom_col, chrom_dic, data

def get_HGTaxl(resolution, cool_file, HGT_file, data):
    HGT = HGTmark(resolution, file, "anno_HGT")   # HGT标记
    H_x, H_y, H_z = HGTaxl(HGT, data)
    return H_x, H_y, H_z

if __name__ == "__main__":
    file = 'GSM1551599_HIC050.mcool'
    resolution = 500000
    x, y, z, chrom_col, chrom_dic, data = get_axl(file, resolution, "PM2.H050_500K")
    center, r, points = CenterAndRadius('PM2.H050_500K')
    fig = plt.figure(figsize = (15, 9))
    
    plt.rcParams['figure.facecolor'] = 'black'
    plt.rcParams['axes.facecolor'] = 'black'
    plt.rcParams['savefig.facecolor'] = 'black'
    
   
    H_x, H_y, H_z = get_HGTaxl(resolution, file, "anno_HGT", data)

    chl = list(chrom_dic.values())
  
    chl = chl[:-1]
    
    axl = fig.add_subplot(111, projection='3d')
    tps = []
    axl.set_box_aspect([1,1,1])
    for i in range(len(x)):
        t = axl.plot(x[i], y[i], z[i], c=chrom_col[i])
        tps.append(t)
    axl.scatter(H_x, H_y, H_z, c="yellow")
    plt.legend(tps, chl, facecolor='white')
    axl.set_axis_off()
 #   axl.scatter(points[:, 0], points[:, 1], points[:, 2], c = 'red')
    u = np.linspace(0, 2 * np.pi, 100)
    v = np.linspace(0, np.pi, 50)
    x = center[0] + r * np.outer(np.cos(u), np.sin(v))
    y = center[1] + r * np.outer(np.sin(u), np.sin(v))
    z = center[2] + r * np.outer(np.ones(np.size(u)), np.cos(v))
    axl.plot_surface(x, y, z, alpha = 0.3)
    plt.show()
    
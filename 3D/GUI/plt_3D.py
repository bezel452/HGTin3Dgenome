'''
    draw the figure
'''
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

import cooler
from HGT_mark import HGTmark

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
    HGT = HGTmark(resolution, cool_file, HGT_file)   # HGT标记
    H_x, H_y, H_z = HGTaxl(HGT, data)
    return H_x, H_y, H_z

def drawPicture(anno, file, axl, resolution):
    x, y, z, chrom_col, chrom_dic, data = get_axl(file, resolution, axl)
    
    fig = plt.figure(figsize = (15, 9))
    
    plt.rcParams['figure.facecolor'] = 'black'
    plt.rcParams['axes.facecolor'] = 'black'
    plt.rcParams['savefig.facecolor'] = 'black'
    
   
    H_x, H_y, H_z = get_HGTaxl(resolution, file, anno, data)

    chl = list(chrom_dic.values())
  
    chl = chl[:-1]
    
    axl = fig.add_subplot(111, projection='3d')
    tps = []
    for i in range(len(x)):
        t = axl.plot(x[i], y[i], z[i], c=chrom_col[i])
        tps.append(t)
    axl.scatter(H_x, H_y, H_z, c="yellow")
    plt.legend(tps, chl, facecolor='white')
    axl.set_axis_off()
    
    plt.show()


if __name__ == "__main__":
    file = 'GSM1551599_HIC050.mcool'
    resolution = 1000000
    axl = "PM2.H050_1M"
    anno_file = 'anno_HGT'
    drawPicture(anno_file, file, axl, resolution)
    
    
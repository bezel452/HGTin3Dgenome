import sys
import cooler

def HGTmark(resolution, file, HGT) -> list:
    
    c = cooler.Cooler(file + '::/resolutions/' + str(resolution))
    B = c.bins()[:]
    chros = B["chrom"]
    l = B['start']
    r = B['end']
    
    HGT_IN = list()
    with open(HGT, "r") as f:
        line = f.readline()
        while line:
            line = line.split(":")
            interval = line[1].split("-")
            tmp = (line[0], int(interval[0]), int(interval[1][:-1]))
            HGT_IN.append(tmp)
            line = f.readline()
    res = list()
#    print(HGT_IN)
#    print(len(chros))
    unmatch = list()
    #print(len(HGT_IN))
    for data in HGT_IN:
        flag = False
        for i in range(len(chros) - 1):
        
            if data[0] != chros[i]:
            #    print(chros[i], l[i], r[i])
                continue
            if l[i] <= data[1] and r[i] >= data[2]:
            #    print((chros[i], l[i], r[i]), data, i)
                flag = True
                res.append(i)
                
            elif l[i] <= data[1] and r[i] < data[2] and data[1] < r[i]:
                flag = True
                res.append(i)
                res.append(i + 1)
        
        if flag == False:
            unmatch.append(data)
    #print(len(res))
    #print(unmatch)
    return res



if __name__ == '__main__':
    HGTmark(500000, 'GSM1551550_HIC001.mcool', "anno_HGT")
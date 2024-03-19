'''
    processing the copy sequences
'''

import cooler

def copy_proc(file, HGT, res):
    c = cooler.Cooler(file + '::/resolutions/' + str(res))
    B = c.bins()[:]
    chros = B["chrom"]
    l = B['start']
    r = B['end']

    HGT_IN = list()
    with open(HGT, 'r') as f:
        line = f.readline()
        while line:
            tmp = list()
            line = line.split(':')
            chrom = line[0]
            intervals = line[1].split('-')
            sta = intervals[0]
            end = intervals[1][:-1]
            tmp = [chrom, int(sta), int(end)]
            HGT_IN.append(tmp)
            line = f.readline()
#    unmatched = list()
    points = list()         # [idx, chrom, start, end, nums]
    pos = 0
#    pts = 0
    gene = dict()
    for idx in range(len(chros) - 1):
        num = 0
    #    print(HGT_IN[pos][2])
        while pos < len(HGT_IN) and chros[idx] == HGT_IN[pos][0] and r[idx] >= HGT_IN[pos][2]:
            '''
            if idx > 0 and l[idx] > HGT_IN[pos][1]:
                if (l[idx] - HGT_IN[pos][1]) * 2 > HGT_IN[pos][2] - HGT_IN[pos][1] + 1:
                    points[pts - 1][4] += 1
                else:
                    num += 1
            else:
                num += 1
            '''
            num += 1
            if idx not in gene.keys():
                gene[idx] = list()
            gene[idx].append([HGT_IN[pos][0], HGT_IN[pos][1], HGT_IN[pos][2]])
            pos += 1
        if num == 0:
            continue
        tmp = [idx, chros[idx], l[idx], r[idx], num]
        points.append(tmp)
    #    pts += 1
    return points, gene

if __name__ == '__main__':
    res, gene = copy_proc('GSM1551550_HIC001.mcool', "anno_HGTcopy_sorted", 1000000)
    print(res)
    ans = 0
    for i in res:
        ans += i[4]
    print(ans)     
    print(gene)   

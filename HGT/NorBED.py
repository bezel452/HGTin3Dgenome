import numpy as np

file_path = 'hg38_copy\copy\copy.bed'

dic_file = 'copy_trans'
out_put = 'HGTcopy_hg38.bed'
trans_dic = dict()
with open(dic_file, 'r') as f:
    line = f.readline()
    while line:
        line = line.split('  ')
    #    print(line[0], line[1])
        trans_dic[line[0]] = line[1][:-1]
        line = f.readline()
# print(trans_dic)
    
res = list()

with open(file_path, 'r') as f:
    line = f.readline()
    while line:
        line = line.split('\t')
        t = line[0]
        t = t.split('.')
        t = t[0]
        if t in trans_dic.keys():
            t = trans_dic[t]
        else:
            t = t[-2:]
            if t[0] == '0':
                t = t[1:]
            if t == "23":
                t = "X"
            if t == "24":
                t = "Y"
            t = 'chr' + t
        chrom = t + '\t' + line[1] + '\t' + line[2]
        res.append(chrom)
        line = f.readline()
    
with open(out_put, 'w') as f:
    f.writelines(res)


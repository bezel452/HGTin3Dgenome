import os
import sys

def getID(file):
    
    Gene_ID = set()
    with open(file, 'r') as f:
        line = f.readline()
        while line:
            if line[0] == '#':
                break
            line = line.split('\t')
            t = line[8].split(';')
            t = t[0].split('"')
            Gene_ID.add(t[1] + '\n')
            line = f.readline()
#    print(len(Gene_ID))
    return Gene_ID

if __name__ == '__main__':
    dire = 'uniqueData'
    for file in os.listdir(dire):
        f = file[0:4]
        tit = file.split('.')
        if len(tit) >= 2:
            t = tit[1]
            if t == 'gtf':
                print(file)
                output = file.split('.')[0] + 'gene'
                data = getID(dire + '/'  + file)
                if len(data) == 0:
                    continue
                with open(dire + '/' + output, 'w') as f:
                    f.writelines(data)
#    getID('GeneAnalysisData/all.gtf')
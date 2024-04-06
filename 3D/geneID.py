import os
import sys



def getID(file):
    output = file.split('.')[0] + 'gene'

    Gene_ID = set()
    with open(file, 'r') as f:
        line = f.readline()
        while line:
            line = line.split('\t')
            t = line[8].split(';')
            t = t[0].split('"')
            Gene_ID.add(t[1] + '\n')
            line = f.readline()

    with open(output, 'w') as f:
        f.writelines(Gene_ID)

if __name__ == '__main__':
    for file in os.listdir():
        f = file[0:4]
        tit = file.split('.')
        if len(tit) >= 2:
            t = tit[1]
            if f == 'H050' and t == 'gtf':
                print(file)
                getID(file)
import os, sys

def getOnly(directory, file):
    input_file = directory + '/' + file
    with open(input_file, 'r') as f:
        cnt = 0
        line = f.readline()
        tmp = line
        while line:
            cnt += 1
            line = f.readline()
            if cnt > 1:
                return None
    return tmp

def normalize(file):
    ans = []
    with open(file, 'r') as f:
        line = f.readline()
        while line:
            t = line.split('\t')
            idx = t[0].split('.')
            
            idx = idx[0][-2:]
            if idx[0] == '0':
                idx = 'chr' + idx[1]
            elif idx == '23':
                idx = 'chrX'
            elif idx == '24':
                idx = 'chrY'
            else:
                idx = 'chr' + idx[0] + idx[1]
            tmp = idx + '\t' + t[1] + '\t' + t[2]
            ans.append(tmp)
            line = f.readline()
    out = 'OnlyCopyfixed_hg38.bed'
    with open(out, 'w') as f:
        f.writelines(ans)


if __name__ == '__main__':
    output = 'OnlyCopy_hg38.bed'
    '''
    directory = 'hg38_copy/copy'
    res = list()
    for file in os.listdir(directory):
        tmp = file.split('_')
        if tmp[0][0] == 'N':
            data = getOnly(directory, file)   # search the only copy sequences
            if data == None:
                continue
            else:
                res.append(data)
    
    with open(output, 'w') as f:
        f.writelines(res)
    '''
    normalize(output)   # change the name of chromsomes

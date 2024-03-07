input_file = 'anno_HGTcopy'
output_file = input_file + '_sorted'

data = list()

with open(input_file, 'r') as f:
    line = f.readline()
    while line:
        line = line.split(':')
        t1 = line[0]
        tmp = line[1].split('-')
        t2 = tmp[0]
        t3 = tmp[1]
        if t1 == 'X':
            t1 = 23
        elif t1 == 'Y':
            t1 = 24
        else:
            t1 = int(t1)
        data.append([t1, int(t2), int(t3[:-1])])
        line = f.readline()

data_sort = sorted(data, key = lambda x: (x[0], x[1], x[2]))

res = []

for d in data_sort:
    t1 = str(d[0])
    if t1 == '23':
        t1 = 'X'
    if t1 == '24':
        t1 = 'Y'
    tmp = t1 + ':' + str(d[1]) + '-' + str(d[2]) + '\n'
    res.append(tmp)

with open(output_file, 'w') as f:
    f.writelines(res)

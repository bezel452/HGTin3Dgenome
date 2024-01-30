import sys

def USAGE(n):
    if n != 3:
        print("USAGE: 2 parameters are needed!")
        exit()

USAGE(len(sys.argv))

input_file = sys.argv[1]
output_file = sys.argv[2]
res = []
with open(input_file, "r") as f:
    line = f.readline()
    while line:
        line = line.split("\t")
        chrm = line[0][3:]
        tmp = chrm + ":" + line[1] + "-" + line[2]
        res.append(tmp)
        line = f.readline()

with open(output_file, "w") as f:
    f.writelines(res)
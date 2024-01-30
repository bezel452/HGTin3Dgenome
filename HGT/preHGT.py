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
        if line[0] == '>':
            line = line[1:]
            res.append(line)
        line = f.readline()
    
with open(output_file, "w") as f:
    f.writelines(res)



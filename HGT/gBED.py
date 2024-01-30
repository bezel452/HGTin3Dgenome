import sys

def USAGE(n):
    if n != 3:
        print("USAGE: 2 parameters are needed!")
        exit()

USAGE(len(sys.argv))

input_file = sys.argv[1]
output_file = sys.argv[2]

special_seq = {
    "NW_015495301": "chr4",
    "NW_016107312": "chr19",
    "NW_019805491": "chr3",
    "NW_025791779": "chr5"
}

with open(input_file, "r") as f:
    line = f.readline()
    res = []
    while line:
        t = line.split("-")
        start = t[1]
        end = t[2]
        t = t[0].split(".")
        if t[0] in special_seq:
            chrom = special_seq[t[0]]
        else:
            num = t[0][-2:]
            if num[0] == '0':
                num = num[1:]
            if num == "23":
                num = "X"
            if num == "24":
                num = "Y"
            chrom = "chr" + num
            
        temp = chrom + "\t" + start + "\t" + end
        res.append(temp)
        line = f.readline()
    
with open(output_file, "w") as f:
    f.writelines(res)


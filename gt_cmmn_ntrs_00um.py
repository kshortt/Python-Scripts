#fileA uniq entries
import string

fileA = open("U:/ARDS_SNPs_wes_vs_1000g/Filter_functional_variants/EA_S_X2significant.xlsx",'r')
fileB = open("U:/ARDS_SNPs_wes_vs_1000g/Chi_square_python/Cauc_control_forX2.txt",'r')
newfile = open("U:/ARDS_SNPs_wes_vs_1000g/Filter_functional_variants/EA_S_X2significant_allelecnt.txt",'w')
lineA = fileA.readline()
lineB = fileB.readline()
chk = 0
while 1:
    recA = string.split(lineA, "\t")
    recB = string.split(lineB, "\t")
    #print recA[0],recB[0]
    if string.strip(recA[0]) == string.strip(recB[0]):
        newfile.write(string.strip(lineB) + "\t" + lineA)
        lineB = fileB.readline()
        if lineB == "":
                chk = 2
                break        
    elif string.strip(recA[0]) > string.strip(recB[0]):
        #print recA[0],">",recB[0]
        lineB = fileB.readline()
        if lineB == "":
                chk = 2
                break
    elif string.strip(recA[0]) < string.strip(recB[0]):
        #print recA[0],"<",recB[0]
        #newfile.write(lineA)
        lineA = fileA.readline()
        if lineA == "":
                chk = 1
                break
    else: print "ERROR"

newfile.close()
fileA.close()
fileB.close()
print "END"



        


LOCATION_INPUT = "U:/ARDS_SNPs_exome_sequence_data/Chi_square_python/"
INPUT = "EA_PnexEA1000G.txt"


LOCATION_OUTPUT = "U:/ARDS_SNPs_exome_sequence_data/Chi_square_python/"

OUTPUT = "EA_PnexEA1000G_chi_fish_tst.txt"


#calculate chi square and fisher exact on the file with 4 descriptive
# entries and 4 data entries: Cntrl A, Cntrl B, Cndtn A, Cndtn B.
###################################################################

import scipy.stats
import numpy as np
from numpy import *
from array import *
import string

file = open(LOCATION_INPUT + INPUT,'r')#
newfile = open(LOCATION_OUTPUT + OUTPUT,'w')
line = file.readline()#title
rec = string.split(line,"\t")
newfile.write(rec[0] + "\t" + rec[1] + "\t" + rec[2] + "\t" + rec[3]\
                      + "\tX2" + "\tX2 P value\t"\
                      + "Fisher Exact\t" + "FE P value\n")
line = file.readline()
Lst = []
print "START"
while line != "":
        rec = string.split(line,"\t")
        Ale_G1000 = string.split(rec[1],"/")
        if Ale_G1000[0] == "N" or Ale_G1000[0] == "NA":
                rec[4] = 0
        if Ale_G1000[1] == "N" or Ale_G1000[1] == "NA":
                rec[5] = 0
        Ale_Lab = string.split(rec[1],"/")
        if Ale_Lab[0] == "N" or Ale_Lab[0] == "NA":
                rec[6] = 0
        if Ale_Lab[1] == "N" or Ale_Lab[1] == "NA":
                rec[7] = 0
        obs = np.array([float(rec[4]),float(rec[5]),float(rec[6]),float(rec[7])])

        Exp_1 = Exp_2 = Exp_3 = Exp_4 = 0.0
        Exp_1 = (float(rec[4])+float(rec[5]))*(float(rec[4])+float(rec[6]))/(float(rec[4])+float(rec[5])+float(rec[6])+float(rec[7]))
        Exp_2 = (float(rec[5])+float(rec[7]))*(float(rec[4])+float(rec[5]))/(float(rec[4])+float(rec[5])+float(rec[6])+float(rec[7]))
        Exp_3 = (float(rec[4])+float(rec[6]))*(float(rec[6])+float(rec[7]))/(float(rec[4])+float(rec[5])+float(rec[6])+float(rec[7]))
        Exp_4 = (float(rec[5])+float(rec[7]))*(float(rec[6])+float(rec[7]))/(float(rec[4])+float(rec[5])+float(rec[6])+float(rec[7]))
        
        exp = np.array([float(Exp_1),float(Exp_2),float(Exp_3),float(Exp_4)])


#Fisher test
        cntrl = np.array([float(rec[4]),float(rec[5])])
        ards = np.array([float(rec[6]),float(rec[7])])

        Chi = scipy.stats.chisquare(obs,exp,2)
        Fish = scipy.stats.fisher_exact([cntrl,ards])

        newfile.write(rec[0] + "\t" + rec[1] + "\t" + rec[2] + "\t" + rec[3]\
                      + "\t" + `Chi[0]` + "\t" + `Chi[1]`\
                      + "\t" + `Fish[0]` + "\t" + `Fish[1]`)

        newfile.write("\n")
        line = file.readline()
      
newfile.close()
file.close()
print "END"

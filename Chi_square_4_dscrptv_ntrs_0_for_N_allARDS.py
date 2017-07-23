
LOCATION_INPUT = "U:/ARDS_SNPs_wes_vs_1000g/Chi_square_python/"
INPUT = "Cauc_Control_forX2.txt"


LOCATION_OUTPUT = "U:/ARDS_SNPs_wes_vs_1000g/Chi_square_python/"

OUTPUT_1 = "Cauc_ControlxEA_1000G_X2.txt"
OUTPUT_2 = "Cauc_ControlxEA_1000G_Not_Matched.txt"


#calculate chi square and fisher exact on the file with 4 descriptive
# entries and 4 data entries: Cntrl A, Cntrl B, Cndtn A, Cndtn B.
###################################################################

import scipy.stats
import numpy as np
from numpy import *
from array import *
import string

file = open(LOCATION_INPUT + INPUT,'r')#
newfile_1 = open(LOCATION_OUTPUT + OUTPUT_1,'w')
newfile_2 = open(LOCATION_OUTPUT + OUTPUT_2,'w')
line = file.readline()#title
rec = string.split(line,"\t")
newfile_1.write(rec[0] + "\t" + rec[1] + "\t" + rec[2] + "\t" + rec[3]\
                      + "\tX2" + "\tX2 P value\n")
line = file.readline()
Lst = []
print "START"
while line != "":
        rec = string.split(line,"\t")
        Check_for_N = 0
#working with the G100 SNPs
        Ale_G1000 = string.split(rec[1],"/")
        if Ale_G1000[0] == "N" or Ale_G1000[0] == "NA":
                rec[4] = 0
                Check_for_N = 1
        if Ale_G1000[1] == "N" or Ale_G1000[1] == "NA":
                rec[5] = 0
                Check_for_N = 1
#working with the lab SNPs
        Ale_Lab = string.split(rec[3],"/")
        if Ale_Lab[0] == "N" or Ale_Lab[0] == "NA":
                rec[6] = 0
                Check_for_N = 1
        if Ale_Lab[1] == "N" or Ale_Lab[1] == "NA":
                rec[7] = 0
                Check_for_N = 1

        if Check_for_N == 0:
                if rec[1] == rec[3]:
                        obs = np.array([float(rec[4]),float(rec[5]),float(rec[6]),float(rec[7])])
                        Exp_1 = Exp_2 = Exp_3 = Exp_4 = 0.0
                        Exp_1 = (float(rec[4])+float(rec[5]))*(float(rec[4])+float(rec[6]))/(float(rec[4])+float(rec[5])+float(rec[6])+float(rec[7]))
                        Exp_2 = (float(rec[5])+float(rec[7]))*(float(rec[4])+float(rec[5]))/(float(rec[4])+float(rec[5])+float(rec[6])+float(rec[7]))
                        Exp_3 = (float(rec[4])+float(rec[6]))*(float(rec[6])+float(rec[7]))/(float(rec[4])+float(rec[5])+float(rec[6])+float(rec[7]))
                        Exp_4 = (float(rec[5])+float(rec[7]))*(float(rec[6])+float(rec[7]))/(float(rec[4])+float(rec[5])+float(rec[6])+float(rec[7]))
                        
                        exp = np.array([float(Exp_1),float(Exp_2),float(Exp_3),float(Exp_4)])

                        Chi = scipy.stats.chisquare(obs,exp,2)


                        newfile_1.write(rec[0] + "\t" + rec[1] + "\t" + rec[2] + "\t" + rec[3]\
                                      + "\t" + `Chi[0]` + "\t" + `Chi[1]`)
                        newfile_1.write("\n")
                else: newfile_2.write(line)
        elif Check_for_N == 1:
                obs = np.array([float(rec[4]),float(rec[5]),float(rec[6]),float(rec[7])])
                Exp_1 = Exp_2 = Exp_3 = Exp_4 = 0.0
                Exp_1 = (float(rec[4])+float(rec[5]))*(float(rec[4])+float(rec[6]))/(float(rec[4])+float(rec[5])+float(rec[6])+float(rec[7]))
                Exp_2 = (float(rec[5])+float(rec[7]))*(float(rec[4])+float(rec[5]))/(float(rec[4])+float(rec[5])+float(rec[6])+float(rec[7]))
                Exp_3 = (float(rec[4])+float(rec[6]))*(float(rec[6])+float(rec[7]))/(float(rec[4])+float(rec[5])+float(rec[6])+float(rec[7]))
                Exp_4 = (float(rec[5])+float(rec[7]))*(float(rec[6])+float(rec[7]))/(float(rec[4])+float(rec[5])+float(rec[6])+float(rec[7]))
                
                exp = np.array([float(Exp_1),float(Exp_2),float(Exp_3),float(Exp_4)])

                Chi = scipy.stats.chisquare(obs,exp,2)


                newfile_1.write(rec[0] + "\t" + rec[1] + "\t" + rec[2] + "\t" + rec[3]\
                              + "\t" + `Chi[0]` + "\t" + `Chi[1]`)
                newfile_1.write("\n")
        line = file.readline()
      
newfile_1.close()
newfile_2.close()
file.close()
print "END"

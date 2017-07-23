

LOCATION_INPUT = "U:/ARDS_SNPs_wes_vs_1000g/Lab_samples_prcssd_txt/"
INPUT = "control.cauc.snps.snp_prcssd_new.txt"


LOCATION_OUTPUT = "U:/ARDS_SNPs_wes_vs_1000g/Lab_samples_prcssd_txt/"

OUTPUT = "control.cauc.snps.snp_prcssd_new_cntd.txt"



###################################################################

import string

file = open(LOCATION_INPUT + INPUT,'r')#VCF_tst.txt
print (LOCATION_INPUT + INPUT)#print filename
newfile = open(LOCATION_OUTPUT + OUTPUT,'w')

line = file.readline()
rec = string.split(line,"\t")

for i in range(1,len(rec)):
      newfile.write("N_" + string.strip(rec[i]) + "\t")
for i in range(1,len(rec)):
      if i < len(rec)-1:
            newfile.write("P_" + rec[i] + "\t")
      else: newfile.write("P_" + string.strip(rec[i]) + "\n")

      

line = file.readline()
rec = string.split(line,"\t")
Lst_N = Lst_P = []
for i in range(1,len(rec)):
      Lst_N = Lst_N + [0]
      Lst_P = Lst_P + [0]
     
while line != "":
      
      rec = string.split(line,"\t")
      for i in range(1,len(rec)):
            if string.strip(rec[i]) == "N/N":
                  Lst_N[i-1] = Lst_N[i-1] + 1
            else: Lst_P[i-1] = Lst_P[i-1] + 1
      line = file.readline()
print Lst_N, Lst_P
for i in range(len(Lst_N)):
      newfile.write(`Lst_N[i]` + "\t")
for i in range(len(Lst_P)):
      if i < len(Lst_P)-1:
            newfile.write(`Lst_P[i]` + "\t")
      else: newfile.write(`Lst_P[i]` + "\n")

newfile.close()
file.close()
print "END"


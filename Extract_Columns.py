

LOCATION_INPUT = "U:/Genome1000/"
INPUT = "chr_21_test.txt"


LOCATION_OUTPUT = "U:/Genome1000/"

OUTPUT = "chr_21_test_AA.txt"



###################################################################

Lst = ['NA19625','NA19700','NA19701','NA19702','NA19703','NA19704','NA19705','NA19707','NA19708','NA19711','NA19712','NA19713','NA19714','NA19818','NA19819','NA19828','NA19834','NA19835','NA19836','NA19900','NA19901','NA19902','NA19904','NA19905','NA19908','NA19909','NA19913','NA19914','NA19915','NA19916','NA19917','NA19918','NA19919','NA19920','NA19921','NA19922','NA19923','NA19924','NA19982','NA19983','NA19984','NA19985','NA20126','NA20127','NA20128','NA20129','NA20274','NA20276','NA20277','NA20278','NA20279','NA20281','NA20282','NA20284','NA20285','NA20287','NA20288','NA20289','NA20290','NA20291','NA20292','NA20294','NA20295','NA20296','NA20297','NA20298','NA20299','NA20300','NA20301','NA20302','NA20312','NA20313','NA20314','NA20316','NA20317','NA20318','NA20319','NA20320','NA20321','NA20322','NA20332','NA20333','NA20334','NA20335','NA20336','NA20337','NA20339','NA20340','NA20341','NA20342','NA20343','NA20344','NA20345','NA20346','NA20347','NA20348','NA20349','NA20350','NA20351','NA20355','NA20356','NA20357','NA20358','NA20359','NA20360','NA20361','NA20362','NA20363','NA20364','NA20412','NA20413','NA20414']
print Lst[2]


import string

file = open(LOCATION_INPUT + INPUT,'r')#VCF_tst.txt
newfile = open(LOCATION_OUTPUT + OUTPUT,'w')

line = file.readline()
L_in = L_out = 0
ACGT_lst = ['A','C','G','T']
while line != "":
      rec = string.split(line,"\t")
      
      if rec[0][1] == "#":
            line = file.readline()
            continue
      else:          
            if rec[0][0] == "#": # Title line
                  L_out = L_out +1
                  newfile.write("SNP_location" + "\t" + "SNP ID" + "\t" + "QC") #write SNP ID instead ofjust ID, 
                                                      #which will convert output to SYLK format
                  for i in range(9,len(rec)):
                        Smpl_ID = string.split(rec[i],".")
                        newfile.write("\t"+ string.strip(Smpl_ID[0]))
                  newfile.write("\t# of Samples" + "\tAA" + "\tCC" +"\tGG" + "\tTT"\
                                "\tA" +"\tC" + "\tG" + "\tT\n")
            else:
                  newfile.write(rec[0]+"_"+rec[1] +"\t"+ rec[2]+"\t"+rec[6]) #write SNP ID
                  REF = rec[3]
                  ALT = rec[4]
                  G_lst = []
                  for i in range(9,len(rec)):
                        GT_a = rec[i][0]
                        if GT_a == ".":
                              GT_a = "N"
                        elif GT_a == "0":
                              GT_a = REF
                        else: GT_a = ALT
                        GT_b = rec[i][2]
                        if GT_b == ".":
                              GT_b = "N"
                        elif GT_b == "0":
                              GT_b = REF
                        else: GT_b = ALT
                        lst = []
                        newfile.write("\t"+ GT_a +"/"+ GT_b)
                        G_lst = G_lst + [GT_a,GT_b]
                  
                  Nuc_lst = [0,0,0,0]
                  for i in range(len(G_lst)): #count allels
                        for j in range(len(Nuc_lst)):
                              if G_lst[i] == ACGT_lst[j]:#check for nucleotide
                                    Nuc_lst[j] = Nuc_lst[j] + 1
                                    break
                              
                  Hyp_lst = [0,0,0,0]
                  for i in range(0,len(G_lst),2): #count genotype, every two entries
                        if G_lst[i] == G_lst[i+1]:#check for homozygosity
                              for j in range(len(Hyp_lst)):
                                    if G_lst[i] == ACGT_lst[j]:#check for nucleotide
                                          Hyp_lst[j] = Hyp_lst[j] + 1
                                          break
                  newfile.write("\t" + `len(rec)-9`)                
                  for i in range(4):                 
                        newfile.write("\t" + `Hyp_lst[i]`)
                  for i in range(4):                 
                        newfile.write("\t" + `Nuc_lst[i]`)
                  newfile.write("\n")
                  

            
      line = file.readline()
newfile.close()
file.close()
print "END"


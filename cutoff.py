import re

#We discard the rare dual K assignments (≈1%) that Kofamscan generates for some genes and only retain the assignment with the highest score
#Depending on your use case, this might not be desirable
def insert_to_dic(KO_num, score):
    if KO_num not in ko_dic:
         out_dic[line[0]] = [KO_num, score]
    else:
        if float(score) > float(ko_dic[line[2]][0]):
            out_dic[line[0]] = [KO_num, score] 

out_dic = {}
ko_dic = {}

#ko_list from the KEGG goes here
with open("ko_list") as ko_list:
    for line in ko_list:
        line = line.split("\t")
        ko_dic[line[0]] = [line[1],line[2]]

#your own hmmsearch output goes here
with open(f"hmm_table.txt") as results:
    for line in results:
        if not line.startswith("#"):
            line = re.sub(' +', ' ', line)
            line = line.split(" ")

            if ko_dic[line[2]][1] == "full":
                if float(line[5]) >= float(ko_dic[line[2]][0]):
                    insert_to_dic(line[2],line[5])

            if ko_dic[line[2]][1] == "domain":
                if float(line[8]) >= float(ko_dic[line[2]][0]):             
                    insert_to_dic(line[2],line[8])
                        
real_ids = []

#The following is optional and sorts the output file in accordance with the input file
#With this, the final file is nearly identical to the Kofamscan script
with open(f"genes.faa") as faa_file:
    for line in faa_file:
        if line.startswith(">"):
            line = line.strip(">")
            line = line.strip("\n")
            real_ids.append(line)

with open(f"kofamscan_out.txt", "w") as filtered:
    for elem in real_ids:
            if str(elem) in out_dic:
                filtered.write(f"{elem}\t{out_dic[str(elem)][0]}\n")
            else:
                filtered.write(f"{elem}\n")

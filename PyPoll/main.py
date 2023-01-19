import os
import csv

csv_path=os.path.join('Resources', 'election_data.csv')

"""with open(csv_path, 'r') as f:
    lines = f.read()
    print(lines)
    print(type(lines))

""" 

#set dictionary
candidates={}

#variables
total_votes=0

#csv reader
with open(csv_path) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    #print(csvreader)
    csv_header=next(csvreader)
    #print(f'CSVHeader: {csv_header}')

    #Loop 
    for row in csvreader:
        total_votes= total_votes + 1
        new_candidate =row[2]
        if new_candidate in candidates:
            candidates.update ({new_candidate:candidates[new_candidate]+1})

        else:
            candidates.update({new_candidate:1})

winner= max(candidates,key=candidates.get)



#Loop 
for key,value in candidates.items():
   # print(key)
    #print(value)
    #print(round((value/total_votes)*100,3)
    ("{}: {}% ({})".format(key,round((value/total_votes)*100,3),value))


    
#output
output_text=(f"Election Results\n"
f"-----------------------\n"
f"Total Votes: {total_votes}\n"
f"-------------------------\n"
f"for key,value in candidates.items()\n"
f"# print(key)\n"
f"#print(value)\n"
f"#print(round((value/total_votes)*100,3)\n"

f"------------------------- \n"
f"Winner: {winner}\n"
f"-------------------------\n")



print(output_text)
output_path=os.path.join('analysis', 'Election Results.txt')
with open(output_path,"w") as text_out:
    text_out.write(output_text)
 





            


        










import os
import csv

csv_path=os.path.join('Resources', 'budget_data.csv')

"""with open(csv_path, 'r') as f:
    lines = f.read()
    print(lines)
    print(type(lines))
""" 
#setlists



#set values 
net_total = 0
total_months= 0
max_daily_increase=0
max_daily_decrease=0
max_increase_day= ""
max_decrease_day=""
last_day_total=0
daily_change=0
sum_change=0



#csv reader
with open(csv_path) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    #print(csvreader)
    csv_header=next(csvreader)
    #print(f'CSVHeader: {csv_header}')

    #totals 
    for row in csvreader:
        total_months = total_months +1
        net_total= net_total + int(row[1])
        daily_change = int(row[1]) - last_day_total
        last_day_total = int(row[1])
        sum_change = sum_change + daily_change
        #changes 
        if daily_change > 0:
            if  daily_change > max_daily_increase:
                max_daily_increase=  daily_change
                max_increase_day =row[0]

        else:
            if  daily_change < max_daily_decrease:
                max_daily_decrease=  daily_change
                max_decrease_day =row[0]

    #average 
    average_change = round(sum_change/total_months,2)



    

            


        







output_text=(f"Financial Analysis\n"
f"----------------------------\n"
f"Total Months: {total_months}\n"
f"Total: ${net_total}\n"
f"Average Change: ${average_change}\n"
f"Greatest Increase in Profits: {max_increase_day} (${max_daily_increase})\n"
f"Greatest Decrease in Profits: {max_decrease_day} (${max_daily_decrease})")


print(output_text)

output_path=os.path.join('analysis', 'budget_analysis.txt')
with open(output_path,"w") as text_out:
    text_out.write(output_text)






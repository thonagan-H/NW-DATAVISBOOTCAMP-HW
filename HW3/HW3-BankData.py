import csv
path_name = 'budget_data_1.csv'

with open(path_name,newline='')as csvfile:
  bd = csv.reader(csvfile,delimiter=',')
  print(csvfile)
  month_count = 0
  tot_rev = 0
  header = next(bd)
  lst =[]
  diff = 0
  diff_lst = []
  
  for i in bd:
    month_count += 1
    x = int(i[1])
    lst.append(x)
    tot_rev = tot_rev + x
  
  print(tot_rev)
  print(month_count)

  #Gives difference of list values
  for i in range(len(lst)-1):
    diff_lst.append(lst[i+1]-lst[i])
  sums = sum(diff_lst)
  average_rev = (abs(sums/len(diff_lst)))
  greatest = max(diff_lst)
  least = min(diff_lst)

with open("Bank_Data.txt",'w',encoding = 'utf-8') as f:
   f.write("Financial Analysis\n\n")
   f.write("----------------------------------------------\n\n")
   f.write("Total Months: "+ repr(month_count) +"\n")
   f.write("Total Revenue: "+ "$" + repr(tot_rev) + "\n")
   f.write("Average change in revenue: "+ "$" +  repr(average_rev) + "\n")
   f.write("Greatest increase in revenue: "+ "$" +  repr(greatest) + "\n")
   f.write("Greatest decrease in revenue: "+ "$" + repr(least) + "\n")
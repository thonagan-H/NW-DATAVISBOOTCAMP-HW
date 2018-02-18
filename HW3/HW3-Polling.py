from collections import Counter
import csv
path_name = 'election_data_2.csv'


with open(path_name,newline='')as csvfile:
  bd = csv.reader(csvfile,delimiter=',')
   
  vote_count = 0 
  next(bd) #skip header in loop
  cand_lst = []
  candidate = set() #sets store unique values
  ####################################################################
  
  #List of candidates and total vote count
  for i in bd:
    vote_count += 1
    cand_lst.append(i[2])
    candidate.add(i[2])
  
  candidates = list(candidate)
  print("The candidates are as follows:")
  for j in candidate:
    print(j)  #gives list of unique candidates 
  print ("\nThe total votes are " +str(vote_count))
  #####################################################################
  
  #Votes and % votes per candidate 

  #Counter gives the number of times a value appears in a list 
  #and returns a dictionary  
  unique_votes = Counter(cand_lst) 
  percent_votes = []
  individual_votes = []
  
  for key,value in unique_votes.items():
      #.items loops over a dictionary and returns the key value pairs
      individual_votes.append(str(value))
      percent_votes.append("%1.f"%((value/vote_count)*100))
      
      #print("The candidate "+key +" won "+ str(value) +" votes")
      #print("(" + str(percent_votes) + "%"+")") 
  print(candidates)
  z = max(percent_votes)
  print(z)
  winner = {candidates[0]:percent_votes[0],
            candidates[1]:percent_votes[1],
            candidates[2]:percent_votes[2],
            candidates[3]:percent_votes[3]}
  
  for keys,values in winner.items():
      if z == values:
          final_winner = keys
          print(final_winner)
##########################################################################  

#Writing to a file

with open("Election_results.txt",'w',encoding = 'utf-8') as f:
   f.write("Election Results: \n\n")
   f.write("----------------------------------------------\n")
   f.write("Total Votes: "+ repr(vote_count) +"\n")
   f.write("----------------------------------------------\n\n")
   f.write(candidates[0] + ": " + percent_votes[0] + "% " + "(" + individual_votes[0] + ")" + "\n")
   f.write(candidates[1] + ": " + percent_votes[1] + "% " + "(" + individual_votes[1] + ")" + "\n")
   f.write(candidates[2] + ": " + percent_votes[2] + "% " + "(" + individual_votes[2] + ")" + "\n")
   f.write(candidates[3] + ": " + percent_votes[3] + "% " + "(" + individual_votes[3] + ")" + "\n")
   f.write("----------------------------------------------\n\n")
   f.write("Winner: " + final_winner + "\n")
#Modules
import os
import csv

#to add in new candidates

csvpath = os.path.join( "election_data.csv")

# Set up the Dictionary with 0 votes for each of the candidates
Candidates = {}

def newcandidate(name):
    Candidates[row[2]] = 0
    
def results(name):
    print(str(name) + "  " +str(Candidates[name]/totvot*100)+ "% (" + str(Candidates[name]) +")")
    
def moreresults(name):
    electionresults.write(str(name) + "  " +str(Candidates[name]/totvot*100)+ "% (" + str(Candidates[name]) +")"+ "\n")


# open up the file and start reading row by row the votes 
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader,None)
    
    # for each row determine the name of who was voted for and then add another vote to that candidates total votes within the dictionary
    for row in csvreader:
        if row[2] not in Candidates:
            newcandidate(row[2])
        Candidates[row[2]] = Candidates[row[2]] +1
    
    totvot = sum(Candidates.values())
    
    
    # identify the winner from the maximum value within the dictionary pulling the index and calling them the winner
    winner = max(Candidates, key=Candidates.get)
    
    #output information to the terminal
    print("Election Results")
    print("-------------------")
    print("Total Votes: " + str(totvot))
    print("-------------------")
    for key in Candidates:
        results(key)
    print("-------------------")
    print("Winner: " + str(winner))
    print("-------------------")
    
    #output information to the text file
    electionresults = open("elec_results.txt","w")   
    electionresults.write("Election Results" + "\n")
    electionresults.write("-------------------" + "\n")
    electionresults.write("Total Votes: " + str(totvot) + "\n")
    electionresults.write("-------------------"+ "\n")
    for index in Candidates: 
        moreresults(index)
    electionresults.write("-------------------"+ "\n")
    electionresults.write("Winner: " + str(winner)+ "\n")
    electionresults.write("-------------------"+ "\n")
    electionresults.close()
# Modules
import os
import csv


#set all variables to 0 to ensure all calculations/lists are set up
totmon = 0
totnet = 0
largestincrease = 0
largestdecrease = 0
data = 0
olddata = 0
dayincrease = ""
daydecrease = ""
change = 0
allchange = []
average = 0

#Get the information from the csv file
csvpath = os.path.join( "budget_data.csv")
outpath = os.path.join("output_data.csv")

with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader,None)
    
    #complete calculations for each row in the csv and continue until end of file
    for row in csvreader:  
        totmon = totmon + 1
        data = int(row[1])
        totnet = totnet + data
        
        #Calculate the changes between each month and add them into the list to hold until final calculation
        change = data - olddata 
        allchange.append(change)
        
        #Determine whether the change made is the largest or the smallest ever
        if largestincrease < change:
            largestincrease = change
            dayincrease = row[0]
        if largestdecrease > change:
            largestdecrease = change
            daydecrease = row[0]
            
        #increment 'comparison' data to allow for comparison with the next datapoint
        olddata = data
        
    #get the total amount of change all added up, but remove the initial as it was wrong. 
    change = sum(allchange)-allchange[0]
    
    average = (change)/(totmon-1)
    
    #output to the terminal
    print ("Financial analysis")
    print ("---------------------")
    print ("Total Months: " + str(totmon))
    print ("Total: $" + str(totnet))
    print ("Average Change: $" + str(average))
    print ("Greatest Increase in Profits: " + dayincrease + " $" + str(largestincrease))
    print ("Greatest Decrease in Profits: " + daydecrease + " $" + str(largestdecrease))
    
    #output to the txt file
    
    
    bankanalysis = open("bank_analysis.txt","w")
    bankanalysis.write("Financial analysis" + "\n")
    bankanalysis.write ("---------------------"+ "\n")
    bankanalysis.write ("Total Months: " + str(totmon)+ "\n")
    bankanalysis.write ("Total: $" + str(totnet)+ "\n")
    bankanalysis.write ("Average Change: $" + str(average)+ "\n")
    bankanalysis.write ("Greatest Increase in Profits: " + dayincrease + " $" + str(largestincrease)+ "\n")
    bankanalysis.write ("Greatest Decrease in Profits: " + daydecrease + " $" + str(largestdecrease)+ "\n")
    bankanalysis.close()
    






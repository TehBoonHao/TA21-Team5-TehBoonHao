from pathlib import Path
import re, csv


#Create overhead function with the currency exchange rate
def overheadfunction(forex):
    #Create path with overhead csv file
    current_overheads = Path.cwd()/"csv_reports"/"overheads-day-90.csv"
    #Create an empty list to append with the data
    overhead_list = []
    #Open file in a read mode 
    with current_overheads.open(mode = "r",encoding = "utf-8-sig", newline="") as file:
        #Use csv reader to read file
        reader = csv.reader(file)
        #Use `next()` to skip the header.
        next(reader)
        #Create a for loop for iterating over a sequence
        for row in reader:
            #Convert the overhead data into float and multiply with the currency exchange rate
            np = float(row[1])*forex
            #Use pair to fit the overhead category and data
            pair = (row[0], np)
            #Append the pair into overhead list
            overhead_list.append(pair)
        #Extract the overhead category into overhead 
        overresult = overhead_list[0]
        #Find out the len to iterate over the list
        for i in range(1,len(overhead_list)): 
            #Find the largest overhead data
            if (overhead_list[i][1] > overresult[1]):
                #The result will save into overresult
                overresult = overhead_list[i]
    
    #Create a path to summary_report.txt
    current = Path.cwd()/"summary_report.txt"
    #Create the summary_report.txt
    current.touch()

    #Open the file in append mode
    with current.open(mode="a", encoding = "UTF-8", newline = "") as file:
        #Extract the overhead category from the result and put into category
        category = overresult[0]
        #Extract the overhead data into the amount and round off to 2 decimal place
        amount = str(round(overresult[1],2))
        msg = "[HIGHEST OVERHEADS]" + category + ": SGD$" + amount +'\n'
        #Write the highest overhead category and amount into the summary_report.txt
        file.write(msg)


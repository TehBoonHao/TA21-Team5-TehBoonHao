from pathlib import Path
import re, csv


#Create a function for profit and loss with the currency exchange rate
def profit_loss_function(forex):
    #Create a path to the cash on hand csv file
    profitloss = Path.cwd()/"csv_reports"/"profit-and-loss-usd.csv"
    #Create an empty list to store data
    pl_list = []
    #Open the csv file and read the data 
    with profitloss.open(mode = "r",encoding = "utf-8-sig", newline="") as file:
        #Use the csv reader to read the csv file
        reader = csv.reader(file)
        #Skip the header
        next(reader)
        #Create a for loop for itering over the value in csv file
        for row in reader:
            #np to convert net profit value into float and times the currency exchange rate
            np = float(row[4])*forex
            #Pair is to fit the day and the net profit value
            pair = (row[0], np)
            #Append the data into the empty list 
            pl_list.append(pair)
        #create empty list for append purposes
        plresult = []
        #This is to compare the value within the list
        #find out the len to iterating over the list
        for i in range(1,len(pl_list)): 
            #If next day amount is higher than the previous day
            if (pl_list[i][1] < pl_list[i-1][1]):
                #Append the data of day and net profit from the list
                plresult.append(pl_list[i])

    #create a path to summary_report.txt
    current = Path.cwd()/"summary_report.txt"
    #Create the summary_report.txt
    current.touch()
    #Open the summary_report.txt in append mode
    with current.open(mode="a", encoding = "UTF-8", newline = "") as file:
        #if the result equal to none, it will show [Net profit Surplus] Net Profit on each day is higher than the previous day
        if len(plresult) == 0:
            file.write("[NET PROFIT SURPLUS] Net profit on each day is higher than the previous day\n")
        #If the result show there is deficit in net profit, it will show the day and amount in the deficit day
        else:
            #create a for loop for iterating over the value in plresult 
            for x in plresult:
                #Extract the day data then put in day
                day = x[0]
                # extract the net profit data in string and round into 2 decimal place, then put into amount
                amount = str(round(x[1],2))
                msg = "[PROFIT DEFICIT] DAY:" + day + ",AMOUNT: SGD" + amount +'\n'
                #write the profit deficit day and amount and append into the summary_report.txt
                file.write(msg)

from pathlib import Path
import re, csv


# create a function for cash on hand calculate with the forex exchange rate
def coh_function(forex):
    # create a path to the cash on hand csv file
    coh = Path.cwd()/"csv_reports"/"cash-on-hand-usd.csv"
    # create a empty list for append purpose
    coh_list = []
    # open the csv file and read
    with coh.open(mode = "r",encoding = "utf-8-sig", newline="") as file:
        # use the csv reader to read the csv file
        reader = csv.reader(file)
        # skip the header
        next(reader)
        # create a for loop for iterating over the value in csv file
        for row in reader:
            # np is to convert cash on hand value into float and times the currency exchange rate 
            np = float(row[1])*forex
            # pair is to fit the day and cash on hand
            pair = (row[0], np)
            # append day and cash on hand into the coh_list
            coh_list.append(pair)
        # create a empty list for append purpose
        cohresult = []
        # this is to compare the the value within the list
        # find out the len to iterating over the list
        for i in range(1,len(coh_list)): 
            # if next day amount is higher than the previous day
            if (coh_list[i][1] < coh_list[i-1][1]):
                # append the data of day and cash of hand from the list
                cohresult.append(coh_list[i])

    # create a path to summary_report.txt    
    current = Path.cwd()/"summary_report.txt"
    # create the summary_report.txt
    current.touch()
    # open the summary_report.txt in append mode
    with current.open(mode="a", encoding = "UTF-8", newline = "") as file:
        # if the result equal to none, it will show [CASH SURPLUS] Net profit on each day is higher than the previous day
        if len(cohresult) == 0:
            file.write("[CASH SURPLUS] Net profit on each day is higher than the previous day\n")
        # if the result show there is deficit in cash, it will show the day and amount in the deficit day
        else:
            # create a for loop for iterating over the value in cohresult
            for y in cohresult:
                # extract the day data then put in o day
                day = y[0]
                # extract the cash on hand data in string and round into 2 decimal place, then put into amount
                amount = str(round(y[1],2))
                msg = "[CASH DEFICIT] DAY:" + day + ",AMOUNT: SGD" + amount +'\n'
                # write the cash deficit day and amount and append into summary report.txt
                file.write(msg)

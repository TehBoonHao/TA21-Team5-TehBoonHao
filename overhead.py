from pathlib import Path
import re, csv



def overheadfunction(forex):
    current_overheads = Path.cwd()/"csv_reports"/"overheads-day-90.csv"
    overhead_list = []
    with current_overheads.open(mode = "r",encoding = "utf-8-sig", newline="") as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            np = float(row[1])*forex
            pair = (row[0], np)
            overhead_list.append(pair)
        overresult = overhead_list[0]
        for i in range(1,len(overhead_list)): 
            if (overhead_list[i][1] > overresult[1]):
                overresult = overhead_list[i]
    
    current = Path.cwd()/"summary_report.txt"
    current.touch()
    with current.open(mode="a", encoding = "UTF-8", newline = "") as file:
        category = overresult[0]
        amount = str(round(overresult[1],2))
        msg = "[HIGHEST OVERHEADS]" + category + ": SGD$" + amount +'\n'
        file.write(msg)

import csv
import pandas as pd
from pathNames import file2022S1, outputS1

def modeFile(dataPath, examType):
    data = pd.read_csv(dataPath)
    data.sort_values(['SECTION'],axis = 0, inplace = True)

    data = data[['MT LT', 'FE LT']].dropna()
    mode_dict = {}
    if examType == "FE":
        rowSearch = 'FE LT'
    elif examType == "MT":
        rowSearch = 'ME LT'
    else: 
        print("Enter MT for midterm, FE for final")
        exit()
    for index, row in data.iterrows():
        modes = row[rowSearch]
        mode = modes.split("; ")
        for lt in mode:
            if lt in mode_dict:
                mode_dict[lt]+=1
            else:
                mode_dict[lt] = 1
    return mode_dict

def fileWrite(outputPath, dataDict):  
    with open(outputPath, 'w', newline='' ) as file:
        writer = csv.writer(file)
        field = ["LT", "Count"]
        writer.writerow(field)
        for title, count in dataDict.items():
            writer.writerow([title,count])


dict1 = modeFile(file2022S1,"FE")

fileWrite(outputS1, dict1)

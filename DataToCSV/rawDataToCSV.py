import pandas as pd
import numpy as np
import os
import re
import time

from datetime import datetime, timedelta, date

import rawDataToCSVAuxFunctions as daux
import searchStringsToCSV as st
import stringsForModifiers as st_modifiers

def save_dataframe_to_csv(df):
    today = "10-07-2023" # datetime.date.today()
    csv_file_name = f"{st_modifiers.dataSet_dir_path}dataSet{today}x{time.time()}.csv"
    df.to_csv(csv_file_name)

def printExecutionTime(start):
    # Grab Currrent Time After Running the Code
    end = time.time()
    total_time = end - start
    print("\nCode Execution took " + str(total_time))


def modifyData(index, tmpString):
    if index in {0, 6, *range(8, 14), *range(15, 17), *range(18, 28), 33}:
        modifiedString = daux.extractNumbers(tmpString)
        if re.match(r'^-?\d+(?:\.\d+)?$', modifiedString):
            modifiedString = int(modifiedString)
        else:
            print("the string is not int, but is: " + tmpString + " and the index is: " + str(index))

    elif (index == 1):
        gush, helka = daux.separateString(tmpString, "-")
        modifiedString = int(gush)
    elif (index == 2):
        gush, helka = daux.separateString(tmpString, "-")
        modifiedString = int(daux.extractNumbers(helka))
    elif (index == 3):
        modifiedString = int(daux.transformDateToNumber(tmpString))
    elif (index == 7): #Entrance
        modifiedString = int("0")
    elif (index == 14):
        modifiedString = float(tmpString)
    elif (index == 17):
        modifiedString = int(daux.modifyFloorNumber(tmpString))
    elif (index == 29):
        modifiedString = daux.modifyDealType(tmpString)
    elif (index == 30):
        modifiedString = daux.modifyFunctionOfBuilding(tmpString)
    elif (index == 31):
        modifiedString = daux.modifyFunctionOfUnit(tmpString)
    elif (index == 32):
        modifiedString = float(daux.modifyShuma(tmpString))
    elif (index == 34):
        modifiedString = int(daux.modifyTava(tmpString))
    elif (index == 35):
        modifiedString = daux.modifyNatureOfRights(tmpString)
    else:
        if index not in {4, 5, 28}:
            print(f"the index is: {str(index)}, but none of the {len(st.termsToSearch)} cases worked for the string: {tmpString}")
        modifiedString = tmpString

    return modifiedString


def process_property(dir_path, file, maxFlatsToProcess = 100000):
    file_path = dir_path + file

    with open(file_path, "r") as f:
        for line in f.readlines():
            if line.find("פרטי קרקע") > 0:
                break
            for index in range(len(indexList)):
                indexList[index] = line.find(st.termsToSearch[index])
                if 0 < fileNumber < maxFlatsToProcess:
                    if indexList[index] > 0:
                        tmpString = line[line.find(">") + 1:line.find("</span>")]
                        modifiedString = modifyData(index, tmpString)
                        newCSV[index].append(modifiedString)


if __name__ == '__main__':
    print("starting")
    start = time.time()

    dir_path = st_modifiers.rawData_dir_path
    files = daux.getFilesInFolder(dir_path)

    indexList = [0] * (len(st.termsToSearch))

    newCSV = st.foundTermsList

    fileNumber=1

    for file in files: # in dir_path
        process_property(dir_path, file)
        fileNumber+=1

    df = pd.DataFrame(newCSV).transpose()
    column_names = df.iloc[0]
    df.columns = column_names
    df = df[1:]
    df = df.reset_index(drop=True)

    save_dataframe_to_csv(df)

    printExecutionTime(start)
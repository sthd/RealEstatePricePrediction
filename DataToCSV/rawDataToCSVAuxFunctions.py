import re
from datetime import datetime, timedelta
import os
import stringsForModifiers as st_modifiers

def keepNumbersOnly(string):
    number = re.sub(r'\D', '', string)
    return number

def modifyDefaultCases(unmodifiedString, feature):
    if (unmodifiedString == "--"):
        modifiedString = "Not Applicable"
    elif (len(unmodifiedString) == 0): # i.e. it is null
        modifiedString = "Invalid"
    else:
        modifiedString = ""
        print("The unmodified string of " + feature + " is: " + unmodifiedString + " and we assigned as NULL")
    return modifiedString

def modifyFloorNumber(unmodifiedString):
    if (unmodifiedString == "קומת קרקע"):
        modifiedString = 0
    elif (re.match(r'^-?\d+(?:\.\d+)?$', unmodifiedString)):
        modifiedString = float(unmodifiedString)
    else:
        modifiedString = modifyDefaultCases(unmodifiedString, "Floor Number")
    return modifiedString


def modifyDealType(unmodifiedString):
    if unmodifiedString in st_modifiers.DealType_mappings:
        modifiedString = st_modifiers.DealType_mappings[unmodifiedString]
    else:
        modifiedString = modifyDefaultCases(unmodifiedString, "Deal Type")
    return modifiedString


def modifyFunctionOfBuilding(unmodifiedString):
    if unmodifiedString in st_modifiers.FunctionOfBuilding_mappings:
        modifiedString = st_modifiers.FunctionOfBuilding_mappings[unmodifiedString]
    else:
        modifiedString = modifyDefaultCases(unmodifiedString, "Function of Building")
    return modifiedString


def modifyFunctionOfUnit(unmodifiedString):
    if unmodifiedString in st_modifiers.FunctionOfUnit_mappings:
        modifiedString = st_modifiers.FunctionOfUnit_mappings[unmodifiedString]
    else:
        modifiedString = modifyDefaultCases(unmodifiedString, "Function of Unit")

    return modifiedString


    #elif (re.match(r'^-?\d+(?:\.\d+)?$', unmodifiedString)):
    #    modifiedString = float(unmodifiedString)

def modifyShuma(unmodifiedString):
    modifiedString = unmodifiedString.replace("ליחידה בשלמותה", "")
    modifiedString = modifiedString.replace("בלתי מסוימים", "")
    modifiedString = modifiedString.replace("ג", "")
    num1, num2 = separateString(modifiedString, "/")
    num1 = keepNumbersOnly(num1)
    num2 = keepNumbersOnly(num2)
    #check if m1, m2 are numbers and not 0
    if (num1.isnumeric() and num2.isnumeric()):
        minimum = min(int(num1), int(num2))
        maximum = max(int(num1), int(num2))
        if ((minimum != 0) and (maximum != 0)):
            modifiedString = float(minimum / maximum)
    else:
        #modifiedString = -1
        modifiedString = modifyDefaultCases(unmodifiedString, "Shuma")
    #print("min is: " + str(minimum) + "  and max is: " + str(maximum) + " and product is: " + str(modifiedString))
    return modifiedString


def modifyNatureOfRights(unmodifiedString):
    if unmodifiedString in st_modifiers.NatureOfRights_mappings:
        modifiedString = st_modifiers.NatureOfRights_mappings[unmodifiedString]
    else:
        modifiedString = modifyDefaultCases(unmodifiedString, "Nature Of Rights")
    return modifiedString



def modifyTava(unmodifiedString):
    if (unmodifiedString == "--"):
        modifiedString = int("-1")
    elif (unmodifiedString.isnumeric() ):
        modifiedString = int(unmodifiedString)
    else:
        modifyDefaultCases(unmodifiedString, "Tava")
    return modifiedString



def modifyNumberOfRooms(unmodifiedString):
    if (unmodifiedString.isnumeric()):
        modifiedString = float(unmodifiedString)
    elif (unmodifiedString == "קומת קרקע"): ##check if makes sensse
        modifiedString = float("0")
    else:
        modifiedString = modifyDefaultCases(unmodifiedString, "Number of Rooms")
    return modifiedString




def transformDateToNumber(date):
    # Convert the date string to a datetime object
    dateObj = datetime.strptime(date, '%d/%m/%Y')

    # Define the base date used by Excel (January 1, 1900)
    baseDate = datetime(1900, 1, 1)

    # Calculate the number of days between the date and the base date
    delta = dateObj - baseDate
    excelNumber = delta.days + 2

    return excelNumber

def extractNumbers(string):
    # Use regular expression to match all numbers in the string
    numbers = re.findall(r'\d+', string)

    # Join the extracted numbers into a single string
    result = ''.join(numbers)

    return result


def separateString(string, delimeter):
    # Split the string using the delimiter "-"
    parts = string.split(delimeter)

    # Ensure that the string contains at least one delimiter
    if len(parts) >= 2:
        firstPart = parts[0]
        secondPart = "-".join(parts[1:])
        return firstPart, secondPart
    else:
        return None, None

def getFilesInFolder(dir_path):
    res = []
    for path in os.listdir(dir_path):
        # check if current path is a file
        if os.path.isfile(os.path.join(dir_path, path)):
            if (path[-4:] == 'flat'):
                res.append(path)
    return res





def modifyFloorNumber2(unmodifiedString):
    if re.match(r'^-?\d+(?:\.\d+)?$', unmodifiedString):
        modifiedString = int(unmodifiedString)
    else:
        modifiedString = 0
        print("modified floor is: " + str(modifiedString))
    return modifiedString

def modifyNumberOfRooms2(unmodifiedString):
    if (unmodifiedString == "קומת קרקע"):
        modifiedString = float("0")
    elif (re.match(r'^-?\d+(?:\.\d+)?$', unmodifiedString)):
        modifiedString = float(unmodifiedString)
    else:
        modifiedString = ""
    return modifiedString

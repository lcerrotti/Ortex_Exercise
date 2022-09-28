import csv
from datetime import datetime
import string

# Formate Functions
# We create a function to convert the string to a datetime object
def separateDatestr(date):


    date = list(date)
    year = date[0]+date[1]+date[2]+date[3]
    month = date[4]+date[5]
    day = date[6]+date[7]

    return year,month,day


#--------------------------------------------------------------------------------------------------------------#


def string_to_int(s):


    try:
        temp = int(eval(str(s)))
        if type(temp) == int:
            return temp
    except:
        return


#--------------------------------------------------------------------------------------------------------------#


# Returns the header element with the most occurrences in the csv file
def maximum_results(header_search,offchangeYN):


    # The list is completed with all the elements of the key selected in the function
    statistics = []
    if offchangeYN == 0:

        with open('2017.csv', newline='', encoding="utf8") as File:   # We open the csv file with the Excel dialect to interpret the first line as header or key 
         reader = csv.DictReader(File, dialect='excel')    
         for key in reader:
            if key[header_search] != "off exchange":
                statistics.append(key[header_search])
    elif offchangeYN == 1:

        with open('2017.csv', newline='', encoding="utf8") as File:   # We open the csv file with the Excel dialect to interpret the first line as header or key 
         reader = csv.DictReader(File, dialect='excel')    
         for key in reader:
            statistics.append(key[header_search])
    else:
        return "missing offchange option"
    

    
    return max(set(statistics), key=statistics.count) # We return the most repeated value in the statistics list
        

#print(maximum_results("exchange",0))



#--------------------------------------------------------------------------------------------------------------#



def getmaxincomeEUR(year1,month1):


    # We open the csv file with the Excel dialect to interpret the first line as header or key
    companyName = []
    trade_EUR = []

    with open('2017.csv', newline='', encoding="utf8") as File:   
     reader = csv.DictReader(File, dialect='excel')   
     for key in reader:
        year = separateDatestr(key["tradedate"])[0]
        month = separateDatestr(key["tradedate"])[1]   
        if year == year1 and month == month1:
            companyName.append(key["companyName"])
            trade_EUR.append(key["valueEUR"])
        else:
            continue
    
    if companyName == []:
        return "The selected year or month is not in the file"
    else:
        companyNameset = set(companyName) # We create a set with the company name
        companyNamelist = list(companyNameset) # We create a list with the company name


        companyValues = [] # We create a list with the company value
        individualValues = [] # We create a list with the individual value

        
        for cN in companyNamelist:
            pos = [i for i in range(len(companyName)) if companyName[i]== cN] 
            euros = []
            
            companyValues.append(cN)

            for p in pos:
                euro = float(trade_EUR[p]) #Float
                #euro = trade_EUR[s].translate(str.maketrans('', '', string.punctuation)) # We remove the punctuation
                euros.append(int(euro))
                
            companyValues.append(sum(euros))    
            individualValues.append(sum(euros))

            maxValue = max(individualValues)    
        
        for cV in companyValues:
            if cV == maxValue:
                return companyValues[companyValues.index(cV) - 1] , maxValue
    

#--------------------------------------------------------------------------------------------------------------#

def tradeSignificate(year1):


    dictofMonths = {"01":"January", "02":"February", "03":"March",
     "04":"April", "05":"May", "06":"June", "07":"July", "08":"August",
      "09":"September", "10":"October", "11":"November", "12":"December"}

    tradesInMonth = []
    tradesInYear = []
    for month1 in dictofMonths:
        
        with open('2017.csv', newline='', encoding="utf8") as File:   
         reader = csv.DictReader(File, dialect='excel')   
         for key in reader:
            year = separateDatestr(key["tradedate"])[0]
            month = separateDatestr(key["tradedate"])[1] 
            if year == year1:
                if key["tradeSignificance"] == "3":
                    tradesInYear.append(key["tradeSignificance"])
                    if month == month1:
                        tradesInMonth.append(key["tradeSignificance"])
        
        percentage = (len(tradesInMonth)/len(tradesInYear))*100
        print(dictofMonths[month1], ":", percentage.__format__("0.2f"),"%")
        


#--------------------------------------------------------------------------------------------------------------#
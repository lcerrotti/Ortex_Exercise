from datetime import datetime

#import calendar
'''
This task is to fix this code to write out a simple monthly report. The report should look professional.
The aim of the exercise is to:
- Ensure that the code works as specified including date formats
- Make sure the code will work correctly for any month
- Make sure the code is efficient
- Ensure adherence to PEP-8 and good coding standards for readability
- No need to add comments unless you wish to
- No need to add features to improve the output, but it should be sensible given the constraints of the exercise.
Code should display a dummy sales report
'''
### Do not change anything in the section below, it is just setting up some sample data
# test_data is a dictionary keyed on day number containing the date and sales figures for that day
month = "02"
test_data = {f"{x}": {"date": datetime.strptime(f"2021{month}{x:02d}", "%Y%m%d"),
                      'sales': float(x ** 2 / 7)} for x in range(1, 29)}
### Do not change anything in the section above, it is just setting up some sample data

'''
In order to include the rest of the months, we must enlarge the 
range of the "test_data" dictionary in order to generate new 
values and days to iterate.In the case of being able to modify 
"test_data" it is convenient to use the automatic parameters 
that you add below to establish the start and end
'''

## --- Automatic date range calculation --- ###
'''
monthRange = calendar.monthrange(2021, int(month))
#start=test_data[str(monthRange[0]+1)]
#end=test_data[str(monthRange[1])]
'''
### --- Automatic date range calculation --- ###

start=test_data["1"]
end=test_data["28"]


def DateToDisplayDate(date):  # E.g. Monday 8th February, 2021
    
    
 return (f"""{date.strftime("%a")} {date.strftime("%d")}th\
{date.strftime("%B")}, {date.strftime("%Y")}""")


#monthRange = calendar.monthrange(2021, int(month))
#for i in range(1,monthRange[1]):
for i in range(1,28):
    start=test_data[f"{i}"]
    start["date"]=DateToDisplayDate(start["date"])
end=test_data[f"{i+1}"]       
end["date"]=DateToDisplayDate(end["date"])


print("\n--------------Sales Report----------------\n",
"Report start date: " + start["date"] + "\n",
"Starting value: " + str(start["sales"]) + "\n",
"Report end date: " + end["date"] + "\n",
"Total sales: " + str(end["sales"]) + "\n")

total = 0
for k, v in test_data.items():


    if test_data[k]["date"] == "02" and k == "29":
         print("Leap year")


    print(f"""Date: {test_data[k]["date"]}\
    Sales: {test_data[k]["sales"].__format__("0.2f")}\
    Month to Date: {total + (test_data[k]["sales"])}""")

    total = total + test_data[k]["sales"]

print(f"\nTotal sales for the month: {total}\n")








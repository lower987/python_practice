year = int(input("A) What year is it? "))
month = input("B) What month is it? ").capitalize()
if month == "January":
    days = 0
if month == "February":
    days = 31
if month == "March":
    days = 59
if month  == "April":
    days = 90
if month == "May":
    days = 120
if month == "june":
    days = 151
if month == "July":
    days = 181
if month == "August":
    days = 212
if month == "September":
    days = 243
if month == "October":
    days = 273
if month == "November":
    days = 304
if month == "December":
    days = 334
day = int(input("C) What is the number of the day? "))
print(f"There is a {((days + day)*100/365):.4f} percentage completed of {year}.")
print("End for now")
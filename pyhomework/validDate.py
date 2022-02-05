# Valid Date 
# Ishai Masada
from ListofDates import *

def valid_date():
    Result = ""
    dates = ListofDates()
    for date in dates:
        if (len(date) == 10) and (int(date[-4]+date[-3]+date[-2]+date[-1]) in range(1, 2501)) and (int(date[3]+date[4]) in range(1, 13)):
            Result += "-"
        else:
            Result += date[1]
    print(f'Result: {Result}')

valid_date()

#This is a function to generate test data for the program to validate dates

def ListofDates():
    DateList = []
    for mon in range (1,13):
        Yr,Feb = 2001,0
        if (mon == 2):
            Feb = 2
            if Yr%400==0 or Yr%100!=0 and Yr%4==0:  # if leap year, make Feb subtract one less day
                Feb = 1
        MonSt = "{0:0>2}".format(mon)
        DateList = DateList + [MonSt +"/00/"+str(Yr)] + [MonSt +"/01/"+str(Yr)]
        ShortMon = (mon-1)%7%2 # Equals 1 or 30 (or less) day months and 0 for 31 day months
        MaxDay = 31 - ShortMon - Feb
        DateList = DateList + [MonSt +"/"+ str(MaxDay+1) +"/"+ str(Yr)] + [MonSt +"/"+ str(MaxDay) +"/"+str(Yr)]
    DateList = DateList + ["02/29/1900"] + ["02/29/2000"]
    DateList = DateList + ["00/29/2000"] + ["02/29/2400"]
    DateList = DateList + ["13/29/2000"] + ["12/31/2500"]
    DateList = DateList + ["01/01/2501"] + ["02/28/0001"]
    DateList = DateList + ["02/28/0000"] + ["02/29/400"]
    return (DateList)   


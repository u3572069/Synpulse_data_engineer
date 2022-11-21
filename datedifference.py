
 
 
 
 

monthDays = [31, 28, 31, 30, 31, 30,
             31, 31, 30, 31, 30, 31]
 
 
def countLeapYears(d):
 
    years = d[2]
 
    if (d[1] <= 2):
        years -= 1
 
    return int(years / 4) - int(years / 100) + int(years / 400)
 
 

def getDifference(l1, l2):

    n1 = l1[2]* 365 + l1[0]
 
    # Add days for months in given date
    for i in range(0, l1[1] - 1):
        n1 += monthDays[i]
 
    # Since every leap year is of 366 days,
    # Add a day for every leap year
    n1 += countLeapYears(l1)
 
    n2 = l2[2] * 365 + l2[0]
    for i in range(0, l2[1] - 1):
        n2 += monthDays[i]
    n2 += countLeapYears(l2)
 
    return (n2 - n1-1)
 
 
# Driver program
# 02/06/1983 - 22/06/1983   04/07/1984 - 25/12/1984 = 173 days
d1 = input()
d2 = input()
l1 = list(map(int, d1.split("/")))
l2 = list(map(int, d2.split("/")))
 
print(getDifference(l1, l2), "days")
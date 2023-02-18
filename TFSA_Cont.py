import math

def TFSA():
    limit = [5000, 5000, 5000, 5000, 5500, 5500, 1000, 5500, 5500, 5500, 6000, 6000, 6000, 6000, 6500]
    year = [2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023]
    age = int(input("Age: ")) 
    if (age < 18):
        print("Too young to invest")
    if (age > len(limit) + 18):
        acc = sum(limit)
        print(f'${acc:,d}')
        return 0
    age = age - 18
    acc = 0 
    for i in range(int((len(limit)) - age - 1), len(limit)):
        acc += limit[i]
    print(f'${acc:,d}')

# Dates
# Students Loans
# RetireBy
def Milli():
    target = 1000000
    pv = int(input("Present Value($): "))
    i = float(input("Interest(%): "))/100
    pmt = int(input("Contributions($): ")) * -1

    count = 0
    for x in range(100):
        count += 1
        fv = FutureValue(pv, i, count, pmt)
        interest = InterestFutureValue(pv, i, count, pmt)
        if (fv > target):
            print("It will take you " + str(count) + "yrs to make your first million.")
            print("Millionaire by the age of " + str(count+18))
            print(interest)
            break

# ADVANCE Fv
def FutureValue(pv, i, n, pmt):
    
    for x in range(1,n+1):
        p_i= pv * i
        fv = pv + p_i - pmt
        pv = fv
    return(fv)
    
def InterestFutureValue(pv, i, n, pmt):
    sum = -pv
    for y in range(1, n+1):
        print(sum)
        sum += pmt
    return(-1*sum)

Milli()




# def compunt_interest(principal, rate, time):
#         amount = principal * (pow((1 + rate / 100), time))
#         CI = Amount  - principal
#         print ("Compund inerest is"

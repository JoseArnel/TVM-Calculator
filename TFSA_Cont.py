import math
# created 2009 
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
    pv = int(input("Present Value($): "))
    i = float(input("Interest(%): "))/100
    # n = int(input("Number of Periods: "))
    pmt = int(input("Payment($): ")) * -1
    target = 1000000

    count = 0
    # CHECK ON LOOOOP
    for x in range(100):
        count += 1
        fv = FutureValue(pv, i, count, pmt)
        print(fv)
        if (fv > target):
            print(count)
            break

    # for x in range(10):
    #     i = x
    #     print(i)

    # # save = input("Would you like to save the values? (y/n) ")
    # n = math.log(fv / pv) / math.log(1 + i)
    # print("Goal " + str(fv))
    # print("Number of Years: {:.3f}".format(n))

def FutureValue(pv, i, n, pmt):
    for x in range(1,n+1):
        p_i= pv * i
        fv = pv + p_i - pmt
        pv = fv
    # print("Future Value = ${:.2f}".format(fv))
    return(fv)

Milli()
# def compunt_interest(principal, rate, time):
#         amount = principal * (pow((1 + rate / 100), time))
#         CI = Amount  - principal
#         print ("Compund inerest is"


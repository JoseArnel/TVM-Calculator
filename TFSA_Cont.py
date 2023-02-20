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
    calc = input("Would you like to show the calculations (y/n)")

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
    principal_s = pv 
    balance_s = pv 
    principal_e = pv
    
    for x in range(1,n+1):
        p_i= pv * i
        fv = pv + p_i - pmt
        principal_e = principal_s - pmt
        print("start_principal " + " start_balance" +   " interest " + " end_balance " + " end_principal ")
        print("{:.2f}".format(principal_s) +  "        " + "{:.2f}".format(balance_s) +  "     " + "{:.2f}".format(p_i)  + "  " + "{:.2f}".format(fv) +  "    " + "{:.2f}".format(principal_e))
        # print("principal:{:.2f}".format(principal_s) + "start balance::{:.2f}".format(balance_s) +   " interest:{:.2f}".format(p_i) + "end balance:{:.2f}".format(fv) + "end balance:{:.2f}".format(principal_e))
        principal_s = principal_s - pmt
        balance_s = fv
        pv = fv
    # print("start principle start balance, interest, end balance, end principal")

    # ("Future Value: {:.3f} \n".format(fv))
    return(fv)
    
def InterestFutureValue(pv, i, n, pmt):
    sum = -pv
    for y in range(1, n+1):
        print(sum)
        sum += pmt
    return(-1*sum)


FutureValue(50000, 0.07, 31, -6000)





# def compunt_interest(principal, rate, time):
#         amount = principal * (pow((1 + rate / 100), time))
#         CI = Amount  - principal
#         print ("Compund inerest is"

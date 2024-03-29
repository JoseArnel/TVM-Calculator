import math
import csv
import numpy as np
import datetime 
import pandas as pd
from matplotlib import pyplot as plt
from os import system, name

####
# main screan, TVM Calculator / Other Financial Calc 
# Display Screen, Terminal Based, Display Graphs, Can save as CSV, and 
# Extra Tools: Millionare, before ..., TFSA Calculations, Interest
# Implement Calculators, Interest, TVM, Investment  
#### 

## Check List
# Implement Charts, Expand, Clean up

def clear():
    _ = system('clear')

def date():
    return (str(datetime.date.today()))

def txtClear():
    resultsTxt = open("results.txt", "r+") 
    resultsTxt.truncate(0)
    resultsTxt.close()

def tvm_visualizer():
    choice = str(input("Would you like to show the values? (y/n) "))
    if (choice == 'y'):
        data = pd.read_csv('tvm_graph.csv')
        plt.plot(data.PV / 10**6)
        plt.plot(data.SumofPMT / 10**6)
        plt.plot(data.AccumulatedInterest / 10**6)
        plt.plot(data.FV / 10**6)
        plt.legend(['PV', 'SumofPMT', 'AccumulatedInterest', 'FV'])
        plt.xlabel('Year')
        plt.ylabel('$(Millions)')
        plt.show()
    else:
        return 0

def interest_visualizer():
    choice = str(input("Would you like to show the values? (y/n) "))
    if (choice == 'y'):
        data = pd.read_csv('interest.csv')
        plt.plot(data.Balance / 10**6)
        plt.plot(data.Principal / 10**6)
        plt.plot(data.Interest / 10**6)
        plt.legend(['Principal', 'Interest', 'Balance'])
        plt.xlabel("Year")
        plt.ylabel("$(Millions)")
        plt.show()
    else:
        return 0

def createResults(x, pv, fv, i, n, pmt):
    resultsTxt = open("results.txt", 'a')
    resultsTxt.write(" ------ Input ------ \n")
    if x in (1, 2, 3, 4, 5, 6):
        #FutureValue
        if x == 1:
            resultsTxt.write(date())
            resultsTxt.write("Present Value: " + str(pv) + "\n")
            resultsTxt.write("Interest: " + str(i) + "\n")
            resultsTxt.write("Periods: " + str(n) + "\n")
            resultsTxt.write("Payment: " + str(pmt) + "\n")
            resultsTxt.write(" ------ Answer ------ \n")
            resultsTxt.write("Future Value: {:.3f} \n".format(fv))
        #PresentValue
        elif x == 2:
            resultsTxt.write(date())
            resultsTxt.write("Future Value: " + str(fv) + "\n")
            resultsTxt.write("Interest: " + str(i) + "\n")
            resultsTxt.write("Periods: " + str(n) + "\n")
            resultsTxt.write("Payment: " + str(pmt) + "\n")
            resultsTxt.write(" ------ Answer ------ \n")
            resultsTxt.write("Present Value: {:.3f} \n".format(pv))
        #Interest
        elif x == 3:
            resultsTxt.write(date())
            resultsTxt.write("Present Value: " + str(pv) + "\n")
            resultsTxt.write("Future Value: " + str(fv) + "\n")
            resultsTxt.write("Periods: " + str(n) + "\n")
            resultsTxt.write("Payment: " + str(pmt) + "\n")
            resultsTxt.write(" ------ Answer ------ \n")
            resultsTxt.write("Annual Interest: {:.3f} \n".format(i))
        #Period
        elif x == 4:
            resultsTxt.write(date())
            resultsTxt.write("Present Value: " + str(pv) + "\n")
            resultsTxt.write("Future Value: " + str(fv) + "\n")
            resultsTxt.write("Interest: " + str(i) + "\n")
            resultsTxt.write("Payment: " + str(pmt) + "\n")
            resultsTxt.write(" ------ Answer ------ \n")
            resultsTxt.write("Periods: {:.3f} \n".format(n))
        #Payment
        elif x == 5:
            resultsTxt.write(date())
            resultsTxt.write("Present Value: " + str(pv) + "\n")
            resultsTxt.write("Future Value: " + str(fv) + "\n")
            resultsTxt.write("Interest: " + str(i) + "\n")
            resultsTxt.write("Periods: " + str(n) + "\n")
            resultsTxt.write(" ------ Answer ------ \n")
            resultsTxt.write("Monthly Payment Amount: {:.3f} \n".format(pmt))
        else:
            resultsTxt.write(date())
            resultsTxt.write("Present Value: " + str(pv) + "\n")
            resultsTxt.write("Future Value: " + str(fv) + "\n")
            resultsTxt.write("Interest: " + str(i) + "\n")
            resultsTxt.write("Periods: " + str(n) + "\n")
            resultsTxt.write(" ------ Answer ------ \n")
            resultsTxt.write("Monthly Payment Amount: {:.3f} \n".format(pmt))

    resultsTxt.close()

# ROI = ((PV - FV) / FV) * 100
def ROI():
    pv = int(input("Amount Invested($): "))
    fv = float(input("Amounted Returned($): "))
    # i = float(input("Investment Length: ")) # 2.75
    save = input("Would you like to save the values? (y/n) ")
    roi = ((fv - pv) / pv) * 100
    gain = fv - pv
    print("Investment Gain = ${:.2f}".format(gain))
    print("Return on Investment = {:.2f}%".format(roi))

    if (save == "y"):
        createResults(1,pv, fv, 0, 0,0)


def Interest_calc():
    pv = int(input("Present Value($): "))
    i = float(input("Interest(%): "))/100
    n = int(input("Number of Periods: "))
    pmt = int(input("Payment($): ")) * -1
    save = input("Would you like to save the values? (y/n) ")  
    sum_pmt = 0
    sum_int = 0
    with open('interest.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Year", "Balance", "Principal", "Interest"])
        principal_s = pv 
        balance_s = pv 
        principal_e = pv
        clear()
        if (save == 'y'):
            for x in range(1,n+1):
                p_i= pv * i
                fv = pv + p_i - pmt
                principal_e = principal_s - pmt
                print("   start_principal " + " start_balance" +   " interest " + " end_balance " + " end_principal ")
                print(str(x) + " " +"{:.2f}".format(principal_s) +  "        " + "{:.2f}".format(balance_s) +  "     " + "{:.2f}".format(p_i)  + "  " + "{:.2f}".format(fv) +  "    " + "{:.2f}".format(principal_e))
                sum_pmt = pmt + sum_pmt
                sum_int = p_i + sum_int
                writer.writerow([x, round(pv), round(-sum_pmt), round(sum_int), round(fv)])
                principal_s = principal_s - pmt
                balance_s = fv
                pv = fv
            print(" ")
        else:
            for x in range(1,n+1):
                p_i= pv * i
                fv = pv + p_i - pmt
                pv = fv
        return(fv)
# Investment

# FV = PV * (1 + i) ** n
# FVa = A/i * ((((1 + i)^n) - 1) / 1)
def FutureValue():
    pv = int(input("Present Value($): "))
    i = float(input("Interest(%): "))/100
    n = int(input("Number of Periods: "))
    pmt = int(input("Payment($): ")) * -1
    save = input("Would you like to save the values? (y/n) ")
    sum_pmt = 0
    sum_int = 0
    with open('tvm.csv', 'w', newline='') as file:
        with open('tvm_graph.csv', 'w', newline='') as file1:
            writer = csv.writer(file)
            writer1 = csv.writer(file1)
            writer.writerow(["Year" , "PV", "PMT", "Interest", "FV"])
            writer1.writerow(["Year", "PV", "SumofPMT", "AccumulatedInterest", "FV"])

            for x in range(1,n+1):
                p_i= pv * i
                fv = pv + p_i - pmt
                sum_pmt = pmt + sum_pmt
                sum_int = p_i + sum_int
                writer1.writerow([x, round(-pv), round(sum_pmt), round(-sum_int), round(fv)])

                if (save == "y"):
                    writer.writerow([x, round(pv), round(-pmt), round(p_i), round(-fv)])
                    resultsTxt = open("results.txt", 'a')
                    resultsTxt.write("Period:" + str(x) + " PV:{:.2f}".format(pv) + " PMT:" + str(pmt) + " Interest:{:.2f}".format(p_i) + " FV:{:.2f}".format(fv) + "\n")
                    resultsTxt.close()
                pv = fv
            print("Future Value = ${:.2f}".format(fv))
            if (save == "y"):
                createResults(1, pv, fv, i, n, pmt)

# PV = FV / (1 + i) ** n
# PVa = A/i * [1 - 1/ (1 + i)^n ]
def PresentValue():
    fv = int(input("Future Value($): "))
    i = float(input("Interest(%): "))/100
    n = int(input("Number of Periods: "))
    pmt = int(input("Payment($): "))
    save = input("Would you like to save the values? (y/n) ")
    for x in range(1,n+1):
        pv = (fv - pmt) / (1 + i)
        p_i= pv * i
        if (save == "y"):
            resultsTxt = open("results.txt", 'a')
            resultsTxt.write("Period:" + str(x) + " PV:{:.2f}".format(pv) + " PMT:" + str(pmt) + " Interest:{:.2f}".format(p_i) + " FV:{:.2f}".format(fv) + "\n")
            resultsTxt.close()
        fv = pv
    print("Present Value = ${:.2f}".format(pv))
    if (save == "y"):
        createResults(1, pv, fv, i, n, pmt)

# i = ((FV / PV) ** (1 / n)) - 1
def Interest():
    pv = int(input("Present Value($): "))
    fv = int(input("Future Value($): "))
    n = int(input("Number of Periods: "))
    pmt = int(input("Payment($): "))
    save = input("Would you like to save the values? (y/n) ")
    i = ((fv / pv) ** (1 / n)) - 1
    print("Interest: {:0.3f}%".format(i))
    if (save == "y"):
        createResults(1, pv, fv, i, n, pmt)

# n = LN(FV / PV) / LN (1 + i)
def Period():
    pv = int(input("Present Value($): "))
    fv = int(input("Future Value($): "))
    i = float(input("Interest(%): "))/100
    pmt = int(input("Payment($): "))
    save = input("Would you like to save the values? (y/n) ")
    n = math.log(fv / pv) / math.log(1 + i)
    print("Number of Period: {:.3f}".format(n))
    if (save == "y"):
        createResults(4, pv, fv, i, n, pmt)

# pmt = (pv - (fv/((1+i)**n))) / ((1 - (1 / ((1 + i) ** n)))/i)
def Payment():
    pv = int(input("Present Value($): "))
    fv = int (input("Future Value($): "))
    i = float(input("Interest(%): "))/100
    n = int(input("Period: "))
    pmt = (pv - (fv/((1+i)**n))) / ((1 - (1 / ((1 + i) ** n)))/i)
    print("Monthly Payment Amount: {:.3f}".format(pmt))
    save = input("Would you like to save the values? (y/n) ")
    pv_x = pv
    fv_x = fv
    for x in range(1, n+1):
        p_i = pv_x * i 
        fv_x = pv_x - pmt + p_i
        if (save == "y"):
            resultsTxt = open("results.txt", "a")
            resultsTxt.write("Period:" + str(x) + " PV:{:.2f}".format(pv_x) + " PMT:" + str(pmt) + " Interest:{:.2f}".format(p_i) + " FV:{:.2f}".format(fv_x) + "\n")
            resultsTxt.close()
        pv_x = fv_x 
    if (save == "y"):
        createResults(5, pv, fv, i, n, pmt)

def printDisplay():
    print("Select Operation")
    print("1.Future Value")
    print("2.Present Value")
    print("3.Interest")
    print("4.Periods")
    print("5.Payment")
    # Other
    print("6.Return On Investments")
    print("6.Interest Calculator")

printDisplay()

while True:
    choice = int(input("Enter choice (0/1/2/3/4/5/6/7): "))
    
    if choice == 0:
        clear()
        printDisplay()
        choice = int(input("Enter choice (0/1/2/3/4/5/6/7): "))

    if choice in ( 1, 2, 3, 4, 5, 6, 7):
        if choice == 0:
            clear()
            printDisplay()
        elif choice == 1:
            txtClear()
            clear()
            FutureValue()
            tvm_visualizer()
        elif choice == 2:
            txtClear()
            clear()
            PresentValue()
        elif choice == 3:
            txtClear()
            clear()
            Interest()
        elif choice == 4:
            txtClear()
            clear()
            Period()
        elif choice == 5:
            txtClear()
            clear()
            Payment()
        elif choice == 6:
            txtClear()
            clear()
            ROI()
        elif choice == 7:
            txtClear()
            clear()
            Interest_calc()
            interest_visualizer()
    else:
        print("Input Invalid, 0 to see menu")
    
    next_calc = str(input("Continue? (y/n): "))
    if (next_calc == 'y'):
        continue
    elif (next_calc == 'n'):
        break
    else: 
        print("Input Invalid")





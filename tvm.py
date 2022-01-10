import math
import numpy as np
from os import system, name

def clear():
    _ = system('clear')

def txtClear():
    resultsTxt = open("results.txt", "r+")
    resultsTxt.truncate(0)
    resultsTxt.close()

def createResults(x, pv, fv, i, n, pmt):
    resultsTxt = open("results.txt", 'a')
    resultsTxt.write(" ------ Input ------ \n")
    if x in ( 1, 2, 3, 4, 5):
        #FutureValue
        if x == 1:
            resultsTxt.write("Present Value: " + str(pv) + "\n")
            resultsTxt.write("Interest: " + str(i) + "\n")
            resultsTxt.write("Periods: " + str(n) + "\n")
            resultsTxt.write("Payment: " + str(pmt) + "\n")
            resultsTxt.write(" ------ Answer ------ \n")
            resultsTxt.write("Future Value: {:.3f} \n".format(fv))
        #PresentValue
        elif x == 2:
            resultsTxt.write("Future Value: " + str(fv) + "\n")
            resultsTxt.write("Interest: " + str(i) + "\n")
            resultsTxt.write("Periods: " + str(n) + "\n")
            resultsTxt.write("Payment: " + str(pmt) + "\n")
            resultsTxt.write(" ------ Answer ------ \n")
            resultsTxt.write("Present Value: {:.3f} \n".format(pv))
        #Interest
        elif x == 3:
            resultsTxt.write("Present Value: " + str(pv) + "\n")
            resultsTxt.write("Future Value: " + str(fv) + "\n")
            resultsTxt.write("Periods: " + str(n) + "\n")
            resultsTxt.write("Payment: " + str(pmt) + "\n")
            resultsTxt.write(" ------ Answer ------ \n")
            resultsTxt.write("Annual Interest: {:.3f} \n".format(i))
        #Period
        elif x == 4:
            resultsTxt.write("Present Value: " + str(pv) + "\n")
            resultsTxt.write("Future Value: " + str(fv) + "\n")
            resultsTxt.write("Interest: " + str(i) + "\n")
            resultsTxt.write("Payment: " + str(pmt) + "\n")
            resultsTxt.write(" ------ Answer ------ \n")
            resultsTxt.write("Periods: {:.3f} \n".format(n))
        #Payment
        else:
            resultsTxt.write("Present Value: " + str(pv) + "\n")
            resultsTxt.write("Future Value: " + str(fv) + "\n")
            resultsTxt.write("Interest: " + str(i) + "\n")
            resultsTxt.write("Periods: " + str(n) + "\n")
            resultsTxt.write(" ------ Answer ------ \n")
            resultsTxt.write("Monthly Payment Amount: {:.3f} \n".format(pmt))
    resultsTxt.close()

# FV = PV * (1 + i) ** n
# FVa = A/i * ((((1 + i)^n) - 1) / 1)
def FutureValue():
    pv = int(input("Present Value($): "))
    i = float(input("Interest(%): "))/100
    n = int(input("Number of Periods: "))
    pmt = int(input("Payment($): "))
    save = input("Would you like to save the values? (y/n) ")
    for x in range(1,n+1):
        p_i= pv * i
        fv = pv + p_i - pmt
        pv = fv
        if (save == "y"):
            resultsTxt = open("results.txt", 'a')
            resultsTxt.write("Period:" + str(x) + " PV:{:.2f}".format(pv) + " PMT:" + str(pmt) + " Interest:{:.2f}".format(p_i) + " FV:{:.2f}".format(fv) + "\n")
            resultsTxt.close()
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
printDisplay()

while True:
    choice = int(input("Enter choice (0/1/2/3/4/5): "))
    
    if choice == 0:
        clear()
        printDisplay()
        choice = int(input("Enter choice (0/1/2/3/4/5): "))

    if choice in ( 1, 2, 3, 4, 5):
        if choice == 0:
            clear()
            printDisplay()
        elif choice == 1:
            txtClear()
            clear()
            FutureValue()
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
    else:
        print("Input Invalid, 0 to see menu")
    
    next_calc = str(input("Continue? (y/n): "))
    if (next_calc == 'y'):
        continue
    elif (next_calc == 'n'):
        break
    else: 
        print("Input Invalid")





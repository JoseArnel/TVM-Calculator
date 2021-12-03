import math
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
            resultsTxt.write("Future Value: " + str(fv) + "\n")
        #PresentValue
        elif x == 2:
            resultsTxt.write("Future Value: " + str(fv) + "\n")
            resultsTxt.write("Interest: " + str(i) + "\n")
            resultsTxt.write("Periods: " + str(n) + "\n")
            resultsTxt.write("Payment: " + str(pmt) + "\n")
            resultsTxt.write(" ------ Answer ------ \n")
            resultsTxt.write("Present Value: " + str(pv) + "\n")
        #Interest
        elif x == 3:
            resultsTxt.write("Present Value: " + str(pv) + "\n")
            resultsTxt.write("Future Value: " + str(fv) + "\n")
            resultsTxt.write("Periods: " + str(n) + "\n")
            resultsTxt.write("Payment: " + str(pmt) + "\n")
            resultsTxt.write(" ------ Answer ------ \n")
            resultsTxt.write("Interest: " + str(i) + "\n")
        #Period
        elif x == 4:
            resultsTxt.write("Present Value: " + str(pv) + "\n")
            resultsTxt.write("Future Value: " + str(fv) + "\n")
            resultsTxt.write("Interest: " + str(i) + "\n")
            resultsTxt.write("Payment: " + str(pmt) + "\n")
            resultsTxt.write(" ------ Answer ------ \n")
            resultsTxt.write("Periods: " + str(n) + "\n")
        #Payment
        else:
            resultsTxt.write("Present Value: " + str(pv) + "\n")
            resultsTxt.write("Future Value: " + str(fv) + "\n")
            resultsTxt.write("Interest: " + str(i) + "\n")
            resultsTxt.write("Periods: " + str(n) + "\n")
            resultsTxt.write(" ------ Answer ------ \n")
            resultsTxt.write("Payment: " + str(pmt) + "\n")
    resultsTxt.close()

# FV = PV * (1 + i) ** n
# FVa = A/i * ((((1 + i)^n) - 1) / 1)
def FutureValue():
    pv = int(input("Present Value: "))
    i = float(input("Interest(%): "))/100
    n = int(input("Number of Periods: "))
    pmt = int(input("Payment: "))
    save = input("Would you wanna save the values? (y/n) ")
    for x in range(0,n):
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
    fv = int(input("Future Value: "))
    i = float(input("Interest(%): "))/100
    n = int(input("Number of Periods: "))
    pmt = int(input("Payment: "))
    save = input("Would you wanna save the values? (y/n) ")
    for x in range(0,n):
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
    pv = int(input("Present Value: "))
    fv = int(input("Future Value: "))
    n = int(input("Number of Periods: "))
    pmt = int(input("Payment: "))
    save = input("Would you wanna save the values? (y/n) ")
    i = (((fv / pv)**(1/n)) - 1) * 100
    print("Interest: {:0.3f}%".format(i))
    if (save == "y"):
        createResults(1, pv, fv, i, n, pmt)

# n = LN(FV / PV) / LN (1 + i)
def Period():
    pv = int(input("Present Value: "))
    fv = int(input("Future Value: "))
    i = float(input("Interest(%): "))/100
    pmt = int(input("Payment: "))
    save = input("Would you wanna save the values? (y/n) ")
    n = math.log(fv / pv) / math.log(1 + i)
    print("Number of Period: {:.3f}".format(n))
    if (save == "y"):
        createResults(4, pv, fv, i, n, pmt)

def printDisplay():
    print("Select Operation")
    print("1.Future Value")
    print("2.Present Value")
    print("3.Interest")
    print("4.Periods")
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
            clear()
            PresentValue()
        
        elif choice == 3:
            clear()
            Interest()
        
        elif choice == 4:
            clear()
            Period()
    else:
        print("Input Invalid")
        print("0 to see menu")
    
    next_calc = str(input("Continue? (y/n): "))
    if (next_calc == 'y'):
        continue
    elif (next_calc == 'n'):
        break
    else: 
        print("Input Invalid")





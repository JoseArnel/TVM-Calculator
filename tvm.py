import math
from os import system, name

def clear():
    _ = system('clear')

def CompoundInterest():
    principal = float(input())
    rate = float(input())
    period = float(input())

    ci_future = principal * (math.pow(1 + rate/100), period)
    compound = ci_future - principal

def CalcInvestment():
    purcahse_price = int(input("Purchase Price: "))
    sale_price = float(input("Sale Price: "))
    dividends = float(input("Dividends: "))
    per_return = (((sale_price-purcahse_price)+dividends)/purcahse_price)*100
    print("Percentage Return: {:.2f}%".format(per_return))

def txtClear():
    resultsTxt = open("results.txt", "r+")
    resultsTxt.truncate(0)
    resultsTxt.close()

def createResults(pv, fv, i, n, result):
    resultsTxt = open("results.txt", 'w+')
    resultsTxt.write("Present Value : " + str(pv) + "\n")
    resultsTxt.write("Future Value : " + str(fv) + "\n")
    resultsTxt.write("Interest: " + str(i) + "\n")
    resultsTxt.write("Periods: " + str(n) + "\n")
    resultsTxt.write("Result: " + str(result))
    # resultsTxt.write("Payment: ", pmt)
    resultsTxt.close()

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
    # if (save == "y"):
    #     createResults(pv, 0, i, n, fv)

# PV = FV / (1 + i) ** n
# PVa = A/i * [1 - 1/ (1 + i)^n ]
def PresentValue():
    fv = int(input("Future Value: "))
    i = float(input("Interest(%): "))/100
    n = int(input("Number of Periods: "))
    pv = fv/((1+i)**n)
    print("Present Value: {:.2f}".format(pv))

# i = ((FV / PV) ** (1 / n)) - 1
def Interest():
    pv = int(input("Present Value: "))
    fv = int(input("Future Value: "))
    n = int(input("Number of Periods: "))
    i = (((fv / pv)**(1/n)) - 1) * 100
    print("Interest: {:0.3f}%".format(i))

# n = LN(FV / PV) / LN (1 + i)
def Period():
    pv = int(input("Present Value: "))
    fv = int(input("Future Value: "))
    i = float(input("Interest(%): "))/100
    n = math.log(fv / pv) / math.log(1 + i)
    print("Number of Period: {:.3f}".format(n))

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
    
    next_calc = str(input("Continue? (y/n): "))
    if (next_calc == 'y'):
        continue
    elif (next_calc == 'n'):
        break
    else: 
        print("Input Invalid")




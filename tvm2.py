pv = int(input("Present Value: "))
fv = int(input("Future Value: "))
n = int(input("Number of Periods: "))
pmt = int(input("Payment: "))
save = input("Would you wanna save the values? (y/n) ")
i = (((fv / pv)**(1/n)) - 1) * 100
print("Interest: {:0.3f}%".format(i))



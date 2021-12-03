fv = int(input("Future Value: "))
i = float(input("Interest(%): "))/100
n = int(input("Number of Periods: "))
pmt = int(input("Payment: "))
for x in range(0,n):
    p_i= fv * i
    pv = fv - p_i - pmt
    fv = pv
    print("Period:" + str(x) +  " FV:{:.2f}".format(fv) + " PMT:" + str(pmt) + " Interest:{:.2f}".format(p_i) + " PV:{:.2f}".format(pv))
pv = fv/((1+i)**n)
print("Present Value = ${:.2f}".format(pv))

980, i 
fv = int(input("Future Value: "))
i = float(input("Interest(%): "))/100
n = int(input("Number of Periods: "))
pmt = int(input("Payment: "))
for x in range(0,n):
    pv = (fv - pmt) / (1 + i)
    p_i= pv * i
    print("Period:" + str(x) +  " FV:{:.2f}".format(fv) + " PMT:" + str(pmt) + " Interest:{:.2f}".format(p_i) + " PV:{:.2f}".format(pv))
    fv = pv
print("Present Value = ${:.2f}".format(pv))

# fv = pv + pmt + (pv*i)
# pv = fv - pmt - (pv*i)
# pv + (pv*i) = fv - pmt (- (pv*i) + (pv*i))
# pv(1 + i ) = fv - pmt (- (pv*i) + (pv*i))
# pv(1 + i) / (1 + i) = (fv - pmt) / (1 + i)
# pv = (fv - pmt) / (1 + i)

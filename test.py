import numpy_financial as npf

initialInvestment       = 500;  # Initial investment

interestRate            = 0.05; # Annual rate of interest

compoundingFrequency    = 4;    # The interest is compounded every 3 months

quarterlyPayment        = 100;  # Payment towards investment 

numberOfYears           = 10;   # Future value of total investment upon expiry of this period

 

futureValue             = npf.fv(interestRate/compoundingFrequency,

                                numberOfYears * compoundingFrequency,

                                -quarterlyPayment,

                                -initialInvestment)

 

print("Initial Investment:%5.2f"%initialInvestment)

print("Interest Rate:%2.2f"%interestRate)

print("Compounding Frequency:%d"%compoundingFrequency)

print("Investment on every quarter:%5.2f"%quarterlyPayment)

print("Investment period in years:%d"%numberOfYears)

print("Value of Investment upon expirty of %d years:%10.2f"%(numberOfYears,futureValue))


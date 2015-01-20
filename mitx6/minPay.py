minPay = 0
month = 0
totalPayments = 0
interest = 0

while month < 12:
  minPay = balance * monthlyPaymentRate
  month += 1
  print "Month: " + str(month)

  print "Minimum monthly payment: " + "{0:.2f}".format(minPay)
  totalPayments += minPay
  balance -= minPay
  interest = balance * (annualInterestRate / 12.0)
  balance += interest

  print "Remaining balance: " + "{0:.2f}".format(balance)

print "Total paid: " + "{0:.2f}".format(totalPayments)
print "Remaining balance: " + "{0:.2f}".format(balance)

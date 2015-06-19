# for test data
#
balance = 3329
annualInterestRate = 0.20

fixedPay = round(((balance + balance * annualInterestRate) / 12.0), -1)
startingBalance = balance
print "Calculated first fixedPay: " + str(fixedPay)

while balance > 0:
  month = 0
  totalPayments = 0.0
  interest = 0.0
  
  while month < 12:
    month += 1

    print "At month: " + str(month) + "balance at: " + str(balance)

    totalPayments += fixedPay 
    balance -= fixedPay
    interest = balance * (annualInterestRate / 12.0)
    balance += interest

  print "Got through a year with fixedPay at: " + "{0:.2f}".format(fixedPay)

  if balance > 0:
    fixedPay += 10
    fixedPay = round(fixedPay, -1)
    balance = startingBalance

  if balance < -fixedPay:
    fixedPay -= fixedPay / 12
    fixedPay = round(fixedPay, -1)
    balance = startingBalance

print "Total paid: " + "{0:.2f}".format(totalPayments)
print "Remaining balance: " + "{0:.2f}".format(balance)
print "Lowest Payment: " + "{0:.2f}".format(fixedPay)

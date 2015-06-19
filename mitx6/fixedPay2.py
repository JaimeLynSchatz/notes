balance = 3926
annualInterestRate = 0.20

fixedPay = round(((balance + balance * annualInterestRate) / 12.0), -1)
startBal = balance
while balance > 0:
  month = 0
  totalPayments = 0.0
  interest = 0.0
  while month < 12:
    month += 1
    totalPayments += fixedPay
    balance -= fixedPay
    interest = balance * (annualInterestRate / 12.0)
    balance += interest
  if balance > 0:
    fixedPay += 10
    fixedPay = round(fixedPay, -1)
    balance = startBal
  elif balance < -fixedPay:
    fixedPay -= fixedPay / 12
    fixedPay = round(fixedPay, -1)
    balance = startBal
print "Lowest Payment: " + str(int(fixedPay))                                                      

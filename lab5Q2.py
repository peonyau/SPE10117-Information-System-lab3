loanAmount = int(input('The loan amount is:'))
annualInterestRate = int(input('The annual interest rate is:')) 
monthlyPayment = int(input('The monthly payment is:'))

startingBalance = loanAmount
payment = monthlyPayment
middleBalance = startingBalance - payment
interst = loanAmount * annualInterestRate/12/100
endingBalance = middleBalance + interest

print('''
        Starting            Middle              Ending
Month	Balance   Payment   Balance   Interest  Balance
-------------------------------------------------------
''')
for i in range(1,5):
    print('%8d%10.2f%10.2f%10.2f%10.2f%10.2f'%(i,
                                               startingBalance,
                                               payment,
                                               middleBalance,
                                               interst,
                                               endingBalance))
   startingBalance = endingBalance 
   if startingBalance > payment:
       payment=monthlyPayment
   else:
       payment = monthlyPayment
   middleBalance = startingBalance - payment
   interst = loanAmount * annualInterestRate/12/100
   endingBalance = middleBalance + interest 

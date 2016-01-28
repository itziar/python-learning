"""
PROBLEM 1: PAYING THE MINIMUM

Write a program to calculate the credit card balance after one year if a person only pays the minimum monthly payment
required by the credit card company each month.

The following variables contain values as described below:

balance - the outstanding balance on the credit card

annualInterestRate - annual interest rate as a decimal

monthlyPaymentRate - minimum monthly payment rate as a decimal

For each month, calculate statements on the monthly payment and remaining balance, and print to screen something of the format:

Month: 1
Minimum monthly payment: 96.0
Remaining balance: 4784.0
Be sure to print out no more than two decimal digits of accuracy - so print

Remaining balance: 813.41
instead of

Remaining balance: 813.4141998135
Finally, print out the total amount paid that year and the remaining balance at the end of the year in the format:

Total paid: 96.0
Remaining balance: 4784.0
A summary of the required math is found below:

Monthly interest rate= (Annual interest rate) / 12.0
Minimum monthly payment = (Minimum monthly payment rate) x (Previous balance)
Monthly unpaid balance = (Previous balance) - (Minimum monthly payment)
Updated balance each month = (Monthly unpaid balance) + (Monthly interest rate x Monthly unpaid balance)

Note that the grading script looks for the order in which each value is printed out. We provide sample test cases below;
we suggest you develop your code on your own machine, and make sure your code passes the sample test cases, before you
paste it into the box below.
"""

balance = 4213  # this is an example balance
annualInterestRate = 0.2  # this is an example annual interest rate
monthlyPaymentRate = 0.04  # this is an example monthly payment rate

monthlyInterestRate = annualInterestRate / 12.0
previousBalance = balance
pagado = 0
for i in range(1, 13, 1):
    MonthlyPayment = monthlyPaymentRate * previousBalance
    monthlyUnpaidBalance = previousBalance - MonthlyPayment
    updatedBalanceEachMonth = monthlyUnpaidBalance + (monthlyInterestRate * monthlyUnpaidBalance)
    previousBalance = updatedBalanceEachMonth
    pagado += MonthlyPayment
    print "Month: " + str(i)
    print "Minimum monthly payment: " + str(round(MonthlyPayment, 2))
    print "Remaining balance: " + str(round(previousBalance, 2))

print "Total paid: " + str(round(pagado, 2))
print "Remaining balance: " + str(round(previousBalance, 2))

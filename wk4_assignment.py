##Write a function that calculates and returns the monthly payments for a loan. This function accepts three parameters in the exact order (principal, annual_interest_rate, duration):

##principal: The total amount of loan. Assume that the principal is a positive floating point number.
##annual_interest_rate: This is the percent interest rate per year. Assume that annual_interest_rate is a floating point number. (Notice that 4.5 means that the interest rate is 4.5 percent per year.)
##duration: number of years to pay the loan back. Assume that duration is a positive integer.
##To calculate the amount of monthly payment for the loan you should use the following equation

##MonthlyPayment=Principal∗r(1+r)**n/((1+r)**n−1)
##Where:

##r is the monthly interest rate (shold be calculated by first dividing the
##annual_interest_rate by 100 and then divide the result by 12 to make it monthly).
##Notice that if the interest rate is equal to zero then the above equation
##will give you a ZeroDivisionError. In that case you should use the
##follwing equation:MonthlyPayment=Principal/n
##n is the total number of monthly payments for the entire duration of the loan (Notice that n is equal to loan duration in years multiplied by 12).
##Your function should return the monthly payment as a floating point number.

def _monpayment(principal, annual_interest_rate, duration):
    r = annual_interest_rate/100/12
    n = duration * 12
    if r != 0:
        payment = principal*r*(1+r)**n/((1+r)**n - 1)
    else:
        payment = principal/n
    return payment

prin = input ('Please enter principal: ')
air = input ('Please enter annual interest rate: ')
dur = input ('Please enter duraion in years: ')
prinint = float(prin)
airint = float(air)
durint = int(dur)

monthly = _monpayment(prinint, airint, durint)
print (monthly)

    

# Program #3: Tax Rate
# A retail company must file a monthly sales tax report listing the total sales for the month, 
# and the amount of state and county sales tax collected. 
# The state sales tax rate is 5 percent and the county sales tax rate is 2.5 percent.  
# Write a program that asks the user to enter the total sales for the month.  
# From this figure, the application should calculate and display the following:
import math
# The amount of county sales tax.
# The amount of state sales tax.
# The total sales tax (county plus state)
# Use at least one function with input and output in this program
def tax(a):
    #amt = int(input("enter amount to tax here:   "))
    state_tax = (a*0.05)
    sales_tax = (a*0.025)
    total_tax = (state_tax+sales_tax)
    total = (a + state_tax + sales_tax)
    total_tax = round(total_tax,2)
    total = round(total,2)
    total_tax = str(total_tax)
    total = str(total)
    print("your total tax is $"+ total_tax)
    print("your total due is $"+ total)
    a = int(a)
amt = int(input("enter amount to tax here:   "))
tax(amt)

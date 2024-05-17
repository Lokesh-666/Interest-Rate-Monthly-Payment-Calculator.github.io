# Collect the necessary input: principal, apr(interest rate), years
# Calculate the monthly payment
# Show it to the User
# F

def main():
    print("This is a monthly payment loan calculator at your service: \n")


    principal = float(input("What was the initial loan amount? \n")) # Get the principal amount 
    apr = float(input("What is the annual interest rate? \n")) # Get the annual interest rate
    years = int(input("How many years will it take to pay off the loan? \n")) # Get the number of years
    
    
    monthly_interest_rate = apr/1200
    amount_of_months = years*12
    monthly_payment = principal * (monthly_interest_rate / (1 - (1 + monthly_interest_rate)**(-amount_of_months)))


    print("Your monthly payment is: %.2f " % monthly_payment) # Show the monthly payment to the user



main() 
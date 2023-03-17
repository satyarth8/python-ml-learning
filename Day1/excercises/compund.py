principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the annual interest rate: "))
time = float(input("Enter the time (in years): "))
compounds_per_year = int(input("Enter the number of times interest is compounded per year: "))

# Calculate compound interest
interest = principal * ((1 + (rate / compounds_per_year)) ** (compounds_per_year * time)) - principal

# Calculate total amount
total_amount = principal + interest

# Display the result
print("Compound interest: ", round(interest, 2))
print("Total amount: ", round(total_amount, 2))
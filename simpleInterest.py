# Assignment 1 Day-2 (Python Programming Essentials Bootcamp)

def calculate_simple_interest(principal, years, gender, senior_citizen):
    if gender == 'female' and senior_citizen:
        rate = 8
    elif gender == 'female' and not senior_citizen:
        rate = 6
    elif gender == 'male' and senior_citizen:
        rate = 7
    elif gender == 'male' and not senior_citizen:
        rate = 5
    else:
        return None  # Invalid gender or senior citizen status

    interest = (principal * rate * years) / 100
    return interest


principal = float(input("Enter the principal amount: "))
years = int(input("Enter the number of years: "))
gender = input("Enter the gender (male/female): ").lower()
senior_citizen = input("Is the customer a senior citizen? (yes/no): ").lower()

if senior_citizen == 'yes':
    senior_citizen = True
elif senior_citizen == 'no':
    senior_citizen = False
else:
    print("Invalid input for senior citizen status.")
    exit(1)

interest = calculate_simple_interest(principal, years, gender, senior_citizen)

if interest is None:
    print("Invalid input for gender.")
else:
    print(f"\nThe Simple Interest for the customer's fixed deposit is: {interest}")

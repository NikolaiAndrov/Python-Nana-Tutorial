def calculate_days_to_hours(days_count):
    days_to_hours = days_count * 24
    return f"{days_count} days are {days_to_hours} hours."

def validate_and_execute():
    try:
        days = int(user_input)
        if days <= 0:
            print("You should enter a valid positive number!")
        else:
            result = calculate_days_to_hours(days)
            print(result)
    except ValueError:
        print("Invalid input!")

while True:
    user_input = input("Enter a number of days.\n")
    validate_and_execute()
    if user_input.lower() == "end":
        break
def calculate_days_to_hours(days_count):
    if days_count > 0:
        days_to_hours = days_count * 24
        return f"{days_count} days are {days_to_hours} hours."
    return "Invalid input!"


user_input = input("Enter a number of days.\n")

if user_input.isdigit():
    days = int(user_input)
    result = calculate_days_to_hours(days)
    print(result)
else:
    print("Invalid input!")
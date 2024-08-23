def calculate_days_to_hours(days_count):

    if not days_count.isdigit():
        return "Invalid input!"

    days = int(days_count)

    if days <= 0:
        return "Invalid input!"

    days_to_hours = days * 24
    return f"{days} days are {days_to_hours} hours."


user_input = input("Enter a number of days.\n")
result = calculate_days_to_hours(user_input)
print(result)
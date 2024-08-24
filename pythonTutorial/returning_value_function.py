def calculate_days_to_hours(days_count):
    try:
        days = int(days_count)
        if days <= 0:
            return "You should enter a valid positive number!"
    except ValueError:
        return "Invalid input!"

    days_to_hours = days * 24
    return f"{days} days are {days_to_hours} hours."


user_input = input("Enter a number of days.\n")
result = calculate_days_to_hours(user_input)
print(result)
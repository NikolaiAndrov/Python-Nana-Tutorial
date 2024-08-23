print("Enter a number of days.")
days_input = int(input())


def calculate_days_to_hours(days_count):
    if days_count > 0:
        days_to_hours = days_count * 24
        return f"{days_count} days are {days_to_hours} hours."
    return "Invalid input!"

result = calculate_days_to_hours(days_input)
print(result)
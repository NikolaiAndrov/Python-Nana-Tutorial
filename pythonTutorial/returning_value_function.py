def calculate_days_to_hours(days_count):
    days_to_hours = days_count * 24
    return f"{days_count} days are {days_to_hours} hours."

def validate_and_execute(days_count):
    try:
        days = int(days_count)
        if days <= 0:
            print("You should enter a valid positive number!")
        else:
            result = calculate_days_to_hours(days)
            print(result)
    except ValueError:
        print("Invalid input!")

while True:
    user_input = input("Enter a number of days.\n")
    if user_input.lower() == "exit":
        break

    for current_day in user_input.split():
        validate_and_execute(current_day)
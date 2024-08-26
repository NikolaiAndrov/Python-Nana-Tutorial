def calculate_days_to_unit(days_count, conversion_unit):
    if conversion_unit.lower() == "hours":
        return f"{days_count} days are {days_count * 24} {conversion_unit}."
    elif conversion_unit.lower() == "minutes":
        return f"{days_count} days are {days_count * 24 * 60} {conversion_unit}."
    elif conversion_unit.lower() == "seconds":
        return f"{days_count} days are {days_count * 24 * 60 * 60} {conversion_unit}."
    else:
        return "Unsupported conversion unit!"


def validate_and_execute(days_and_conversion_unit):
    try:
        days = int(days_and_conversion_unit["days"])
        if days <= 0:
            print("You should enter a valid positive number!")
        else:
            unit = days_and_conversion_unit["unit"]
            result = calculate_days_to_unit(days, unit)
            print(result)
    except ValueError:
        print("Invalid input!")


while True:
    user_input = input("Enter a number of days and conversion unit.\n")
    if user_input.lower() == "exit":
        break

    try:
        days_and_unit = user_input.split()
        days_and_unit_dictionary = {"days": days_and_unit[0], "unit": days_and_unit[1]}
        validate_and_execute(days_and_unit_dictionary)
    except:
        print("Invalid input")


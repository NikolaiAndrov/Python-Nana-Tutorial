import helper

while True:
    user_input = input("Enter a number of days and conversion unit.\n")
    if user_input.lower() == "exit":
        break

    try:
        days_and_unit = user_input.split()
        days_and_unit_dictionary = {"days": days_and_unit[0], "unit": days_and_unit[1]}
        helper.validate_and_execute(days_and_unit_dictionary)
    except:
        print("Invalid input")


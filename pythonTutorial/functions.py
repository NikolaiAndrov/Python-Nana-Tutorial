days_input = int(input())

def calculate_days_to_minutes(days_count):
    days_to_minutes = days_count * 24 * 60
    print(f"{days_count} days are {days_to_minutes} minutes.")

calculate_days_to_minutes(days_input)
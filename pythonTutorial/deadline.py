import datetime

user_input = input("Enter your goal with a deadline\n")
input_list = user_input.split(", ")

goal = input_list[0]
deadline_str = input_list[1]
deadline = datetime.datetime.strptime(deadline_str, "%d.%m.%Y")
till_deadline = deadline - datetime.datetime.today()
print(f"Time till your deadline: {till_deadline.days} days, goal: {goal}.")
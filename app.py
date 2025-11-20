# print Welcome
print('Welcome to my python program!')
# input hours
hours = input("How many hours did you study today? ")
# alculate hours
hours = float(hours)
weekly_hours = hours * 7
# print result
print(f"You are on track to study {weekly_hours} hours this week.")
# error handling
try:
    hours = float(hours)
except ValueError:
    print("Please enter a valid number.")
    exit()
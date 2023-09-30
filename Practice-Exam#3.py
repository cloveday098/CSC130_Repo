total_hours = 0

# Nested loops to collect study hours
for day in range(7):
    for time_slot in range(3):
        day_name = ""
        time_name = ""

        # Map the day and time_slot values to corresponding names
        if day == 0:
            day_name = "Sunday"
        elif day == 1:
            day_name = "Monday"
        elif day == 2:
            day_name = "Tuesday"
        elif day == 3:
            day_name = "Wednesday"
        elif day == 4:
            day_name = "Thursday"
        elif day == 5:
            day_name = "Friday"
        elif day == 6:
            day_name = "Saturday"

        if time_slot == 0:
            time_name = "morning"
        elif time_slot == 1:
            time_name = "afternoon"
        elif time_slot == 2:
            time_name = "evening"

        hours = int(input(f"How many hours did you study on {day_name} {time_name}? "))
        total_hours += hours

# Print the total study hours for the week
print(f"You studied {total_hours} hours this week.")

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#OR LIKE THIS

total_hours = 0

for day in range(7):
    for time_slot in range(3):
        question = input("How many hours did you study on " + 'Sunday Monday Tuesday Wednesday Thursday Friday Saturday'.split()[day] + ' ' + 'morning afternoon evening'.split()[time_slot] + "? ")

        hours = int(question.split()[0])

        total_hours += hours

print(f"You studied {total_hours} hours this week.")


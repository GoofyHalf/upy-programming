# Problem 1 - Grade Averaging System
# The user enters student grades one by one until typing "done".
# Then the program calculates the average and displays pass/fail.

grades = []

while True:
    # INPUT
    entry = input("Enter a grade (or type 'done' to finish): ")

    # PROCESS
    if entry.lower() == "done":
        break
    grade = float(entry)
    grades.append(grade)

# PROCESS
if len(grades) == 0:
    # OUTPUT
    print("No grades entered. Please enter at least one grade.")
else:
    average = sum(grades) / len(grades)

    # OUTPUT
    if average >= 7.0:
        print(f"Average: {average:.2f} - Passed")
    else:
        print(f"Average: {average:.2f} - Failed")

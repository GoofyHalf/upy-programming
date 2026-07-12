# Problem 4 - Season Classifier
# The user enters month numbers one by one.
# The program displays the corresponding season for each entry.
# The loop continues until the user types "exit".
# If a number is outside 1-12, an error message is shown and the loop continues.

while True:
    # INPUT
    entry = input("Enter a month number (or type 'exit' to finish): ")

    # PROCESS
    if entry.lower() == "exit":
        break
    month = int(entry)

    if month < 1 or month > 12:
        # OUTPUT
        print("Invalid month. Please enter a number between 1 and 12.")
        continue

    if month in (12, 1, 2):
        season = "Winter"
    elif month in (3, 4, 5):
        season = "Spring"
    elif month in (6, 7, 8):
        season = "Summer"
    else:
        season = "Fall"

    # OUTPUT
    print(season)

# Problem 3 - Water Bill Calculator
# The user enters the m3 consumed for multiple months.
# The program calculates the charge per month using tiered rates
# (the rate for the tier the consumption falls into applies to all the m3).
# The loop continues until the user types "exit".
# At the end, the total accumulated charge is displayed.

total = 0.0

while True:
    # INPUT
    entry = input("Enter m3 consumed (or type 'exit' to finish): ")

    # PROCESS
    if entry.lower() == "exit":
        break
    consumption = float(entry)

    if consumption <= 10:
        rate = 8.00
    elif consumption <= 20:
        rate = 12.00
    else:
        rate = 18.00

    charge = consumption * rate
    total += charge

    # OUTPUT
    print(f"Month charge: ${charge:.2f} MXN")

# OUTPUT
print(f"Total: ${total:.2f} MXN")

# Problem 5 - Shipping Cost Calculator
# The user enters weight (kg) and distance (km) for multiple packages.
# The program calculates the shipping cost for each package based on
# weight category (<=5 kg or >5 kg) and distance (<=100 km or >100 km).
# The loop continues until the user types "exit".
# At the end, the total accumulated shipping cost is displayed.

total = 0.0

while True:
    # INPUT
    weight_entry = input("Enter package weight in kg (or type 'exit' to finish): ")

    # PROCESS
    if weight_entry.lower() == "exit":
        break
    weight = float(weight_entry)

    # INPUT
    distance = float(input("Enter distance in km: "))

    # PROCESS
    if distance <= 100:
        cost = 50.00 if weight <= 5 else 80.00
    else:
        cost = 120.00 if weight <= 5 else 200.00

    total += cost

    # OUTPUT
    print(f"Shipping cost: ${cost:.2f} MXN")

# OUTPUT
print(f"Total: ${total:.2f} MXN")

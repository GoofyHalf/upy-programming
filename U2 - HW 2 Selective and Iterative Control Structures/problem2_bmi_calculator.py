# Problem 2 - BMI Calculator
# The user enters weight (kg) and height (m) for multiple people.
# The program calculates and classifies the BMI for each one.
# The loop continues until the user types "exit" when asked for weight.

while True:
    # INPUT
    weight_entry = input("Enter weight in kg (or type 'exit' to finish): ")

    # PROCESS
    if weight_entry.lower() == "exit":
        break
    weight = float(weight_entry)

    # INPUT
    height = float(input("Enter height in m: "))

    # PROCESS
    bmi = weight / (height ** 2)

    if bmi < 18.5:
        category = "Underweight"
    elif bmi < 25:
        category = "Normal"
    elif bmi < 30:
        category = "Overweight"
    else:
        category = "Obese"

    # OUTPUT
    print(f"BMI: {bmi:.2f} - {category}")

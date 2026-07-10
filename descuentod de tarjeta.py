price = 150
age = int(input("Ingresa la edad: "))
id = input("tiene tarjeta: (si/no): ")

if age < 12:
    rate = .30
elif age <=25 and id == "si":
    rate= .20
elif age < 65:
    rate=0.00
else:
    rate= 0.40
n_price= price*(1-rate)
print(f"Price: ${n_price}")
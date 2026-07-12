price=150
#childreanyear > 12 = 30%
#students 12<year<25 = 20% (with ID)
#adultos 26<year<64 = no discount
#adulto mayor year>65= 40% discount
age=int(input("Ingresa la edad: "))
ID=input("Cuenta con tarjeta? (si/no): ")

if age<12:
    rate= 0.30
elif age<=25 and ID== "si":
    rate=0.20
elif age>65:
    rate=0.40
else:
    rate=0.00
n_price=price*(1-rate)
print(f"Price:$ {n_price}")

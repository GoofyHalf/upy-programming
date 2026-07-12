#IMC
#IMC < 18.5 = desnutrido
#18.5 <= IMC < 25 = normal
#25 <= IMC < 30 = Gordito
#IMC > 30 = Majin Boo

weight = float(input("Ingrese su peso: "))
height = float(input("Ingrese su altura en metros: "))
IMC = weight / (height*height)
if IMC < 18.5:
    print("Estas desnutrido.")
elif IMC <= 25:
    print("Estas normal.")
elif IMC <= 30:
    print("Estas gordito.")
else:
    print("Estas Majin Boo")

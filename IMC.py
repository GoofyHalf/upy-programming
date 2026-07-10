weight = float(input("Ingresa tu peso: "))
height = float(input("Ingresa tu altura: "))
IMC = weight / (height*height)
if IMC < 18.5:
    print("Desnutricion")
elif IMC <= 25:
    print("Normal")
elif IMC <= 30:
    print("fat ahh nigger")
else:
    print("Holy ahh")
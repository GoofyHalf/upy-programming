num= int(input("Ingrese un número: "))

if num <=0:
    print("No es positivo")
else:
    if num % 2 == 0:
        print("Positivo par")
    else:
        print("Positivo impar")

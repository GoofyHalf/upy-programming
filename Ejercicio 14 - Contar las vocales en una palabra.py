#Contar vocales en una palabra
palabra= input("Ingrese una palabra: ")
contar = 0
for i in palabra.lower():
    if i in "aeiou":
        contar = contar +1
print(f"La palabra {palabra}, tiene {contar} vocales")

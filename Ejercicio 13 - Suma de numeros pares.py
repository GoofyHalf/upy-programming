#sumar número pares hasta n
n = int(input("Ingresa un número: "))
total = 0
for i in range (2, n+1, 2):
    total= total+i
print(f"El resultado de sumar los números pares hasta {n}, es de {total}")

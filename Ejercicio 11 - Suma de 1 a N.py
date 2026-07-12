num = int(input("Ingresa un número positivo: "))

sum= 0
i = 1

while i <= num:
    sum = sum + i
    i= i + 1

print(f"La suma de números anteriores hasta {num} es de {sum}")

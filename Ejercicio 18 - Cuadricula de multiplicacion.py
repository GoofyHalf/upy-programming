#cuadricula de multiplicación
#lee un número, se imprime una columna #*#, un numero que contenga un # fila y columna

n= int(input("Ingrese un número: "))
for r in range (1, n+1):
    l = ""
    for c in range (1, n+1):
        l = l + str(r*c) + "\t"
    print(l)

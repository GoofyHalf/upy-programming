#lee un #, se imprime una cuadricula #*#, un numero que contrenda una fila y una columna

n = int(input("Ingresa un numero: "))
for r in range(1, n+1):
    row = ""
    for c in range(1, n+1):
        linea = linea + str(r+c) + "\t"
    print(linea)
        
    
pronombres = ['yo', 'tu', 'el', 'nosotros', 'vosotros', 'ellos']

terminaciones = {
    'ar': ['o', 'as', 'a', 'amos', 'ais', 'an'],
    'er': ['o', 'es', 'e', 'emos', 'eis', 'en'],
    'ir': ['o', 'es', 'e', 'imos', 'is', 'en']
}

# INPUT / PROCESS / OUTPUT con manejo de errores
verbo_valido = False
while not verbo_valido:
    try:
        # INPUT
        verbo = input("Ingrese verbo: ")

        # PROCESS
        raiz = verbo[:-2]
        terminacion = verbo[-2:]
        lista_terminaciones = terminaciones[terminacion]

        verbo_valido = True

    except KeyError:
        print("Terminación no válida. El verbo debe terminar en 'ar', 'er' o 'ir'.")
    except IndexError:
        print("Verbo demasiado corto. Intente de nuevo.")

# OUTPUT
for i in range(len(pronombres)):
    print(pronombres[i] + " " + raiz + lista_terminaciones[i])

pronombres = ['yo', 'tu', 'el', 'nosotros', 'vosotros', 'ellos']

terminaciones = {
    'ar': ['o', 'as', 'a', 'amos', 'ais', 'an'],
    'er': ['o', 'es', 'e', 'emos', 'eis', 'en'],
    'ir': ['o', 'es', 'e', 'imos', 'is', 'en']
}

# INPUT
verbo = input("Ingrese verbo: ")

# PROCESS
raiz = verbo[:-2]
terminacion = verbo[-2:]
lista_terminaciones = terminaciones[terminacion]

# OUTPUT
for i in range(len(pronombres)):
    print(pronombres[i] + " " + raiz + lista_terminaciones[i])

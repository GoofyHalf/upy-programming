usuarios = {
    'jperez':  {'password': '1234', 'rol': 'alumno',      'nombre': 'Juan Pérez'},
    'amartin': {'password': '1234', 'rol': 'alumno',      'nombre': 'Ana Martín'},
    'lgomez':  {'password': '1234', 'rol': 'alumno',      'nombre': 'Luis Gómez'},
    'cruiz':   {'password': '1234', 'rol': 'alumno',      'nombre': 'Carla Ruiz'},
    'dtorres': {'password': '1234', 'rol': 'alumno',      'nombre': 'Diego Torres'},
    'msanchez':{'password': '1234', 'rol': 'alumno',      'nombre': 'Mónica Sánchez'},
    'mlopez':  {'password': '1234', 'rol': 'maestro',     'nombre': 'María López'},
    'rgarcia': {'password': '1234', 'rol': 'coordinador', 'nombre': 'Rosa García'}
}

materias = ('Matemáticas', 'Programación', 'Inglés')

calificaciones = {
    'jperez':   {'Matemáticas': 8.5, 'Programación': 9.0, 'Inglés': 7.5},
    'amartin':  {'Matemáticas': 9.0, 'Programación': 8.0, 'Inglés': 8.5},
    'lgomez':   {'Matemáticas': 6.5, 'Programación': 7.0, 'Inglés': 8.0},
    'cruiz':    {'Matemáticas': 7.5, 'Programación': 9.5, 'Inglés': 6.0},
    'dtorres':  {'Matemáticas': 8.0, 'Programación': 6.5, 'Inglés': 7.0},
    'msanchez': {'Matemáticas': 9.5, 'Programación': 9.0, 'Inglés': 9.0}
}

# INPUT / PROCESS - Login con reintentos ilimitados
autenticado = False
while not autenticado:
    usuario = input("Usuario: ")
    contrasena = input("Contraseña: ")

    if usuario in usuarios and usuarios[usuario]['password'] == contrasena:
        autenticado = True
    else:
        print("Usuario o contraseña incorrectos. Intente de nuevo.")

# PROCESS - Determinar el rol
rol = usuarios[usuario]['rol']
nombre = usuarios[usuario]['nombre']

# OUTPUT
print("Bienvenido, " + nombre + " (" + rol + ")")
print()

# PROCESS / OUTPUT - Menú según el rol
if rol == 'alumno':
    print("Boleta de " + nombre)
    for materia in materias:
        print(materia + ": " + str(calificaciones[usuario][materia]))

    aprobadas = set()
    for materia in materias:
        if calificaciones[usuario][materia] >= 8.0:
            aprobadas.add(materia)
    pendientes = set(materias) - aprobadas

    print()
    print("Materias aprobadas: " + str(aprobadas))
    print("Materias pendientes: " + str(pendientes))

elif rol == 'maestro':
    print("Lista de alumnos:")
    for clave in usuarios:
        if usuarios[clave]['rol'] == 'alumno':
            print("- " + clave + ": " + usuarios[clave]['nombre'])

    print()
    alumno = input("Alumno: ")
    materia = input("Materia: ")
    nueva_calificacion = float(input("Nueva calificación: "))

    calificaciones[alumno][materia] = nueva_calificacion
    print("Calificación actualizada.")

elif rol == 'coordinador':
    print("Lista de maestros:")
    for clave in usuarios:
        if usuarios[clave]['rol'] == 'maestro':
            print("- " + clave + ": " + usuarios[clave]['nombre'])

    print()
    print("Lista de materias:")
    for materia in materias:
        print("- " + materia)

    print()
    print("Lista de alumnos y calificaciones:")
    for clave in calificaciones:
        print(usuarios[clave]['nombre'] + ":")
        for materia in materias:
            print("  " + materia + ": " + str(calificaciones[clave][materia]))

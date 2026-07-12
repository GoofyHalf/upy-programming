usuario= "admin"
contraseña = "12345"

u_read= input("Ingrese el usuario: ").lower()
c_read= input("Ingrese la contraseña: ")

if u_read == usuario:
    if c_read== contraseña:
        print("Bienvenido")
    else:
        print("Contraseña incorrecta")
else:
    print("Usuario incorrecto")

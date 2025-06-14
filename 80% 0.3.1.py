#Realice un programa el cual va a permitir generar un menú de ingreso de usuarios 

listaUsuario = []
listasexo = []
listacontra = []

def ingresar_usuarios():
    
    nombre = input("ingrese nombre de usuario: ")
    sexo = input("ingrese Sexo (M o F): ")
    contrasena = input("Ingrese Contraseña (mínimo 8 caracteres): ")
    while len(contrasena) < 8:
        print("la contraseña debe tener minimo 8 caracteres, ingrese nuevamente por favor.")
        contrasena = input("Ingrese Contraseña (mínimo 8 caracteres): ")
    listaUsuario.append(nombre)
    listasexo.append(sexo)
    listacontra.append(contrasena)
    print("el usuario ha sido creado")

def buscar_usuarios():

    usuario = input("ingrese nombre de usuario a encontrar: ")
    if usuario in listaUsuario:
        info = listaUsuario.index(usuario)
        print (f"Usuario: {listaUsuario[info]}, Sexo: {listasexo[info]}, Contraseña: {listacontra[info]}")
    else:
        print("Usuario no existe")

def eliminar_usuario():

    nombre = input("ingrese el nombre del Usuario que desea borrar: ")
    if nombre in listaUsuario:
        eliminar = listaUsuario.index(nombre)
        listaUsuario.pop(eliminar)
        listasexo.pop(eliminar)
        listacontra.pop(eliminar)
        print("el usuario a sido eliminado con exito")
    else:
        print("el usuario no se ha eliminado")
def salir():

    print("Saliendo del programa")
    exit()

def menu():

    while True:
        print("Esta aplicacion es para Registrar, buscar y borrar usuarios")
        print("Opción 1) Registrar Usuario")
        print("Opción 2) Buscar Usuario")
        print("Opción 3) Borrar Usuario")
        print("Opción 4) Salir")
        opcion = int(input("ingrese la opcion que desea realizar: "))
        match opcion:
            case 1:
                ingresar_usuarios()
            case 2:
                buscar_usuarios()
            case 3:
                eliminar_usuario()
            case 4:
                salir()

menu()

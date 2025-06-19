try:

    listaUsuario = []
    listasexo = []
    listacontra = []

    def ingresar_usuarios():
        
        nombre = input("ingrese nombre de usuario: ")
        while nombre.lower() in [usuarios.lower() for usuarios in listaUsuario]:
            print("Nombre de usuario en uso, Por favor intente nuevamente.")
            nombre = input("ingrese nombre de usuario: ")
        sexo = input("ingrese Sexo (M o F): ").upper()
        while sexo != "m" and sexo != "M" and sexo != "f" and sexo != "F":
            if sexo != "m" and sexo != "M" and sexo != "f" and sexo != "F":
                print("Opcion ingresada invalida, Por favor intente nuevamente.")
                sexo = input("ingrese Sexo (M o F): ").upper()
        
        
        contrasena = input("Ingrese Contraseña: ")
        while len(contrasena) < 8 or " " in contrasena or not (any(c.isalpha() for c in contrasena) and any(c.isdigit() for c in contrasena)):
            if len(contrasena) < 8:
                print("La contraseña debe tener minimo 8 caracteres, intente nuevamente.")
                contrasena = input("Ingrese Contraseña: ")
            elif " " in contrasena:
                print("La contraseña no puede tener espacios, intente nuevamente.")
                contrasena = input("Ingrese Contraseña: ")
            elif not (any(c.isalpha() for c in contrasena) and any(c.isdigit() for c in contrasena)):
                print("La contraseña debe tener al menos 1 letra y un numero.")
                contrasena = input("Ingrese Contraseña: ")
            

        listaUsuario.append(nombre)
        listasexo.append(sexo)
        listacontra.append(contrasena)
        print("el usuario ha sido creado")
        print()

    def buscar_usuarios():

        usuario = input("ingrese nombre de usuario a encontrar: ")
        if usuario in listaUsuario:
            info = listaUsuario.index(usuario)
            print (f"Usuario: {listaUsuario[info]} ")
            print(f"Sexo: {listasexo[info]}")
            print(f"Contraseña: {listacontra[info]}")
            print()
        else:
            print("Usuario no existe")
            print()

    def eliminar_usuario():

        nombre = input("ingrese el nombre del Usuario que desea borrar: ")
        if nombre in listaUsuario:
            eliminar = listaUsuario.index(nombre)
            listaUsuario.pop(eliminar)
            listasexo.pop(eliminar)
            listacontra.pop(eliminar)
            print("el usuario a sido eliminado con exito")
            print()
        else:
            print("el usuario no se ha eliminado")
            print()
    def salir():

        print("Saliendo del programa")
        exit()

    def menu():

        while True:
            print("   Menu de Usuarios   ")
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
            if opcion != 1 and opcion != 2 and opcion != 3 and opcion != 4:
                print("Opcion invalida, Por favor intente nuevamente")
                print()

    menu()

except:
    print("Ha ocurrido un problema, cerrando programa.")
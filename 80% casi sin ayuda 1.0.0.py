try:
    listUser = []
    listPassw = []
    listSex = []

    def addUser():

        Username = input("Ingrese nombre de Usuario: ")
        while Username.lower() in [user.lower() for user in listUser]:
            print("El nombre de usuario esta en uso. Por favor, intente nuevamente.")
            Username = input("Ingrese nombre de Usuario: ")
        
        Sex = input("Ingrese Sexo (M/F): ").upper()
        while Sex != "M" and Sex != "F":
            print("Opcion no valida, intente nuevamente.")
            Sex = input("Ingrese Sexo (M/F): ").upper()

        Passw = input("ingrese contraseña: ")
        while len(Passw) < 8 or " " in Passw or not (any(c.isalpha() for c in Passw) and any(c.isdigit() for c in Passw)):
            if len(Passw) < 8:
                print("La contraseña debe tener minino 8 digitos, intente nuevamente.")
            
            elif " " in Passw:
                print("La contraseña no puede llevar espacio, intente nuevamente.")
            
            elif not (any(c.isalpha() for c in Passw) and any(c.isdigit() for c in Passw)):
                print("La contraseña debe contener al menos una letra y al menos un numero, intente nuevamente")
            Passw = input("ingrese contraseña: ")
        
        listUser.append(Username)
        listPassw.append(Passw)
        listSex.append(Sex)

        print("Usuario Creado Exitosamente.")
        print()

    def SearchUser():
        while True:

            Username = input("ingrese nombre de usuario: ")
        
            if Username in listUser:
                search = listUser.index(Username)
                print()
                print(f"Nombre De Usuario: {listUser[search]}")
                print(f"Sexo: {listSex[search]}")
                print(f"Contraseña: {listPassw[search]}")
                print()
                print("desea seguir buscando?")
                decision = input("Si/No: ").lower()
                while True:
                    if decision == "si":
                        return SearchUser()
                    elif decision == "no":
                        print()
                        break
                    else:
                        print("opcion invalida")
                        print("desea seguir buscando?")
                        decision = input("Si/No: ").lower()
            elif Username not in listUser:
                print("Usuario no encontrado. ¿Desea buscar nuevamente?")
                decision = input("Si/No: ").lower()
                while True:
                    if decision == "si":
                        return SearchUser()
                    elif decision == "no":
                        print()
                        break 
                    else:
                        print("opcion invalida intente nuevamente")
                        decision = input("Si/No: ").lower()
            break
    def DeleteUser():
        
        name = input("ingrese nombre que desea borrar: ")
        if name in listUser:
            delete = listUser.index(name)
            listUser.pop(delete)
            listSex.pop(delete)
            listPassw.pop(delete)
            print("usuario ha sido borrado con exito")
            print()
        elif name not in listUser:
            print("El usuario no ha sido encontrado. Desea intentar nuevamente?")
            decision = input("Si/No: ").lower()
            while True:
                if decision=="si":
                    return DeleteUser()
                elif decision=="no":
                    print()
                    break
                else:
                    print("opcion invalida intente nuevamente")
                    decision = input("Si/No: ").lower()
    def menu():
        while True:
            print("---Menu de Usuarios---")
            print("1. Agregar Usuarios")
            print("2. Buscar Usuarios")
            print("3. Eliminar Usuarios")
            print("4. Salir")
            decision=input("Ingrese la opcion que desea usar: ")
            match decision:
                case "1":
                    addUser()
                case "2":
                    SearchUser()
                case "3":
                    DeleteUser()
                case "4":
                    print("Saliendo del programa")
                    break
            if decision != "1" and decision != "2" and decision != "3" and decision != "4":
                print("Opcion no valida, intente nuevamente.")
                print()
    menu()
except:
    print("cerrando")
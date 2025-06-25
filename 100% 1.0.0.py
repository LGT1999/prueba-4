try:
    listUser = []
    listPassw = []
    listSex = []

    def addUser():

        userName = input("Ingrese nombre de usuario: ")
        while userName.lower() in [user.lower() for user in listUser]:
            print("Usuario ya existe. Intente otro.")
            userName = input("Ingrese nombre de usuario: ")
        
        sex = input("Ingrese Sexo: ").upper()
        while sex != "M" and sex != "F":
            print("Debe ingresar M o F solamente. Intente de nuevo.")
            sex = input("Ingrese Sexo): ").upper()

        passW = input("ingrese contraseña: ")
        while len(passW) < 8 or " " in passW or not (any(c.isalpha() for c in passW) and any(c.isdigit() for c in passW)):
            if len(passW) < 8:
                print("La contraseña debe tener un minino de 8 digitos")
            
            elif " " in passW:
                print("La contraseña no puede llevar espacio")
            
            elif not (any(c.isalpha() for c in passW) and any(c.isdigit() for c in passW)):
                print("La contraseña debe contener al menos 1 letra y al menos 1 numero")

            passW = input("ingrese contraseña: ")

        print("Contraseña valida.")
        
        listUser.append(userName)
        listPassw.append(passW)
        listSex.append(sex)

        print("Usuario ingresado con exito!!")
        print()

    def SearchUser():
        while True:

            userName = input("Ingrese usuario a buscar: ")
        
            if userName in listUser:
                search = listUser.index(userName)
                print()
                print(f"El sexo del usuario es: {listSex[search]} y la contraseña es: {listPassw[search]}")
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
            elif userName not in listUser:
                print("Usuario no se encuentra. ¿Desea buscar nuevamente?")
                decision = input("Si/No: ").lower()
                while True:
                    if decision == "si":
                        return SearchUser()
                    elif decision == "no":
                        print()
                        break 
                    else:
                        print("Opcion invalida. Intente nuevamente")
                        decision = input("Si/No: ").lower()
            break
    def DeleteUser():
        
        name = input("ingresar usuario a buscar: ")
        if name in listUser:
            delete = listUser.index(name)
            listUser.pop(delete)
            listSex.pop(delete)
            listPassw.pop(delete)
            print("Usuario eliminado!")
            print()
        elif name not in listUser:
            print("No se puedo eliminar usuario!. Desea intentar nuevamente?")
            decision = input("Si/No: ").lower()
            while True:
                if decision=="si":
                    return DeleteUser()
                elif decision=="no":
                    print()
                    break
                else:
                    print("Opcion invalida. Intente nuevamente")
                    decision = input("Si/No: ").lower()
    def menu():
        while True:
            print("MENU PRINCIPAL")
            print("1. Ingresar usuario.")
            print("2. Buscar Usuario.")
            print("3. Eliminar Usuario.")
            print("4. Salir.")
            print()
            decision=input("Ingrese opción: ")
            match decision:
                case "1":
                    addUser()
                case "2":
                    SearchUser()
                case "3":
                    DeleteUser()
                case "4":
                    print("Programa terminado...")
                    break
            if decision != "1" and decision != "2" and decision != "3" and decision != "4":
                print("Debe ingresar una opción válida!!")
                print()
    menu()
except:
    print("Ha ocurrido un error.")  
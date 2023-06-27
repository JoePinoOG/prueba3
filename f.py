
def opcion1(njs,ruts,fcs,ct,cls,idp,listacorreo):
    while True:
        try:
            nombre=input("ingrese un nombre: ")
            validar=validarletras(nombre)
            if validar==True and len(nombre)>=2:
                njs.append("nombre")
                break
            else:
                print("error ingrese un nombre valido")
        except:
            print("error")
    while True:
        try:
            rut=int(input("ingrese el rut: "))
            ruts.append(rut)
            break
        except:
            print("error")
    while True:
        try:
            fc=int(input("ingrese año de cumpleaños: "))
            if fc>1937:
                fcs.append(fc)
                break
        except:
            print("error")
    while True:
        try:
            cat=input("ingrese su categoria plata bronce u oro: ")
            if cat=="plata" or "bronce" or "oro":
                ct.append(cat)
                break
            else:
                print("error")

        except:
            print("error")
    while True:
        try:
            cel=int(input("ingrese el numero de celular: "))
            celu=str(cel)
            if len(celu)==9:
                cls.append(cel)
                break
            else:
                print("error")
        except:
            print("error")
    while True:
        try:
            correo=input("ingrese su correo: ")
            if len(correo)>=6:
                listacorreo.append(correo)
                break
            else:
                print("error")
        except:
            print("error")

    while True:
        try:
            par=input("ingrese su identificador de pareja:")
            idp.append(par)
            break    
        except:
            print("error")

def opcion2(njs,ruts,fcs,ct,cls,idp,listacorreo):
    while True:
        try:
            rut=int(input("ingrese el rut que desea buscar: "))
            if rut:
                for x in range(len(ruts)):
                    pos=x
                    print(f"{ruts[pos]},{njs[pos]},{ruts[pos]},{fcs[pos]},{ct[pos]},{cls[pos]},{idp[pos]},{listacorreo[pos]}")
                    break
            else:
                print("error")


        except:
            print("error")
def opcion3(njs,ruts,fcs,ct,cls,idp,listacorreo):
    while True:
        try:
            pareja=input("ingrese el id de pareja que desea buscar: ")
            if pareja==idp:
                for x in range(len(idp)):
                    pos=x
                    print(f"{ruts[pos]},{njs[pos]},{ruts[pos]},{fcs[pos]},{ct[pos]},{cls[pos]},{idp[pos]},{listacorreo[pos]}")
                    break
            else:
                print("error")
        except:
            print("error1")

def validarletras(nombre):
    letra=False
    numeros=["1","2","3","4","5","6","7","8","9","0"]
    for x in nombre:
        for y in numeros:
            if x==y:
                letra=True
        if letra==True:
            return False
        else:
            return True
        
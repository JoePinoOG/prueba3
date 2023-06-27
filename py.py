import f as fn
#hay validacion de 9 digitos en el numero de cel
#error en la 3 pk se repiten datos:(
njs=[]
ruts=[]
fcs=[]
ct=[]
cls=[]
idp=[]
listacorreo=[]
op=0
while op!=4:
    print("1.grabar")
    print("2.buscar")
    print("3.mostrar parejas")
    print("4.salir")
    try:
        op=int(input("ingrese una opcion:"))
        if op==1:
            fn.opcion1(njs,ruts,fcs,ct,cls,idp,listacorreo)
            
        if op==2:
            fn.opcion2(njs,ruts,fcs,ct,cls,idp,listacorreo)
           
        if op==3:
            fn.opcion3(njs,ruts,fcs,ct,cls,idp,listacorreo)
    except:
        print("error")

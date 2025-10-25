import os
os.system("cls")
total=0
respuesta = "s"

while  respuesta.lower()=="s" :

    print("x"*30)
    print("Cafecito".center(30,"-"))
    print("x"*30)
    print("1.Cafe.........s/.5.0")
    print("2.Sandwich.....s/.4.0")
    print("3.Jugo.........s/.3.0")
    print("4.Infusion.....s/.2.0")
    print("5.Te...........s/.1.0")
    print("6.Salir0")
    orden=int(input("Elegir una opcion"))
    if orden >=1 and orden <=5 :
        cantidad=int(input("Que cantidad deseas?"))
        if orden == 1 :
            subtotal=cantidad * 5
        elif orden == 2 :
            subtotal=cantidad * 4
        elif orden == 3 :
            subtotal=cantidad * 3
        elif orden == 4 :
            subtotal=cantidad * 2
        elif orden == 5 :
            subtotal=cantidad * 1
                
        total += subtotal + total
    elif orden == "6":
        print("Gracias")
        break
    else:
        print("OPcion incorrecta")

   
    respuesta=input("DEsea agregar algo mas? S/N")

    print("x"*30)
    print("Total a pagar: ", total)
    print("x"*30)
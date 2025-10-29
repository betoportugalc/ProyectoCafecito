import os
os.system("cls")
total = 0
respuesta = "s"

while respuesta.lower() == "s": #lower para poner todo en minusculo

    print("Cafecito".center(30, "-"))
    print("1.Cafe.........s/.5.0")
    print("2.Sandwich.....s/.4.0")
    print("3.Jugo.........s/.3.0")
    print("4.Infusion.....s/.2.0")
    print("5.Te...........s/.1.0")
    print("6.Salir")

    orden = int(input("Elegir una opcion: "))

    if orden >= 1 and orden <= 5:
        cantidad = int(input("Que cantidad deseas?: "))

        if orden == 1:
            subtotal = cantidad * 5
        elif orden == 2:
            subtotal = cantidad * 4
        elif orden == 3:
            subtotal = cantidad * 3
        elif orden == 4:
            subtotal = cantidad * 2
        elif orden == 5:
            subtotal = cantidad * 1

        total += subtotal
        print("Productos agregados correctamente")
        print("Subtotal:", subtotal)
        print("Total acumulado:", total)

        respuesta = input("Desea agregar algo mas? (S/N): ") #puede usarse mayuscula o minuscula

    elif orden == 6:
        print("\nPedido cancelado por el cliente.")
        total = 0
        respuesta = "n"
        break #termina bucle

    else:
        print("Opcion incorrecta")

if total > 0:
    print("\nTotal del pedido: S/.", total)
    confirmar = input("Confirmar pedido y enviar a cocina? (S/N): ")
    if confirmar.lower() == "s":
        print("\nPedido confirmado y enviado a cocina.")
        print("Estado: PEDIDO RECIBIDO EN COCINA")
    else:
        print("\nPedido cancelado antes de enviar.")
else:
    print("No se realizo ningun pedido.")


print("\nfin del proceso")

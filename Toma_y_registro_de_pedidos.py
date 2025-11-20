def Toma_y_registro_de_pedidos():

    total = 0
    respuesta = "s"

    while respuesta.lower() == "s":  # Lower para poner todo en minúscula

        print("Cafecito".center(30, "-"))
        print("1. Café......... S/.5.0")
        print("2. Sándwich..... S/.4.0")
        print("3. Jugo......... S/.3.0")
        print("4. Infusión..... S/.2.0")
        print("5. Té........... S/.1.0")
        print("6. Salir")

        orden = int(input("Elegir una opción: "))

        if 1 <= orden <= 5:
            cantidad = int(input("¿Qué cantidad deseas?: "))

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
            print("Producto agregado correctamente")
            print("Subtotal:", subtotal)
            print("Total acumulado:", total)

            respuesta = input("¿Desea agregar algo más? (S/N): ")

        elif orden == 6:
            print("\nPedido cancelado por el cliente.")
            total = 0
            respuesta = "n"
            break  # Termina el bucle

        else:
            print("Opción incorrecta")

    # Fuera del while
    if total > 0:
        print("\nTotal del pedido: S/.", total)
        confirmar = input("¿Confirmar pedido y enviar a cocina? (S/N): ")

        if confirmar.lower() == "s":
            print("\nPedido confirmado y enviado a cocina.")
            print("Estado: PEDIDO RECIBIDO EN COCINA")
        else:
            print("\nPedido cancelado antes de enviar.")
    else:
        print("No se realizó ningún pedido.")

    print("\nFin del proceso")

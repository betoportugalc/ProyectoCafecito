def despacho_y_entrgas():
    
    print("-"*40)
    print("MODULO DE DESPACHO Y ENTREGAS".center(40, "-"))
    print("-"*40)
    print("Pedido #01")

    pedido_correcto = input("el pedido correcto? (S/N): ").lower()
    if pedido_correcto=="s" :
        entrega=input("Tipo de entrega:\n" \
                   "1: Presencial\n" \
                   "2: Despacho/Delivery\n")
        if entrega=="1" :
            recojo=input("Notificar al mozo: Pedido Listo\n"
                           "Mozo recogio el pedido?(S/N)").lower()
            if recojo=="s":
                print("Pedido Entregado")
            else:
                print("Registrar incidencia")   
        elif entrega=="2" :
            recojo=input("Repartidor notidicado\n" 
                    "Repartidor recogio el pedido?(S/N)").lower()
            if recojo=="s":
                print("Pedido Entregado")
            else:
                print("Registrar incidencia")

    else :
        print("Notificar a cocina: Pedido incorrecto")

    print("\nFin del proceso de despacho y entregas")
    print("-"*40)

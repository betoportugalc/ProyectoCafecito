
print("-"*40)
print("MODULO DE COCINA".center(40, "-"))
print("-"*40)
print("Pedido #01 en cola")
preparado=input("Iniciar preparacion: (s/n): ").lower()
if preparado == "s" :  
   producto_listo = input("Estado : En preparacion\n Pedido listo? (s/n): ").lower()
   if producto_listo=="s" :
      print("\nEstado : Pedido en Modulo de despacho")
      print("Pedido listo notificado al mozo")
   elif producto_listo=="n" :
      print("Informar al Mozo: Pedido no Listo") 
   else :
      print("Opcion incorreecta")
else: 
   preparado=="n"
   print("Notificar al mozo: Pedido no listo") 

print("\nFin del proceso de cocina")
print("-"*40)

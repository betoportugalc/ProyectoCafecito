import Toma_y_registro_de_pedidos
import Cocina
import despacho_y_entrgas

users = {
    "pedidos": {"user": "pedidos123", "pass": "123"},
    "cocina": {"user": "cocina123", "pass": "123"},
    "despacho": {"user": "despacho123", "pass": "123"},
}

def login(modulo):
    print(f"\n=== LOGIN {modulo.upper()} ===")
    usuario = input("Usuario: ")
    clave = input("Contraseña: ")

    if usuario == users[modulo]["user"] and clave == users[modulo]["pass"]:
        return True
    else:
        print("Usuario o contraseña incorrectos")
        return False

while True:
    print("\n=== MENÚ PRINCIPAL ===")
    print("1. Toma y registro de pedidos")
    print("2. Cocina")
    print("3. Despacho y entregas")
    print("4. Salir")

    opcion = input("Elige una opción: ")

    if opcion == "1":
        if login("pedidos"):
            Toma_y_registro_de_pedidos.Toma_y_registro_de_pedidos()

    elif opcion == "2":
        if login("cocina"):
            Cocina.Cocina()

    elif opcion == "3":
        if login("despacho"):
            despacho_y_entrgas.despacho_y_entrgas()

    elif opcion == "4":
        print("Saliendo...")
        break

    else:
        print("Opción no válida")



   

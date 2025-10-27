Algoritmo Cafecito
    Definir opcion, cantidad Como Entero
    Definir total, subtotal Como Real
    Definir respuesta Como Caracter
	
    total <- 0
    respuesta <- "S"
	
    Repetir
        Escribir "==============================="
        Escribir "          CAFECITO"
        Escribir "==============================="
        Escribir "1. Café ............... S/ 9"
        Escribir "2. Sándwich ........... S/ 7"
        Escribir "3. Galletas ........... S/ 5"
        Escribir "4. Té ................. S/ 4"
		Escribir "5. Infusiones ..........S/ 2.5"
        Escribir "6. Salir"
        Escribir "==============================="
        Escribir "Elija una opción (1-6):"
        Leer opcion
		
        Si opcion >= 1 Y opcion <= 5 Entonces
            Escribir "Ingrese cantidad:"
            Leer cantidad
			
            Segun opcion
                Caso 1:
                    subtotal = cantidad * 9
                Caso 2:
                    subtotal = cantidad * 7
                Caso 3:
                    subtotal = cantidad * 5
                Caso 4:
                    subtotal = cantidad * 4
				Caso 5:
					subtotal = cantidad *2.5
            FinSegun
			
            total = total + subtotal
			
        Sino
            Si opcion = 6 Entonces
                Escribir "Exit"
            Sino
                Escribir "Ingrese nuevamente"
            FinSi
        FinSi
		
        Si opcion <> 6 Entonces
            Escribir "¿Desea agregar otro producto? (S/N):"
            Leer respuesta
        FinSi
		
    Hasta Que opcion = 6 O respuesta = "N" O respuesta = "n"
	
    Escribir "--------------------------------"
	Escribir "TOTAL A PAGAR: S/ ", total
    Escribir "Gracias por su compra"
    Escribir "--------------------------------"
FinAlgoritmo

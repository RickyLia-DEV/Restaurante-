class Restaurante:
    def __init__(self, nombre, capacidad):
        self.nombre = nombre
        self.capacidad = capacidad
        self.reservaciones = []

    def verificar_disponibilidad(self, num_personas):
        if num_personas <= self.capacidad:
            return True
        else:
            return False

    def hacer_reservacion(self, nombre_cliente, num_personas):
        if self.verificar_disponibilidad(num_personas):
            self.reservaciones.append((nombre_cliente, num_personas))
            self.capacidad -= num_personas
            print(f"Reservación realizada para {nombre_cliente} para {num_personas} personas.")
        else:
            print("Lo sentimos, no hay disponibilidad para esa cantidad de personas.")

    def mostrar_reservaciones(self):
        print("Reservaciones:")
        for reserva in self.reservaciones:
            print(f"{reserva[0]} - {reserva[1]} personas")

rylcomida = Restaurante("RyLcomida", 50)

while True:
    print("\nBienvenido al asistente de reservaciones de Restaurante RyLcomida")
    print("1. Verificar disponibilidad")
    print("2. Hacer una reservación")
    print("3. Mostrar reservaciones")
    print("4. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        num_personas = int(input("Ingrese el número de personas: "))
        if rylcomida.verificar_disponibilidad(num_personas):
            print("Hay disponibilidad para esa cantidad de personas.")
        else:
            print("No hay disponibilidad para esa cantidad de personas.")

    elif opcion == "2":
        nombre_cliente = input("Ingrese su nombre: ")
        num_personas = int(input("Ingrese el número de personas: "))
        rylcomida.hacer_reservacion(nombre_cliente, num_personas)

    elif opcion == "3":
        rylcomida.mostrar_reservaciones()

    elif opcion == "4":
        print("Gracias por utilizar el asistente de reservaciones. ¡Buen provecho!")
        break

    else:
        print("Opción inválida. Por favor, seleccione una opción válida.")
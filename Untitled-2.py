nombre = "Fabrizio"
apellido = "Provati"
curso = "4°5"
tarjetan = "123123"
dinero_en_cuenta = 150

def mostrar_menu():
    print("--- MENÚ ---")
    print("a. Datos personales")
    print("b. Lista de productos")
    print("c. Ingresar dinero")
    print("d. Salir del sistema")

def mostrar_datos_personales():
    print("--- DATOS PERSONALES ---")
    print("Nombre:", nombre)
    print("Apellido:", apellido)
    print("Curso:", curso)
    print("Dinero en la cuenta:", dinero_en_cuenta)

def mostrar_lista_productos():
    global dinero_en_cuenta

    print("--- LISTA DE PRODUCTOS ---")
    productos = [
        ("Galletas", 20),
        ("Jugo", 30),
        ("Sanguchito", 50),
        ("Gaseosa", 20),
        ("Agua", 5),
        ("Caramelo", 3),
        ("Lays", 30),
        ("Doritos", 30),
        ("Chocolate", 10),
        ("Chupetin", 5)
    ]

    for pro, producto in enumerate(productos, start=1):
        nombre_producto, precio_producto = producto
        print(f"{pro}. {nombre_producto} - Precio: {precio_producto}")

    codigo_producto = input("Ingrese el número del producto que desea comprar (o 'q' para volver al menú): ")

    while codigo_producto != "q":
        if codigo_producto.isdigit():
            codigo_producto = int(codigo_producto)
            if codigo_producto >= 1 and codigo_producto <= len(productos):
                producto_seleccionado = productos[codigo_producto - 1]
                nombre_producto, precio_producto = producto_seleccionado
                if dinero_en_cuenta >= precio_producto:
                    dinero_en_cuenta -= precio_producto
                    print("Ha comprado", nombre_producto)
                    print("Dinero restante en la cuenta:", dinero_en_cuenta)
                else:
                    print("No tiene suficiente dinero en la cuenta para comprar", nombre_producto)
            else:
                print("Número de producto inválido")

        codigo_producto = input("Ingrese el número del producto que desea comprar (o 'q' para volver al menú): ")

def ingresar_dinero():
    global dinero_en_cuenta
    cantidad = float(input("Ingrese la cantidad de dinero que desea ingresar: "))
    dinero_en_cuenta += cantidad
    print("Se ha ingresado", cantidad, "a la cuenta")
    print("Dinero total en la cuenta:", dinero_en_cuenta)

tarjeta = input("Ingrese el número de la tarjeta (6 dígitos): ")

while tarjeta != tarjetan:
    print("Número de tarjeta inválido. Intente otra vez")
    tarjeta = input("Ingrese el número de la tarjeta (6 dígitos): ")

opcion=""

while opcion != "d":
    mostrar_menu()
    opcion = input("Ingrese la opción que desea seleccionar: ")

    if opcion =="a":
        mostrar_datos_personales()
    elif opcion == "b":
        mostrar_lista_productos()
    elif opcion == "c":
        ingresar_dinero()
    elif opcion == "d":
        print("Saliendo del sistema.")
    else:
        print("Opción inválida. Intente otra vez.")

print("Programa finalizado.")

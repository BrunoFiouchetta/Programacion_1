#punto 1
def crear_archivo_inicial():
    with open("productos.txt", "w") as archivo:
        archivo.write("Lapicera,120.5,30\n")
        archivo.write("Cuaderno,250.0,15\n")
        archivo.write("Mochila,3500.0,8\n")
    print("Archivo creado\n")

# punto 2
def mostrar_productos():
    print("=== PRODUCTOS ===")
    with open("productos.txt", "r") as archivo:
        for linea in archivo:
            datos = linea.strip().split(",")
            print(f"Producto: {datos[0]} | Precio: ${datos[1]} | Cantidad: {datos[2]}")
    print()


# punto 3
def agregar_producto():
    print("=== AGREGAR PRODUCTO ===")
    nombre = input("Nombre: ")
    precio = input("Precio: ")
    cantidad = input("Cantidad: ")
    
    with open("productos.txt", "a") as archivo:
        archivo.write(f"{nombre},{precio},{cantidad}\n")
    
    print(f"Producto agregado\n")

#punto 4
def cargar_productos():
    productos = []
    with open("productos.txt", "r") as archivo:
        for linea in archivo:
            datos = linea.strip().split(",")
            producto = {
                "nombre": datos[0],
                "precio": float(datos[1]),
                "cantidad": int(datos[2])
            }
            productos.append(producto)
    return productos

#punto 5
def buscar_producto(productos):
    print("=== BUSCAR PRODUCTO ===")
    nombre = input("Nombre del producto: ")
    
    for producto in productos:
        if producto["nombre"].lower() == nombre.lower():
            print(f"\nNombre: {producto['nombre']}")
            print(f"Precio: ${producto['precio']}")
            print(f"Cantidad: {producto['cantidad']}\n")
            return
    
    print("Producto no encontrado\n")


# punto 6

def guardar_productos(productos):
    with open("productos.txt", "w") as archivo:
        for p in productos:
            archivo.write(f"{p['nombre']},{p['precio']},{p['cantidad']}\n")
    print("Archivo actualizado\n")


#programa principal

crear_archivo_inicial()
mostrar_productos()
agregar_producto()

productos = cargar_productos()

buscar_producto(productos)
guardar_productos(productos)
mostrar_productos()

print("Programa completado")
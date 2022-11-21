p1=[1,"Pokemon X",33.77]
p2=[2,"Nintendo XL",203]
p3=[3,"Mario Kart 7",27.58]
p4=[4,"PlayStation 4",348.00]
p5=[5,"FIFA 16",51.19]
productos = [p1, p2, p3, p4, p5]

def mostrar_menu_principal():
    print("Tienda Amazon.\nA continuacion estan los productos:")
    #for i in productos:
    #    print(f"Producto {i[0]}: {i[1]}. Precio: ${i[2]}")
    print("Seleccione el producto que desea y la cantidad.")

def navegar():
    listaProductos = [0, 0, 0, 0, 0]
    precios = [0, 0, 0, 0, 0]
    while True:
        seleccion = input()
        if seleccion == "checkout":
            break
        elif seleccion == "ver":
            mostrar_menu_principal()
        else:
            producto, unidades = (int(x) for x in seleccion.split(","))
            listaProductos[producto-1] += unidades
    for i, j in enumerate(listaProductos):
        precios[i] = productos[i][2]*j
    checkout = sum(precios)
    if listaProductos[0] > 0 and listaProductos[1] > 0 and listaProductos[2] > 0:
        checkout *= 0.8
    if listaProductos[3] > 0 and listaProductos[4] > 0:
        checkout *= 0.85
    checkout = round(checkout, 1)
    print(checkout)


navegar()

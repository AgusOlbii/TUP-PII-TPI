import libro

# Crear una lista vacía para almacenar los libros
libros = []

# Añadir los diccionarios a la lista
libros.append(libro.libro1)
libros.append(libro.libro2)
libros.append(libro.libro3)


def ejemplares_prestados():
    print("Los codigos de los libros registados son: \n")
    codLibros = list(map(lambda x: x['cod'], libros))
    for codigos in codLibros:
        print(codigos)
    codigoPrestados=str(input("Ingrese el codigo para buscar la cantidad de libros prestada:\n"))
    encontrado=False
    for libro in libros:
        if libro['cod']==codigoPrestados:
            if libro['cant_ej_pr']<1:
                print(f"Titulo: {libro['titulo']}\nAutor: {libro['autor']}\n")
                print("No tiene ejemplares prestados!")
            else:
                print(f"Titulo: {libro['titulo']}\nAutor: {libro['autor']}\n")
                print(f"Ejemplares prestados: {libro['cant_ej_pr']}")
            encontrado=True    
    if not encontrado:
        print("El codigo es inexistente.")
    

def registrar_nuevo_libro():
    nuevo_libro()
    

def eliminar_ejemplar_libro():
    codEliminar=str(input("Ingrese el codigo del ejemplar para eliminarlo: \n"))
    for libro in libros:
        if libro['cod'] == codEliminar:
            libros.remove(libro)
            print("Eliminacion completa!")
            bandera=True
            break
        else:
            bandera=False
    if bandera != True:
        print("Codigo inexistente")

    

def prestar_ejemplar_libro():
    buscarLibro = input("Ingrese el codigo del ejemplar buscado:\n")
    encontrado=False
    for libro in libros:
        if libro['cod'] == buscarLibro:
            print(f'Autor: {libro["autor"]}\nTítulo: {libro["titulo"]}\nCantidad de ejemplares disponibles: {libro["cant_ej_ad"]}\n')
            if libro['cant_ej_ad'] >= 1:
                opcion = int(input("1-confirmar prestamo\nOtro digito- cancelar prestamo\n"))
                if opcion == 1:
                    libro['cant_ej_ad']= libro['cant_ej_ad']-1
                    libro['cant_ej_pr']= libro['cant_ej_pr']+1
                    print("Se confirmo el prestamo!")
                else:
                    print("Ha cancelado el prestamo")
            else:
                print("No quedan ejemplares para prestar, lo sentimos!") 
            encontrado=True     
    if not encontrado:
        print("No se encontro ningun libro con el codigo ingresado")  
    

def devolver_ejemplar_libro():
    buscarLibro = input("Ingrese el codigo del ejemplar que quiere devolver:\n")
    encontrado=False
    for libro in libros:
        if libro['cod'] == buscarLibro:
            print(f"Libros prestados: {libro['cant_ej_pr']}")
            if libro['cant_ej_pr'] >= 1:        #inicializar opcion si tira errores
                opcion = int(input("1-confirmar devolucion\nOtro digito- cancelar la misma\n"))
                if opcion == 1:
                    libro['cant_ej_ad']= libro['cant_ej_ad']+1
                    libro['cant_ej_pr']= libro['cant_ej_pr']-1
                    print("Se confirmo la devolucion! Muchas gracias!")
                else:
                    print("Ha cancelado la devolucion")
            else:
                print("No tenemos ejemplares prestados, Vuelva pronto!")      
            encontrado=True
    if not encontrado:
        print("No se encontro ningun libro con el codigo ingresado")  
    
 
def nuevo_libro():
    nuevoLibroLista=libro.nuevo_libro()
    libros.append(nuevoLibroLista)
    
import libro as l

# Crear una lista vacía para almacenar los libros
libros = []

# Añadir los diccionarios a la lista
libros.append(l.libro1)
libros.append(l.libro2)
libros.append(l.libro3)

'''ibro1 = {'cod': 'CRBJsAkS', 'cant_ej_ad': 3, 'cant_ej_pr': 1, "titulo": "Cien años de soledad", "autor": "Gabriel García Márquez"}
libro2 = {'cod': 'QgfV4j3c', 'cant_ej_ad': 4, 'cant_ej_pr': 2, "titulo": "El principito", "autor": "Antoine de Saint-Exupéry"}
libro3 = {'cod': 'adOd09UE', 'cant_ej_ad': 1, 'cant_ej_pr': 0, "titulo": "El código Da Vinci", "autor": '''

def ejemplares_prestados():
    codigoPrestados=str(input("Ingrese el codigo para buscar la cantidad de libros prestada:\n"))
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
    return

def registrar_nuevo_libro():
    nuevo_libro = l.nuevo_libro()
    #completar
    return None

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

    return None

def prestar_ejemplar_libro():
    buscarLibro = input("Ingrese el codigo del ejemplar buscado:\n")
    for libro in libros:
        if libro['cod'] == buscarLibro:
            print(f'Autor: {libro["autor"]}, Título: {libro["titulo"]}, Cantidad de ejemplares disponibles: {libro["cant_ej_ad"]}')
            if libro['cant_ej_ad'] >= 1:
                eleccion=input("1-confirmar prestamo\nOtro digito para cancelar prestamo\n")
                if eleccion == 1:
                    libro['cant_ej_ad']= libro['cant_ej_ad']-1
                    libro['cant_ej_pr']= libro['cant_ej_pr']+1
                else:
                    print("Ha cancelado el prestamo")
            else:
                print("No quedan ejemplares para prestar, lo sentimos!")      
        else:
            print("No se encontro ningun libro con el codigo ingresado")  
    return None

def devolver_ejemplar_libro():
    #completar
    return None

def nuevo_libro():
    l.nuevo_libro()
    libros.append(l.libro4)
    return None

ejemplares_prestados()
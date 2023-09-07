import cod_generator as gen
# Crear un diccionario para cada libro
libro1 = {'cod': 'CRBJsAkS', 'cant_ej_ad': 3, 'cant_ej_pr': 1, "titulo": "Cien años de soledad", "autor": "Gabriel García Márquez"}
libro2 = {'cod': 'QgfV4j3c', 'cant_ej_ad': 4, 'cant_ej_pr': 2, "titulo": "El principito", "autor": "Antoine de Saint-Exupéry"}
libro3 = {'cod': 'adOd09UE', 'cant_ej_ad': 1, 'cant_ej_pr': 0, "titulo": "El código Da Vinci", "autor": "Dan Brown"}

def nuevo_libro():
    nuevoLibro={}
    nuevoCodigo=generar_codigo()
    cantidadAdquirida=int(input("Ingrese la cantidad de libros adquiridos:\n"))
    cantidadPrestada=int(input("Ingrese la cantidad de libros prestados: \n"))
    nuevoTitulo=str(input("Ingrese el titulo del libro nuevo: \n"))
    nuevoAutor=str(input("Ingrese el nombre del autor del libro: \n"))
    
    nuevoLibro={'cod':nuevoCodigo,'cant_ej_ad': cantidadAdquirida,'cant_ej_pr':cantidadPrestada,'titulo':nuevoTitulo,'autor':nuevoAutor}
    print(f'Este es nuevo libro: \n{nuevoLibro}')
    return nuevoLibro

def generar_codigo():
    codigo=gen.generar()
    print(f'Este es CODIGO:\n{codigo}')
    return codigo

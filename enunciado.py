'''Enunciado
La Biblioteca “José Manuel Estrada” necesita un sistema para gestionar los préstamos y
devoluciones de las personas de la ciudad.
En una biblioteca se cuentan con registros de los libros existentes, con la siguiente información
a saber:
Código de libre (string)
Cantidad de ejemplares adquiridos(entero)
Cantidad de ejemplares prestados(entero)
Autor (string)
Título (string)
Lista “libros” de tipo diccionario.
Al iniciar el sistema se muestra un menú que permite al bibliotecario elegir alguna de las
siguientes opciones:
1) Gestionar Préstamo
El bibliotecario debe ingresar el código del libro. Se valida que el mismo exista y en caso
contrario se muestra error. Si se ingresa un código correcto se muestra en pantalla el
autor, el título y la cantidad de ejemplares disponibles.
Si no quedan ejemplares para prestar se muestra un cartel aclaratorio. Si quedan
ejemplares para prestar, se muestra un mensaje para confirmar el préstamo, se
actualiza la cantidad de ejemplares disponibles.
2) Gestionar devolución
El bibliotecario debe ingresar el código del libro. Se valida que el mismo exista y tenga
ejemplares prestados, en caso contrario se muestra error.
Para confirmar la devolución se muestra un mensaje y se actualiza la cantidad de
ejemplares prestados.
3) Registrar nuevo libro
Si se adquieren nuevos libros los mismos deben registrarse. Agregar un libro y la
cantidad de sus ejemplares adquiridos a la lista “libros”. Para el libro registrado se
generará el código automáticamente y se informará el mismo con un resumen de los
datos registrados.
4) Eliminar ejemplar
Si debe sacarse de circulación un ejemplar, debe actualizarse la cantidad de ejemplares
adquiridos del libro. El bibliotecario debe ingresar el código del libro. Se valida que el
mismo exista y se actualiza la cantidad de ejemplares adquiridos, en caso contrario se
muestra error.
5) Mostrar ejemplares prestados
De la lista “libros” mostrar la cantidad de ejemplares prestados de cada uno. En caso de
no tener ningún ejemplar prestado mostrar un mensaje.
6) Salida
Finaliza el bucle.
El sistema se ejecuta hasta que el usuario presione la opción 6 del menú. Muestra un mensaje
de despedida.'''

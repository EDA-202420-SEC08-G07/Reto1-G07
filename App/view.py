import sys
import App.logic as logic
import time
import csv
import sys
import os
import json
from DataStructures.List import single_linked_list as lt
from DataStructures.List import array_list as ar

def new_logic():
    """
        Se crea una instancia del controlador
    """
    control = logic.new_logic()
    return control

def print_menu():
    print("Bienvenido")
    print("1- Cargar información")
    print("2- Ejecutar Requerimiento 1")
    print("3- Ejecutar Requerimiento 2")
    print("4- Ejecutar Requerimiento 3")
    print("5- Ejecutar Requerimiento 4")
    print("6- Ejecutar Requerimiento 5")
    print("7- Ejecutar Requerimiento 6")
    print("8- Ejecutar Requerimiento 7")
    print("9- Ejecutar Requerimiento 8 (Bono)")
    print("0- Salir")
    
data_dir = os.path.dirname(os.path.realpath('__file__')) + '/Data/'

def load_data(control, data_dir):
    """
    Carga los datos
    """
    catalog=logic.load_data(control, data_dir)
    print(print_first_and_last_movies(catalog))
    return catalog

def print_first_and_last_movies(catalog):
    """
    Imprime las primeras 5 peliculas y las ultimas 5 peliculas cargadas
    """
    first, last=logic.get_first_last_movies(catalog)
    print("\nLas primeras peliculas de la lista son: \n")
    for movie in first:
        print(movie)
    
    print("\Las ultimas peliculas de la lista son: \n")
    for movie in last:
        print(movie)
    return None



def print_data(control, id):
    """
        Función que imprime un dato dado su ID
    """
    id_a_buscar=input("Ingrese el id de la pelicula que desea buscar: ")
    print(logic.get_data(control,id_a_buscar))
    return None

def print_req_1(control):
    """
        Función que imprime la solución del Requerimiento 1 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 1
    catalog=logic.load_data(control, data_dir)
    min_runtime = input("Ingrese el tiempo minimo desde el cual desea buscar: ")
    ultima_pelicula, count = logic.req_1(catalog, min_runtime)
    
    print("El numero total de peliculas que cumplen con este criterio es de: "+str(count))
    print("La ultima pelicula que cumple con este criterio es: ")
    print(ultima_pelicula)


def print_req_2(control):
    """
        Función que imprime la solución del Requerimiento 2 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 2
    pass


def print_req_3(control):
    """
        Función que imprime la solución del Requerimiento 3 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 3
    pass


def print_req_4(control):
    """
        Función que imprime la solución del Requerimiento 4 en consola
    """
    catalog=logic.load_data(control, data_dir)
    fecha_inicial=input("Ingrese la fecha donde quiere que inicie la busqueda, formato YYYY-MM-DD: ")
    fecha_final=input("Ingrese la fecha donde quiere que acabe la busqueda, formato YYYY-MM-DD: ")
    estado=input("Ingrese el estado de la pelicula que desea buscar: ")
    tot_peliculas, duracion_promedio, lista=logic.req_4(catalog, fecha_inicial, fecha_final, estado)
    
    print("El total de peliculas es de: "+  str(tot_peliculas))
    print("La duracion promedio de las peliculas es de: "+ str(round(duracion_promedio, 2)))
    if tot_peliculas>20:
        print("Las primeras 5 peliculas entre las fechas son: ")
        for i in range(5):
            print(lista[i])
        print("Las ultimas 5 peliculas entre las fechas son: ")
        for k in range(len(lista)-5, len(lista)):
            print(lista[k])
    else:
        print("La lista de peliculas sacadas entre las fechas son: ")
        for pelicula in lista:
            print(pelicula)
    
    return None


def print_req_5(control, catalog):
    """
        Función que imprime la solución del Requerimiento 5 en consola
    """
    # TODO
    pass
    
def print_req_6(control):
    """
        Función que imprime la solución del Requerimiento 6 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 6
    pass


def print_req_7(control):
    """
        Función que imprime la solución del Requerimiento 7 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 7
    pass


def print_req_8(control):
    """
        Función que imprime la solución del Requerimiento 8 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 8
    pass


# Se crea la lógica asociado a la vista
control = new_logic()

# main del ejercicio
def main():
    """
    Menu principal
    """
    working = True
    #ciclo del menu
    while working:
        print_menu()
        inputs = input('Seleccione una opción para continuar\n')
        if int(inputs) == 1:
            print("Cargando información de los archivos ....\n")
            data = load_data(control, data_dir)
        elif int(inputs) == 2:
            print_req_1(control)

        elif int(inputs) == 3:
            print_req_2(control)

        elif int(inputs) == 4:
            print_req_3(control)

        elif int(inputs) == 5:
            print_req_4(control)

        elif int(inputs) == 6:
            print_req_5(control)

        elif int(inputs) == 7:
            print_req_6(control)

        elif int(inputs) == 8:
            print_req_7(control)

        elif int(inputs) == 9:
            print_req_8(control)

        elif int(inputs) == 0:
            working = False
            print("\nGracias por utilizar el programa") 
        else:
            print("Opción errónea, vuelva a elegir.\n")
    sys.exit(0)

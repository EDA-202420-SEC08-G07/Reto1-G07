import sys
import App.logic as logic
import time
import csv
import sys
import os
import json
from DataStructures.List import single_linked_list as lt
from DataStructures.List import array_list as lt
from tabulate import tabulate


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
    first, last, total=logic.get_first_last_movies(catalog)
    print("Se cargo un total de "+str(total)+" peliculas")
    print("\nLas primeras peliculas de la lista son: \n")
    for movie in first:
        tabla_pelicula = [[k, v] for k, v in movie.items()]
        print(tabulate(tabla_pelicula, headers=["Campo", "Valor"], tablefmt="pretty"))
    
    print("\nLas ultimas peliculas de la lista son: \n")
    for movie in last:
        tabla_pelicula = [[k, v] for k, v in movie.items()]
        print(tabulate(tabla_pelicula, headers=["Campo", "Valor"], tablefmt="pretty"))
    return None



def print_data(control, id):
    """
        Función que imprime un dato dado su ID
    """
    id_a_buscar=input("Ingrese el id de la pelicula que desea buscar: ")
    print(logic.get_data(control,id_a_buscar))
    return None

def print_req_1(control, data):
    """
        Función que imprime la solución del Requerimiento 1 en consola
    """
    catalog=data
    min_runtime = float(input("Ingrese el tiempo minimo desde el cual desea buscar: "))
    ultima_pelicula, count = logic.req_1(catalog, min_runtime)
    tabla_pelicula = [[k, v] for k, v in ultima_pelicula.items()]
    print("El numero total de peliculas que cumplen con este criterio es de: "+str(count))
    print("La ultima pelicula que cumple con este criterio es: ")
    print(tabulate(tabla_pelicula, headers=["Campo", "Valor"], tablefmt="pretty"))


def print_req_2(control, data):
    """
        Función que imprime la solución del Requerimiento 2 en consola
    """
    catalog=data
    idioma_usuario = input("Ingrese el idioma (en, n, fr, zh, etc.) desde el cual desea buscar: ")
    ultima_pelicula, count = logic.req_2(catalog, idioma_usuario)
    tabla_pelicula = [[k, v] for k, v in ultima_pelicula.items()]
    print("El numero total de peliculas que cumplen con este criterio es de: "+str(count))
    print("La ultima pelicula que cumple con este criterio es: ")
    print(tabulate(tabla_pelicula, headers=["Campo", "Valor"], tablefmt="pretty"))



def print_req_3(control, data):
    """
        Función que imprime la solución del Requerimiento 3 en consola
    """
    catalog=data
    fecha_inicial=input("Ingrese la fecha donde quiere que inicie la busqueda, formato YYYY-MM-DD: ")
    fecha_final=input("Ingrese la fecha donde quiere que acabe la busqueda, formato YYYY-MM-DD: ")
    idioma=input("Ingrese el idioma del cual quiere saber la pelicula (en, it, fr): ")
    tot_peliculas, duracion_promedio, lista_primeras, lista_ultimas=logic.req_3(catalog, idioma, fecha_inicial, fecha_final)
    
    print("El total de peliculas en "+idioma+" es de: "+  str(tot_peliculas))
    print("La duracion promedio de las peliculas en "+idioma+" es de: "+ str(round(duracion_promedio, 2)))
    if tot_peliculas>20:
        print("Las primeras 5 peliculas entre las fechas son: ")
        for i in lista_primeras:
            tabla_pelicula = [[k, v] for k, v in i.items()]
            print(tabulate(tabla_pelicula, headers=["Campo", "Valor"], tablefmt="pretty"))
            
        print("Las ultimas 5 peliculas entre las fechas son: ")
        for k in lista_ultimas:
            tabla_pelicula = [[k, v] for k, v in k.items()]
            print(tabulate(tabla_pelicula, headers=["Campo", "Valor"], tablefmt="pretty"))
    else:
        print("La lista de peliculas sacadas entre las fechas son: ")
        for pelicula in lista_primeras:
            tabla_pelicula = [[k, v] for k, v in pelicula.items()]
            print(tabulate(tabla_pelicula, headers=["Campo", "Valor"], tablefmt="pretty"))
    
    return None
def print_req_4(control, data):
    """
        Función que imprime la solución del Requerimiento 4 en consola
    """
    catalog=data
    fecha_inicial=input("Ingrese la fecha donde quiere que inicie la busqueda, formato YYYY-MM-DD: ")
    fecha_final=input("Ingrese la fecha donde quiere que acabe la busqueda, formato YYYY-MM-DD: ")
    estado=input("Ingrese el estado de la pelicula que desea buscar: ")
    tot_peliculas, duracion_promedio, lista_primeras, lista_ultimas=logic.req_4(catalog, fecha_inicial, fecha_final, estado)
    
    print("El total de peliculas es de: "+  str(tot_peliculas))
    print("La duracion promedio de las peliculas es de: "+ str(round(duracion_promedio, 2)))
    if tot_peliculas>20:
        print("Las primeras 5 peliculas entre las fechas son: ")
        for i in lista_primeras:
            tabla_pelicula = [[k, v] for k, v in i.items()]
            print(tabulate(tabla_pelicula, headers=["Campo", "Valor"], tablefmt="pretty"))
            
        print("Las ultimas 5 peliculas entre las fechas son: ")
        for k in lista_ultimas:
            tabla_pelicula = [[k, v] for k, v in k.items()]
            print(tabulate(tabla_pelicula, headers=["Campo", "Valor"], tablefmt="pretty"))
    else:
        print("La lista de peliculas sacadas entre las fechas son: ")
        for pelicula in lista_primeras:
            tabla_pelicula = [[k, v] for k, v in pelicula.items()]
            print(tabulate(tabla_pelicula, headers=["Campo", "Valor"], tablefmt="pretty"))
    
    return None


def print_req_5(control):
    """
        Función que imprime la solución del Requerimiento 5 en consola
    """
    # TODO
    catalog= logic.load_data(control, data_dir)
    fecha_inicial=input("Ingrese la fecha donde quiere que inicie la busqueda, formato YYYY-MM-DD: ")
    fecha_final=input("Ingrese la fecha donde quiere que acabe la busqueda, formato YYYY-MM-DD: ")
    duracion_min= float(input("Ingrese el tiempo minimo de la pelicula que desea buscar: "))
    duracion_max = float(input("Ingrese el tiempo maximo de la pelicula que desea buscar: "))
    tot_peliculas, duracion_promedio, peliculas =logic.req_5(catalog, fecha_inicial, fecha_final, duracion_min, duracion_max)
    
    print("El total de peliculas es de: "+  str(tot_peliculas))
    print("La duracion promedio de las peliculas es de: "+ str(round(duracion_promedio, 2)))
    
    if tot_peliculas > 20:
        print("\nLas primeras 5 películas entre las fechas son:")
        for i in range(5):
            tabla_pelicula = [[k, v] for k, v in peliculas[i].items()]
            print(tabulate(tabla_pelicula, headers=["Campo", "Valor"], tablefmt="pretty"))
            print("\n")
            
        print("Las últimas 5 películas entre las fechas son:")
        for k in range(len(peliculas) - 5, len(peliculas)):
            tabla_pelicula = [[key, val] for key, val in peliculas[k].items()]
            print(tabulate(tabla_pelicula, headers=["Campo", "Valor"], tablefmt="pretty"))
            print("\n")
    
    else:
        print("\nLa lista de películas encontradas entre las fechas es:")
        for j in range(len(peliculas)):
            tabla_pelicula = [[key, val] for key, val in peliculas[j].items()]
            print(tabulate(tabla_pelicula, headers=["Campo", "Valor"], tablefmt="pretty"))
            print("\n")
            
    return None

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
            print_req_1(control, data)

        elif int(inputs) == 3:
            print_req_2(control, data)

        elif int(inputs) == 4:
            print_req_3(control, data)

        elif int(inputs) == 5:
            print_req_4(control, data)

        elif int(inputs) == 6:
            print_req_5(control, data)

        elif int(inputs) == 7:
            print_req_6(control, data)

        elif int(inputs) == 8:
            print_req_7(control, data)

        elif int(inputs) == 9:
            print_req_8(control, data)

        elif int(inputs) == 0:
            working = False
            print("\nGracias por utilizar el programa") 
        else:
            print("Opción errónea, vuelva a elegir.\n")
    sys.exit(0)

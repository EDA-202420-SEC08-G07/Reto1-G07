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
    nombre_archivo= input("Ingrese el nombre del archivo ('movies-small.csv'): ")
    catalog=logic.load_data(control, data_dir, nombre_archivo)
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
    start_time = time.time()
    ultima_pelicula, count = logic.req_1(catalog, min_runtime)
    end_time = time.time()
    elapsed_time = end_time - start_time
    tabla_pelicula = [[k, v] for k, v in ultima_pelicula.items()]
    print("El numero total de peliculas que cumplen con este criterio es de: "+str(count))
    print("La ultima pelicula que cumple con este criterio es: ")
    print(tabulate(tabla_pelicula, headers=["Campo", "Valor"], tablefmt="pretty"))
    print(f"Tiempo de ejecución: {elapsed_time:.6f} segundos")


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


def print_req_5(control, data):
    """
        Función que imprime la solución del Requerimiento 5 en consola
    """
    catalog=data
    fecha_inicial=input("Ingrese la fecha donde quiere que inicie la busqueda, formato YYYY-MM-DD: ")
    fecha_final=input("Ingrese la fecha donde quiere que acabe la busqueda, formato YYYY-MM-DD: ")
    duracion_min= float(input("Ingrese el tiempo minimo de la pelicula que desea buscar: "))
    duracion_max = float(input("Ingrese el tiempo maximo de la pelicula que desea buscar: "))
    start_time = time.time()
    tot_peliculas, duracion_promedio, peliculas =logic.req_5(catalog, fecha_inicial, fecha_final, duracion_min, duracion_max)
    end_time = time.time()
    elapsed_time = end_time - start_time
    
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
            
    print(f"Tiempo de ejecución: {elapsed_time:.6f} segundos")

def print_req_6(control, data):
    """
        Función que imprime la solución del Requerimiento 6 en consola
    """
    catalog=data
    idioma_org = input("Ingrese el idioma original de las películas (ej.: 'en', 'fr', 'zh'): ")
    anio_inicial = int(input("Ingrese el año inicial del periodo a consultar (formato YYYY): "))
    anio_final = int(input("Ingrese el año final del periodo a consultar (formato YYYY): "))
    start_time = time.time()
    resultados = logic.req_6(catalog, idioma_org, anio_inicial, anio_final)
    end_time = time.time()
    elapsed_time = end_time - start_time
    for anio, datos in resultados.items():
        print(f"Resultados para el año {anio}:")
        print(f"Total de películas: {datos['total_peliculas']}")
        print(f"Votación promedio: {datos['votacion_promedio_total']}")
        print(f"Duración promedio: {datos['duracion_promedio_total']} minutos")
        print(f"Ganancias acumuladas: {datos['ganancias_acumuladas']}")
        if datos['mejor_pelicula'] is not None:
            print(f"Mejor película: {datos['mejor_pelicula']['titulo']} con una votación promedio de: {datos['mejor_pelicula']['votacion']}")
        else:
            print("Mejor película: No disponible")
        if datos['peor_pelicula'] is not None:
            print(f"Peor película: {datos['peor_pelicula']['titulo']} con una votación promedio de: {datos['peor_pelicula']['votacion']}")
        else:
            print("Peor película: No disponible")
        print("\n")
        print(f"Tiempo de ejecución: {elapsed_time:.6f} segundos")



def print_req_7(control, data):
    """
        Función que imprime la solución del Requerimiento 7 en consola
    """
    catalog = data
    companie = input('Ingrese el nombre de la compañia deseada: ')
    fecha_inicial = input('Ingrese el año donde quiere que inicie la busqueda: ')
    fecha_final = input('Ingrese la fecha donde quiere que finalice la busqueda: ')
    resultado = logic.req_7(data, companie, fecha_inicial, fecha_final)
    
    if not resultado:
        print("No se encontraron películas producidas por la compañía en el rango de años especificado.")
        return None
    #crear tabla para el tabulate con los datos por año
    table_data = []
    for year, datos in resultado.items():
        
        
        table_data.append([
            year, 
            datos['total_peliculas'], 
            round(datos['promedio_votacion'], 2),
            round(datos['promedio_duracion'], 2),
            datos['total_ganancias'],
            datos['mejor_pelicula'],
            datos['mejor_votacion'],
            datos['peor_pelicula'],
            datos['peor_votacion']
        ])
    
    print(tabulate(table_data, headers=[
        "Año", "Total Películas", "Promedio Votación", 
        "Promedio Duración", "Ganancias Acumuladas", 
        "Mejor Película", "Mejor Votación", 
        "Peor Película", "Peor Votación"], tablefmt="pretty"))


def print_req_8(catalog, data):
    """
        Función que imprime la solución del Requerimiento 8 en consola
    """
    catalog=data
    anio=int(input("Ingrese el año donde desea buscar la informacion: "))
    genero=input("Ingrese el genero que desea consultar: ")
    print("Espere que cargue la informacion")
    diccionario=logic.req_8(catalog, anio, genero)
    tabla_pelicula = [[k, v] for k, v in diccionario.items()]
    print(tabulate(tabla_pelicula, headers=["Campo", "Valor"], tablefmt="pretty"))


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

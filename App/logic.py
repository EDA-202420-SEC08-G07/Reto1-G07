import time
import csv
import sys
import os
import json
from DataStructures.List import single_linked_list as lt
from DataStructures.List import array_list as ar

csv.field_size_limit(2147483647)
default_limit=1000
sys.setrecursionlimit(default_limit*10)

data_dir = os.path.dirname(os.path.realpath('__file__')) + '/Data/'

def new_logic():
    """
    Crea el catalogo para almacenar las estructuras de datos
    """
    catalog = {"id": None, # Identificador
               "title":None,
               "original_language": None,
               "release_date": None, # Depende si fue lanzada o no
               "revenue":None, # Ingresos netos de la película al momento de publicación
               "runtime": None,
               "status":None,
               "vote_average":None,
               "vote_count":None,
               "budget":None,
               "genres": {"nombre_genero": None, "id_genero": None},  # id y name
               "production_companies": {"nombre_compania": None, "id_compania": None}  # id y name
    }
    
    catalog['id'] = ar.new_list()
    catalog["title"]= ar.new_list()
    catalog['original_language']= ar.new_list()
    catalog['release_date']=  ar.new_list()
    catalog['revenue'] = ar.new_list()
    catalog['runtime'] = ar.new_list()
    catalog['status'] = ar.new_list()
    catalog['vote_average'] = ar.new_list()
    catalog['vote_count'] = ar.new_list()
    catalog['budget'] = ar.new_list()
    
    # Inicializar 'genres' correctamente con sublistas para 'nombre_genero' e 'id_genero'
    catalog['genres'] = {
        "nombre_genero": ar.new_list(),
        "id_genero": ar.new_list()
    }

    # Inicializar 'production_companies' correctamente con sublistas para 'nombre_compania' e 'id_compania'
    catalog['production_companies'] = {
        "nombre_compania": ar.new_list(),
        "id_compania": ar.new_list()
    }
    return catalog


# Funciones para la carga de datos

def load_data(catalog, data_dir):
    """
    Carga los datos del reto
    """
    movie_file = data_dir + 'movies-small.csv'
    movies = csv.DictReader(open(movie_file, encoding='utf-8'))

    for movie in movies:
        id = movie.get("id", "Unknown")
        if len(id) == 0:
            id = "Unknown"
        ar.add_last(catalog["id"], id)

        title = movie.get("title", "Unknown")
        if len(title) == 0:
            title = "Unknown"
        ar.add_last(catalog["title"], title)

        original_language = movie.get("original_language", "Unknown")
        if len(original_language) == 0:
            original_language = "Unknown"
        ar.add_last(catalog["original_language"], original_language)

        release_date = movie.get("release_date", "Unknown")
        if len(release_date) == 0:
            release_date = "Unknown"
        ar.add_last(catalog["release_date"], release_date)

        revenue = movie.get("revenue", "0")
        if revenue == "0":
            revenue = "Undefined"
        ar.add_last(catalog["revenue"], revenue)

        runtime = movie.get("runtime", "Unknown")
        if len(runtime) == 0:
            runtime = "Unknown"
        ar.add_last(catalog["runtime"], runtime)

        status = movie.get("status", "Unknown")
        if len(status) == 0:
            status = "Unknown"
        ar.add_last(catalog["status"], status)

        vote_average = movie.get("vote_average", "Unknown")
        if len(vote_average) == 0:
            vote_average = "Unknown"
        ar.add_last(catalog["vote_average"], vote_average)

        vote_count = movie.get("vote_count", "Unknown")
        if len(vote_count) == 0:
            vote_count = "Unknown"
        ar.add_last(catalog["vote_count"], vote_count)

        budget = movie.get("budget", "0")
        if budget == "0":
            budget = "Undefined"
        ar.add_last(catalog["budget"], budget)

    return catalog

def get_first_last_movies(catalog):
    """Imprime las 5 primeras peliculas y las ultimas 5 peliculas cargadas

    Args:
        catalog (dict): diccionario con array list que contiene toda la informacion
    Returns:
        Una lista con las primeras 5 y una lista con las ultimas 5
    """
    first_elems= []
    first_elems.append(ar.first_element(catalog["id"]))
    last_elems= []
    last_elems.append(ar.last_element(catalog["id"]))
    tamanio= int(ar.size(catalog["id"]))
    
    # Primeras 5
    for i in range(1, 6):
        primeros_id=ar.get_element(catalog["id"], i+1)
        first_elems.append(get_data(catalog, primeros_id))
        
    # Ultimas 5
    for k in range(tamanio-5,tamanio):
        ultimos_id=ar.get_element(catalog["id"], k+1)
        last_elems.append(get_data(catalog, ultimos_id))
          
    return first_elems, last_elems

# Funciones de consulta sobre el catálogo

def get_data(catalog, id):
    """
    Retorna un dato por su ID.
    """
    tamanio= int(ar.size(catalog["id"]))
    posicion_dato=0
    for i in range(tamanio):
        if catalog["id"]["elements"][i] == id:
            posicion_dato=i
    
    pelicula={"publicacion":ar.get_element(catalog["release_date"], posicion_dato),
              "titulo":ar.get_element(catalog["title"], posicion_dato),
              "idioma":ar.get_element(catalog["original_language"], posicion_dato),
              "duracion":ar.get_element(catalog["runtime"], posicion_dato),
              "presupuesto":ar.get_element(catalog["budget"], posicion_dato),
              "ingresos_netos":ar.get_element(catalog["revenue"], posicion_dato),         
    }
    if isinstance(pelicula.get("presupuesto"), str):
        pelicula["ganancias"] = "Unknown"
    else:
        pelicula["ganancias"] = float(ar.get_element(catalog["revenue"], posicion_dato)) - float(ar.get_element(catalog["budget"], posicion_dato))
    return pelicula

def req_1(catalog, min_runtime):
    """
    Retorna el resultado del requerimiento 1
    """
    # TODO: Modificar el requerimiento 1
    ocurrencia = None
    count = 0
    for movie in catalog:
        if movie['duracion'] >= min_runtime:
            if ocurrencia is None:
                ocurrencia = movie
                count = 1
            else:
                count +=1
    return ocurrencia, count
                
    pass



def req_2(catalog):
    """
    Retorna el resultado del requerimiento 2
    """
    # TODO: Modificar el requerimiento 2
    pass


def req_3(catalog):
    """
    Retorna el resultado del requerimiento 3
    """
    # TODO: Modificar el requerimiento 3
    pass


def req_4(catalog):
    """
    Retorna el resultado del requerimiento 4
    """
    # TODO: Modificar el requerimiento 4
    pass


def req_5(catalog):
    """
    Retorna el resultado del requerimiento 5
    """
    # TODO: Modificar el requerimiento 5
    pass

def req_6(catalog):
    """
    Retorna el resultado del requerimiento 6
    """
    # TODO: Modificar el requerimiento 6
    pass


def req_7(catalog):
    """
    Retorna el resultado del requerimiento 7
    """
    # TODO: Modificar el requerimiento 7
    pass


def req_8(catalog):
    """
    Retorna el resultado del requerimiento 8
    """
    # TODO: Modificar el requerimiento 8
    pass


# Funciones para medir tiempos de ejecucion

def get_time():
    """
    devuelve el instante tiempo de procesamiento en milisegundos
    """
    return float(time.perf_counter()*1000)


def delta_time(start, end):
    """
    devuelve la diferencia entre tiempos de procesamiento muestreados
    """
    elapsed = float(end - start)
    return elapsed

import time
import csv
import sys
import os
import json
from DataStructures.List import single_linked_list as lt
from DataStructures.List import array_list as ar
from datetime import datetime

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
    
    pelicula={"Publicacion":ar.get_element(catalog["release_date"], posicion_dato),
              "Titulo":ar.get_element(catalog["title"], posicion_dato),
              "Idioma":ar.get_element(catalog["original_language"], posicion_dato),
              "Duracion":ar.get_element(catalog["runtime"], posicion_dato),
              "Presupuesto":ar.get_element(catalog["budget"], posicion_dato),
              "Recaudo":ar.get_element(catalog["revenue"], posicion_dato),         
    }
    if isinstance(pelicula.get("Presupuesto"), str):
        pelicula["Ganancias"] = "Unknown"
    else:
        pelicula["Ganancias"] = float(ar.get_element(catalog["revenue"], posicion_dato)) - float(ar.get_element(catalog["budget"], posicion_dato))
    return pelicula

def req_1(catalog, min_runtime):
    """
    Retorna el resultado del requerimiento 1
    """
    movies_true =[]
    for i in range (ar.size(catalog['runtime'])):
        duracion = catalog['runtime']['elements'][i]
        if duracion >= min_runtime:                 
            m={"Duracion":catalog["runtime"]["elements"][i],
               "Publicacion":catalog["release_date"]["elements"][i],
               "Titulo":catalog["title"]["elements"][i],
               "Presupuesto":catalog["budget"]["elements"][i],
               "Recaudo":catalog["revenue"]["elements"][i],
               "Puntaje":catalog["revenue"]["elements"][i],
               "Idioma":catalog["original_language"]["elements"][i]      
            }
            if isinstance(m.get("Presupuesto"), str):
                m["Ganancias"] = "Unknown"
            else:
                m["Ganancias"] = float(catalog["revenue"]["elements"][i]) - float(catalog["budget"]["elements"][i])
            
            movies_true.append(m)  

    ultima_pelicula = movies_true[0]
    for pelicula in movies_true:  
        fecha_pelicula_dt = datetime.strptime(pelicula["Publicacion"], "%Y-%m-%d")
        fecha_final_dt = datetime.strptime(ultima_pelicula["Publicacion"], "%Y-%m-%d")
        if fecha_pelicula_dt>fecha_final_dt:
            ultima_pelicula=pelicula
        
    contador = len(movies_true)
    return ultima_pelicula, contador     



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


def req_4(catalog, fecha_inicial, fecha_final, estado):
    """Listar  las películas  con  un  estado de  publicación entre un periodo de tiempo dado

    Args:
        catalog (dict): Diccionario con arraylist que contiene toda la informacion
        fecha_inicial (str): La fecha inicial del periodo a consultar (con formato "%Y-%m-%d")
        fecha_final (str): La fecha final del periodo a consultar (con formato "%Y-%m-%d").
        estado (str): Estado de producción de la película (ej.: “Released”,“Rumored”,etc)
    """
    # Fecha formato YYYY-MM-DD
    fecha_inicial_dt = datetime.strptime(fecha_inicial, "%Y-%m-%d")
    fecha_final_dt = datetime.strptime(fecha_final, "%Y-%m-%d")

    duracion_promedio = 0
    peliculas = {"peli": [], "tamanio": 0}
    tamanio = int(ar.size(catalog["id"]))
    
    for i in range(0, tamanio):
        salida = catalog["release_date"]["elements"][i]
        salida_dt = datetime.strptime(salida, "%Y-%m-%d")
        estado_pelicula = catalog["status"]["elements"][i]
        
        if fecha_inicial_dt < salida_dt < fecha_final_dt and estado_pelicula.lower() == estado.lower():
            peliculas["tamanio"]+=1
            duracion_promedio+=float(catalog["runtime"]["elements"][i])
            """
            Fecha de publicación de la película
            Título original de la película
            Presupuesto destinado a la realización de la película
            Dinero recaudado por la película
            Ganancia de final de la película
            Tiempo de duración en minutos de la película
            Puntaje de calificación de la película
            Idioma original de publicación
            """
            m={"Publicacion":catalog["release_date"]["elements"][i],
              "Titulo":catalog["title"]["elements"][i],
              "Presupuesto":catalog["budget"]["elements"][i],
              "Recaudo":catalog["revenue"]["elements"][i],
              "Duracion":catalog["runtime"]["elements"][i],
              "Puntaje":catalog["revenue"]["elements"][i],
              "Idioma":catalog["original_language"]["elements"][i]      
            }
            if isinstance(m.get("Presupuesto"), str):
                m["Ganancias"] = "Unknown"
            else:
                m["Ganancias"] = float(ar.get_element(catalog["revenue"], i)) - float(ar.get_element(catalog["budget"], i))
            
            peliculas["peli"].append(m)
            
    if peliculas["tamanio"] > 20:
        lista = peliculas["peli"][:5] + peliculas["peli"][-5:]
    else:
        lista = peliculas["peli"]
        
    tot_peliculas=int(peliculas.get("tamanio"))
    if tot_peliculas==0:
        duracion_promedio=0
    else:
        duracion_promedio=duracion_promedio/tot_peliculas
        
    return tot_peliculas, duracion_promedio, lista

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

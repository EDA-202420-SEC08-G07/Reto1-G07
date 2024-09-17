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
               "genres": None,
               "production_companies": None
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
    catalog['genres'] = ar.new_list()
    catalog['production_companies'] = ar.new_list()
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

        genero = movie.get("genres", "Unknown")
        if len(genero) == 0:
            genero = "Unknown"
        gen = {
            "id_pelicula": None,
            "id_genero": None,
            "nombre_genero": None
        }
        genres_list = json.loads(movie.get("genres"))
        for genre in genres_list:
            gen["id_pelicula"] = movie.get("id", "Unknown")
            gen["id_genero"] = genre.get("id", "Unknown")
            gen["nombre_genero"] = genre.get("name", "Unknown")
            
            ar.add_last(catalog["genres"], gen)
        
        # La estructura queda almacenada en la llave genres dentro de un array list y cada elemento tiene la siguiente forma:
        # {"id_pelicula":id_pelicula, "id_genero": id_genero, "nombre_genero": "name_genero"}
        # EJ: {'id_pelicula': 'tt0457513', 'id_genero': 9648, 'nombre_genero': 'Mystery'}
        
        compania = movie.get("production_companies", "Unknown")
        if len(compania) == 0:
            compania = "Unknown"
        comp = {
            "id_pelicula": None,
            "id_compania": None,
            "nombre_compania": None
        }
        companies_list = json.loads(movie.get("production_companies"))
        for company in companies_list:
            comp["id_pelicula"] = movie.get("id", "Unknown") 
            comp["id_compania"] = company.get("id", "Unknown")
            comp["nombre_compania"] = company.get("name", "Unknown")
            
            ar.add_last(catalog["production_companies"], comp)
        
        # La estructura queda almacenada en la llave genres dentro de un array list y cada elemento tiene la siguiente forma:
        # {"id_pelicula":id_pelicula, "id_compania": id_compania, "nombre_compania": "nombre_compania"}
        # EJ: {'id_pelicula': 'tt0457513', 'id_compania': 291, 'nombre_compania': 'Perdido Prod.'}
        
    return catalog

def get_first_last_movies(catalog):
    """Imprime las 5 primeras peliculas y las ultimas 5 peliculas cargadas

    Args:
        catalog (dict): diccionario con array list que contiene toda la informacion
    Returns:
        Una lista con las primeras 5 y una lista con las ultimas 5
    """
    first_elems= []
    last_elems= []
    tamanio= int(ar.size(catalog["id"]))
    
    # Primeras 5
    for i in range(1, 6):
        primeros_id=ar.get_element(catalog["id"], i+1)
        first_elems.append(get_data(catalog, primeros_id))
        
    # Ultimas 5
    for k in range(tamanio-5,tamanio):
        ultimos_id=ar.get_element(catalog["id"], k+1)
        last_elems.append(get_data(catalog, ultimos_id))
          
    return first_elems, last_elems, tamanio

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
    Listar las películas con una duracion minima en minutos, y retornar la cantidad de estas,
    aparte retona la informacion de la ultima ultima en formato fecha que cumple con la condicion  

    Args:
        catalog (dict): Diccionario con arraylist que contiene toda la informacion
        min_runtime (float): Flotante (que puede ser un int) que dicta la duracion minima de la pelicula 
        (es inclusivo, si se le pasa por ejemplo 90, va a tomar en cuenta las peliculas que duren 90 minutos
        minimo, y no las que duren mas que esto (desde 91 en adelante))
    
    return:
        Contador: cantidad de peliculas que cumplen la condicion
        Ultima_pelicula: Diccionario con la informacion de la pelicula qud cumple la condicion (segun la fecha de publicacion)
    """
    movies_true =[]
    for i in range (ar.size(catalog['runtime'])):
        duracion = float(catalog['runtime']['elements'][i])
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



def req_2(catalog, idioma_usuario):
    """
    Listar las películas con un lenguaje original dado, y retornar la cantidad de estas,
    aparte retona la informacion de la ultima ultima en formato fecha que cumple con la condicion  

    Args:
        catalog (dict): Diccionario con arraylist que contiene toda la informacion
        idioma_usuario (str): String de dos letras con las iniciales del lenguaje (en, fr, es)
    
    return:
        Contador: cantidad de peliculas que cumplen la condicion
        Ultima_pelicula: Diccionario con la informacion de la pelicula qud cumple la condicion (segun la fecha de publicacion)
    """
    
    movies_true = []
    for i in range (ar.size(catalog['original_language'])):
        idioma = catalog['original_language']['elements'][i]
        if idioma == idioma_usuario:  
            m= {
                "Duracion":catalog["runtime"]["elements"][i],
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

def req_3(catalog, language, fecha_inicial, fecha_final):
    """Consultar las películas en un idioma original entre un rango de fechas de publicación dado

    Args:
        catalog (dict): diccionario con array list que contiene toda la informacion
        language (str): Idioma del cual se desea consultar
        fecha_inicial (str): La fecha inicial del periodo a consultar (con formato "%Y-%m-%d")
        fecha_final (str): La fecha final del periodo a consultar (con formato "%Y-%m-%d").

    Returns:
        lista con las peliculas que cumplen con las condiciones
    """
    fecha_inicial_dt = datetime.strptime(fecha_inicial, "%Y-%m-%d")
    fecha_final_dt = datetime.strptime(fecha_final, "%Y-%m-%d")
    
    tamanio = int(ar.size(catalog['release_date']))
    peliculas = {"peli": [], "tamanio": 0}
    duracion_promedio = 0
    
    for i in range(tamanio):
        fecha_movie = catalog['release_date']['elements'][i]
        fecha_movie_dt = datetime.strptime(fecha_movie, "%Y-%m-%d")
        idioma_movie= catalog["original_language"]["elements"][i]

        if fecha_inicial_dt < fecha_movie_dt < fecha_final_dt and idioma_movie.lower() == language.lower():
            peliculas["tamanio"] += 1
            duracion_promedio += float(catalog["runtime"]["elements"][i])
            
            # Crear diccionario de película
            m = {
                "Publicacion": catalog["release_date"]["elements"][i],
                "Titulo": catalog["title"]["elements"][i],
                "Presupuesto": catalog["budget"]["elements"][i],
                "Recaudo": catalog["revenue"]["elements"][i],
                "Duracion": catalog["runtime"]["elements"][i],
                "Puntaje": catalog["vote_average"]["elements"][i],
                "Estado": catalog["status"]["elements"][i]
            }
            if isinstance(m.get("Presupuesto"), str):
                m["Ganancias"] = "Unknown"
            else:
                m["Ganancias"] = float(ar.get_element(catalog["revenue"], i+1)) - float(ar.get_element(catalog["budget"], i+1))
            
            peliculas["peli"].append(m)
    
    # Llamamos al ordenado por Insertion Sort
    peliculas["peli"] = ordenar_peliculas_por_fecha_insertion(peliculas["peli"])

    lista_primeras = []
    lista_ultimas = []

    if peliculas["tamanio"] > 20:
        # Primeras 5 películas
        lista_primeras = peliculas["peli"][:5]
        
        # Últimas 5 películas
        lista_ultimas = peliculas["peli"][-5:]
    else:
        lista_primeras = peliculas["peli"]

    tot_peliculas = int(peliculas.get("tamanio"))
    if tot_peliculas == 0:
        duracion_promedio = 0
    else:
        duracion_promedio = duracion_promedio / tot_peliculas

    return tot_peliculas, duracion_promedio, lista_primeras, lista_ultimas
    


def ordenar_peliculas_por_fecha_insertion(peliculas):
    """Ordena la lista de películas en base a la fecha de publicación (Insertion Sort)"""
    n = len(peliculas)
    for i in range(1, n):
        # Película actual a insertar en la posición correcta
        pelicula_actual = peliculas[i]
        fecha_actual = datetime.strptime(pelicula_actual["Publicacion"], "%Y-%m-%d")
        
        # Desplazar las películas que están desordenadas
        j = i - 1
        while j >= 0 and datetime.strptime(peliculas[j]["Publicacion"], "%Y-%m-%d") > fecha_actual:
            peliculas[j + 1] = peliculas[j]
            j -= 1
        
        # Insertar la película actual en su posición correcta
        peliculas[j + 1] = pelicula_actual
    
    return peliculas


def req_4(catalog, fecha_inicial, fecha_final, estado):
    """Listar las películas con un estado de publicación entre un periodo de tiempo dado

    Args:
        catalog (dict): Diccionario con arraylist que contiene toda la información
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
    
    for i in range(tamanio):
        salida = catalog["release_date"]["elements"][i]
        salida_dt = datetime.strptime(salida, "%Y-%m-%d")
        estado_pelicula = catalog["status"]["elements"][i]
        
        if fecha_inicial_dt < salida_dt < fecha_final_dt and estado_pelicula.lower() == estado.lower():
            peliculas["tamanio"] += 1
            duracion_promedio += float(catalog["runtime"]["elements"][i])
            
            # Crear diccionario de película
            m = {
                "Publicacion": catalog["release_date"]["elements"][i],
                "Titulo": catalog["title"]["elements"][i],
                "Presupuesto": catalog["budget"]["elements"][i],
                "Recaudo": catalog["revenue"]["elements"][i],
                "Duracion": catalog["runtime"]["elements"][i],
                "Puntaje": catalog["vote_average"]["elements"][i],
                "Idioma": catalog["original_language"]["elements"][i]
            }
            if isinstance(m.get("Presupuesto"), str):
                m["Ganancias"] = "Unknown"
            else:
                m["Ganancias"] = float(ar.get_element(catalog["revenue"], i+1)) - float(ar.get_element(catalog["budget"], i+1))
            
            peliculas["peli"].append(m)
    
    # Llamamos al ordenado por Insertion Sort
    peliculas["peli"] = ordenar_peliculas_por_fecha_insertion(peliculas["peli"])

    lista_primeras = []
    lista_ultimas = []

    if peliculas["tamanio"] > 20:
        # Primeras 5 películas
        lista_primeras = peliculas["peli"][:5]
        
        # Últimas 5 películas
        lista_ultimas = peliculas["peli"][-5:]
    else:
        lista_primeras = peliculas["peli"]

    tot_peliculas = int(peliculas.get("tamanio"))
    if tot_peliculas == 0:
        duracion_promedio = 0
    else:
        duracion_promedio = duracion_promedio / tot_peliculas

    return tot_peliculas, duracion_promedio, lista_primeras, lista_ultimas

def req_5(catalog, fecha_inicial, fecha_final, duracion_min, duracion_max):
    """
    consultar las películas que tengan una duración en minutos entre un rango de 
    tiempo en minutos dado un rango de fechas
    args:
    
        catalog (dict): Diccionario con arraylist que contiene toda la informacion
        fecha_inicial (str): La fecha inicial del periodo a consultar (con formato "%Y-%m-%d")
        fecha_final (str): La fecha final del periodo a consultar (con formato "%Y-%m-%d").
        duracion_min (int): Tiempo minimo que dura la pelicula
        duracion_max (int): Tiempo maximo que dura la pelicula
    return:
        total de peliculas que cumplen la condicion
        La duracion promedio de las peliculas que cumplen el criterio
        Lista de diccionarios de las peliculas que cumplen el requisito, si hay mas de 20, retornar 
        solo las primeras 5 y las ultimas 5
    """
    # Fecha formato YYYY-MM-DD
    duracion_promedio = 0
    fecha_inicial_dt = datetime.strptime(fecha_inicial, "%Y-%m-%d")
    fecha_final_dt = datetime.strptime(fecha_final, "%Y-%m-%d")
    peliculas = {"movies": [], "tamanio": 0}
    tamanio = int(ar.size(catalog["id"]))
    
    for i in range(0, tamanio):
        salida = catalog["release_date"]["elements"][i]
        salida_dt = datetime.strptime(salida, "%Y-%m-%d")
        duracion = float(catalog["runtime"]["elements"][i])
        
        
        if fecha_inicial_dt < salida_dt < fecha_final_dt and duracion_min < duracion < duracion_max:
            peliculas["tamanio"]+=1
            duracion_promedio+= duracion
            movie={"Publicacion":catalog["release_date"]["elements"][i],
              "Titulo":catalog["title"]["elements"][i],
              "Presupuesto":catalog["budget"]["elements"][i],
              "Recaudo":catalog["revenue"]["elements"][i],
              "Duracion":catalog["runtime"]["elements"][i],
              "Puntaje":catalog["revenue"]["elements"][i],
              "Idioma":catalog["original_language"]["elements"][i]      
            }
            if isinstance(movie.get("Presupuesto"), str):
                movie["Ganancias"] = "Unknown"
            else:
                movie["Ganancias"] = float(ar.get_element(catalog["revenue"], i+1)) - float(ar.get_element(catalog["budget"], i+1))
            
            peliculas["movies"].append(movie)
            
    if peliculas["tamanio"] > 20:
        lista_peliculas = peliculas["movies"][:5] + peliculas["movies"][-5:]
    else:
        lista_peliculas = peliculas["movies"]
        
    total_peliculas = int(peliculas.get("tamanio"))
    if total_peliculas==0:
        duracion_promedio=0
    else:
        duracion_promedio = duracion_promedio/total_peliculas
        
    return total_peliculas, duracion_promedio, lista_peliculas

def req_6(catalog, idioma_org, anio_inicial, anio_final):
    """
    Retorna las estadísticas de las películas publicadas en un idioma dado durante un rango de años.

    Este requerimiento analiza las películas en el catálogo que fueron publicadas 
    (status = "released") en un idioma específico y dentro de un periodo de años determinado. 
    Para cada año en el rango especificado, la función recopila la siguiente información:
    
    - El total de películas publicadas en el idioma de consulta en ese año.
    - El promedio de votación promedio de las películas publicadas en ese año.
    - El tiempo promedio de duración de las películas publicadas en ese año.
    - Las ganancias acumuladas por todas las películas publicadas en ese año (calculadas como la diferencia entre recaudación y presupuesto).
    - El título y la votación de la mejor película publicada en ese año.
    - El título y la votación de la peor película publicada en ese año.
    
    Args:
        catalog (dict): El catálogo de películas que contiene todos los datos relevantes (fechas, votos, duración, etc.).
        idioma_org (str): El código del idioma original de las películas (por ejemplo: 'en' para inglés, 'fr' para francés).
        anio_inicial (int): El año inicial del periodo a analizar (por ejemplo, 2000).
        anio_final (int): El año final del periodo a analizar (por ejemplo, 2020).
    
    Returns:
        dict_anios (dict): diccionario de diccionario con las llaves como los anios que entran dentro del rango
        de consolta y con los values con la respectiva informacion estadistica de cada uno de estos anios

    """
    dict_anios = {}
    
    for year in range(anio_inicial, anio_final + 1):
        tamanio = int(ar.size(catalog["id"]))
        total_peliculas = 0
        votacion_total = 0
        duracion_total = 0
        ganancias_acumuladas = 0
        mejor_pelicula = None
        peor_pelicula = None
        
        for i in range(tamanio):
            fecha = catalog["release_date"]["elements"][i]
            anio = int(fecha[:4])
            status = catalog["status"]["elements"][i].lower()  
            idioma = catalog["original_language"]["elements"][i].lower()  
            
            if status == "released" and idioma == idioma_org and year == anio:
                total_peliculas += 1
                votacion = float(catalog["vote_average"]["elements"][i])
                duracion = float(catalog["runtime"]["elements"][i])
                presupuesto = catalog["budget"]["elements"][i]
                recaudacion = catalog["revenue"]["elements"][i]
                
                if isinstance(presupuesto, (int, float)) and isinstance(recaudacion, (int, float)):
                    ganancias_acumuladas += (recaudacion - presupuesto)
                else:
                    ganancias_acumuladas += 0
                votacion_total += votacion
                duracion_total += duracion
                
                if mejor_pelicula is None or votacion > mejor_pelicula["votacion"]:
                    mejor_pelicula = {
                        "titulo": catalog["title"]["elements"][i],
                        "votacion": votacion
                    }
                
                if peor_pelicula is None or votacion < peor_pelicula["votacion"]:
                    peor_pelicula = {
                        "titulo": catalog["title"]["elements"][i],
                        "votacion": votacion
                    }
        
        if total_peliculas > 0:
            votacion_promedio_total = votacion_total / total_peliculas
            duracion_promedio_total = duracion_total / total_peliculas
        else:
            votacion_promedio_total = 0
            duracion_promedio_total = 0
        
        dict_anios[year] = {
            "total_peliculas": total_peliculas,
            "votacion_promedio_total": round(votacion_promedio_total, 2),
            "duracion_promedio_total": round(duracion_promedio_total, 2),
            "ganancias_acumuladas": round(ganancias_acumuladas, 2),
            "mejor_pelicula": mejor_pelicula,
            "peor_pelicula": peor_pelicula
        }
    return dict_anios

    


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

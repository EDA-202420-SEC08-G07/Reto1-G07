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
               "genres":None, #id y name
               "production_companies":None} #id, name
    
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
    ar.add_last(catalog["genres"],{"nombre_genero":None, "id_genero":None} )
    catalog["genres"]["nombre_genero"]=ar.new_list
    catalog["genres"]["id_genero"]=ar.new_list
    
    catalog['production_companies'] = ar.new_list()
    ar.add_last(catalog["production_companies"], {"nombre_compania":None, "id_compania":None})
    catalog["production_companies"]["nombre_compania"]=ar.new_list
    catalog["production_companies"]["id_compania"]=ar.new_list
    return catalog


# Funciones para la carga de datos

def load_data(catalog, data_dir):
    """
    Carga los datos del reto
    """
    movies=csv.DictReader(open(data_dir, encoding='utf-8'))
    for movie in movies:
        
        id_list=json.load(movies["id"])
        for id in id_list:
            if len(id)==0:
                id="Unknown"
            ar.add_last(catalog["id"],id)
            
        title_list=json.loads(movie["title"])
        for title in title_list:
            if len(title)==0:
                title="Unknown"
            ar.add_last(catalog["title"],title)
            
        original_language_list=json.loads(movie["original_language"])
        for original_language in original_language_list:
            if len(original_language)==0:
                original_language="Unknown"
            ar.add_last(catalog["original_language"],original_language)
            
        release_date_list=json.loads(movies["release_date"])
        for release_date in release_date_list:
            if len(release_date)==0:
                release_date="Unknown"
            ar.add_last(catalog["release_date"],release_date)
            
        revenue_list=json.loads(movies["revenue"])
        for revenue in revenue_list:
            if revenue == 0:
                revenue="Undefined"
            ar.add_last(catalog["revenue"],revenue)
            
        runtime_list=json.loads(movies["runtime"])
        for runtime in runtime_list:
            if len(runtime)==0:
                runtime="Unknown"
            ar.add_last(catalog["runtime"], runtime)
            
        status_list=json.loads(movies["status"])
        for status in status_list:
            if len(status)==0:
                status="Unknown"
            ar.add_last(catalog["status"], status)
            
        vote_average_list=json.loads(movies["vote_average"])
        for vote_average in vote_average_list:
            if len(vote_average)==0:
                vote_average="Unknown"
            ar.add_last(catalog["vote_average"], vote_average)
            
        vote_count_list=json.loads(movies["vote_count"])
        for vote_count in vote_count_list:
            if len(vote_count)==0:
                vote_count="Unknown"
            ar.add_last(catalog["vote_count"], vote_count)
            
        budget_list=json.loads(movies["budget"])
        for budget in budget_list:
            if budget==0:
                budget="Undefined"
            ar.add_last(catalog["budget"], budget)
            
        genres_list=json.loads(movies["genres"])
        for genre in genres_list:
            if len(genre["nombre_genero"])==0:
                nombre_genero="Sin_genero"
            elif len(genre["nombre_genero"])!=0:
                nombre_genero=catalog["genres"]["nombre_genero"]
            if len(genre["id_genero"])==0:
                id_genero="Sin_genero"
            elif len(genre["id_genero"])!=0:
                nombre_genero=catalog["genres"]["id_genero"]    
                
            ar.add_last(catalog["genres"]["nombre_genero"], nombre_genero)
            ar.add_last(catalog["genres"]["id_genero"], id_genero)
            
        
        production_companies_list=json.loads(movies["production_companies"])
        for production_companies in production_companies_list:
            if len(production_companies["nombre_compania"])==0:
                nombre_companias="Indefinida"
            elif len(production_companies["nombre_compania"])!=0:
                nombre_companias=catalog["production_companies"]["nombre_compania"]
            if len(production_companies["id_compania"])==0:
                id_companias="Indefinida"
            elif len(production_companies["id_compania"])!=0:
                id_companias=catalog["production_companies"]["id_compania"]    
                
            ar.add_last(catalog["production_companies"]["nombre_genero"], nombre_companias)
            ar.add_last(catalog["production_companies"]["id_genero"], id_companias)
        
    return catalog


# Funciones de consulta sobre el catálogo

def get_data(catalog, id):
    """
    Retorna un dato por su ID.
    """
    #TODO: Consulta en las Llamar la función del modelo para obtener un dato
    pass


def req_1(catalog):
    """
    Retorna el resultado del requerimiento 1
    """
    # TODO: Modificar el requerimiento 1
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

from . import list_node as node

def new_list():
    newlist={'first': None,'last': None,'size': 0,}
    return newlist

def add_first(lst, element): 
	new_node = node.new_single_node(element)
	new_node["next"] = lst["first"]
	lst["first"] = new_node
	if (lst["size"] == 0):
		lst["last"]= lst["first"]
	lst["size"]+=1
	return lst

def add_last(lst, element):
	new_node = node.new_single_node(element)
	if lst["size"]==0:
		lst["first"]=new_node
	else:
		lst["last"]["next"]= new_node
	lst["last"]= new_node
	lst["size"]+=1
	return lst

def is_empty(my_list):
    return my_list['size'] == 0

def size(list):
    return list['size']

def first_element(lst):
	if lst["first"] is not None:
		return lst["first"]["info"]
	else:
		return None
		
def last_element(lst):
	if lst["last"] is not None:
		return lst["last"]["info"]
	else:
		return None

def get_element(lst, pos):
    searchpos = 1 
    current_node = lst['first']
    
    while searchpos <= pos:
        searchpos += 1
        current_node = current_node['next']
    return current_node['info']

def remove_first(lst):
	if lst["first"] is not None:
		temp= lst["first"]["next"]
		node= lst["first"]
		lst["first"]= temp
		lst["size"] = lst["size"]-1
		if lst["size"] == 0:
			lst["last"] = lst["first"]
		return node["info"]
	return None

def delete_element(lst, pos):
    if pos < 0 or pos > lst["size"]:
        return lst  

    current_node = lst["first"]
    prev_node = lst["first"]
    searchpos = 0
    
    if pos == 0:
        lst["first"]=lst["first"]["next"]
    else:
        while searchpos < pos:
            prev_node = current_node
            current_node = current_node["next"]
            searchpos += 1
        
        prev_node["next"] = current_node["next"]
    
    lst["last"]=prev_node
    lst["size"] = lst["size"] - 1
    print(lst)
    return lst

def remove_last (list):
    if list["last"] is None:
        return None
    
    else:
        penultimo = list["first"]
        
        while penultimo["next"] != list["last"]:
            penultimo = penultimo["next"]
        
        nodo = list["last"]
        penultimo["next"] = None
        list["last"] = penultimo
        list["size"] -= 1
        return nodo['info']
    
def insert_element(list, element, pos):
    new_node = node.new_single_node(element)
    if list["first"] is None:
            list["first"] = new_node
            list["last"] = new_node
            list["size"] += 1
            return list
    if pos == 0:
        new_node["next"] = list["first"]
        list["first"] = new_node
        if list["size"] == 0:
            list["last"] = new_node
        list["size"] += 1
        return list
    anterior = list["first"]
    i = 0
    while i < pos - 1 and anterior["next"] is not None:
        anterior = anterior["next"]
        i += 1
    
    if i == pos - 1:  
        new_node["next"] = anterior["next"]
        anterior["next"] = new_node
        
        if new_node["next"] is None:
            list["last"] = new_node
        
        list["size"] += 1
    else:
        return list

    return list


def is_present(my_list, element, cmp_function):
    nodo = my_list['first']
    posicion = 0
    while nodo is not None:
        if nodo['info'] == element:
            return posicion
        nodo = nodo['next']
        posicion += 1
    return -1

def change_info(list, pos, info):
    recorrido = list['first']
    i = 0
    if pos == 0:
        if list['first'] is not None:
            list['first']['info'] == info
        return list
    while i < pos and recorrido["next"] is not None:
        recorrido = recorrido["next"]
        i += 1
    if recorrido is not None and i == pos:
        recorrido['info'] = info
    return list
        
def exchange(list, pos1, pos2):
    nodo1 = list['first']
    nodo2 = list['first']
    info1 = None
    info2 = None
    i = 0
    j = 0
    while nodo1 is not None and i < pos1:
        nodo1 = nodo1['next']
        i += 1
    if nodo1 is not None and i == pos1:
        info1 = nodo1['info']
    
    while nodo2 is not None and j < pos2:
        nodo2 = nodo2['next']
        j += 1
    if nodo2 is not None and j == pos2:
        info2 = nodo2['info']
        
    if nodo1 is not None and nodo2 is not None:
        nodo1['info'] = info2
        nodo2['info'] = info1
    return list
        
def sub_list(my_list, pos, num_elem):
    nodo_principal = my_list["first"]
    nueva_lista = []
    k = 0
    j = 0
    
    if pos < 0 or num_elem < 0:
        return nueva_lista

        
# Búsqueda Lineal en Lista de Fechas

def buqueda_lineal(lista_fechas , buscar_fecha):
    
    for i in range  (len(lista_fechas)):
        if lista_fechas[i] == buscar_fecha :
            return i 
    
    return -1

lista_fechas =["1998-10-25","2001-06-16","2016-09-27","2018-07-16"]
buscar_fecha ="2001-06-16"
posicion =buqueda_lineal(lista_fechas,buscar_fecha)

if posicion != -1 :
    print(f"la fecha {buscar_fecha} se encuentra en la posicion {posicion}")
    
else:
    print(f"la fecha {buscar_fecha}no se encuentra en la lista ")         








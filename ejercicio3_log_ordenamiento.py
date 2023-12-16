# Ordenamiento por Selección

def orden_desc(lista):
    
    for i in range(len(lista) -1):
        mayor = i
        
        for j in range(i+1 ,len(lista)):
            if lista[j] > lista[mayor]:
                mayor = j
        
        
        lista[i],lista[mayor] = lista[mayor],lista[i]
        
    return lista    
lista = [20,30,5,3,28,50,1]
        
print(orden_desc(lista))
                
                  
    
class Stack:
    def __init__(self):
        self.items = []      #Aqui inicia la estructura

    def push(self, item):
        self.items.append(item)   
    
    def pop(self):
        if not self.is_empty():      #Verificamos que tenga contenido la fila
            return self.items.pop()
        else:
            return None
        
    
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            return None
        
    
    def is_empty(self):
        return len(self.items) == 0     #Comprueba si tenemos contenido en la pila
    
    def size(self):
        return len(self.items)


def invertir_lista(lista):
    pila = Stack()
    for elemento in lista:
        pila.push(elemento)
 
    lista_invertida = []               #Aca se guardaran los datos de forma invertida
    while not pila.is_empty():
        lista_invertida.append(pila.pop())

    return lista_invertida           #Nos devuelve la lista ya invertida


#En esta parte del codigo ya se emperzaran a imprimir las listas
lista_original = [1, 2, 3, 4, 5]              
print("Lista original:", lista_original)
lista_invertida = invertir_lista(lista_original)
print("Lita invertida:", lista_invertida)






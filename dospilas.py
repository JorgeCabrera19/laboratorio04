class ColaPila:
    def __init__(self):
        #Se inicia una pila de entrada y otra para salida
        self.entrada = []
        self.salida = []

    def enqueue(self, elemento):
        self.entrada.append(elemento)   #Se agregan elementos a la cola

    def dequeue(self):
        if not self.salida:               #Eliminamos y devolvemos el dato mas antiguo a la cola
            while self.entrada:           #Si la pila salida esta vacia pasa los datos de entrada a salida pero en orden inverso
                self.salida.append(self.entrada.pop())

        # Si la pila de salida tiene datos, eliminar y devolver el elemento superior de la pila
        if self.salida:
            return self.salida.pop()
        else:
            return None

cola = ColaPila()#Creamos una instancia

num_elementos = int(input("Ingrese el número de elementos en la cola: "))
for i in range(num_elementos):
    elemento = input(f"Ingrese el elemento {i + 1}: ")
    cola.enqueue(elemento)  #Se agrega el elemento a la cola

#Metodo Dequeue
print("Inicio del proceso de atención: ")
while True:
    elemento_atendido = cola.dequeue()
    if elemento_atendido is not None:
        print("Atendiendo al cliente", elemento_atendido)
    else:
        print("Todos los clientes han sido atendidos.")
        break
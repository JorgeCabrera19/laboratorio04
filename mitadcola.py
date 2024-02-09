class Queue:
    def __init__(self):
        self.items = []             #Aca empieza la lista que nos servira mas adelante como cola

    def enqueue(self, item):
        self.items.append(item)     #Con este metodo agregamos datos al final de la cola

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0) #Quita y devuelve el primer dato en la cola 
        else:
            return None

    def is_empty(self):
        return len(self.items) == 0 #Aca se ve si esta vacia la cola

    def size(self):
        return len(self.items)

# A partir de aca se empieza la funcion de revertir los datos
def reverse_half_queue(queue):
    stack = []
    size = queue.size()
    half_size = size // 2

    for _ in range(half_size):
        stack.append(queue.dequeue())

    while stack:
        queue.enqueue(stack.pop())

    for _ in range(size - half_size):
        queue.enqueue(queue.dequeue())

#El usuario podra ingerar sus datos
def get_queue_from_user():
    queue = Queue()
    n = int(input("Ingrese la cantidad de elementos en la cola: "))
    for i in range(n):
        item = input(f"Ingrese el elemento {i + 1}: ")
        queue.enqueue(item)
    return queue


if __name__ == "__main__":
    queue = get_queue_from_user()
    print("Cola original:", queue.items)  #Imprime la original

    reverse_half_queue(queue)
    print("Cola con la mitad de elementos revertidos:", queue.items) #imprime la cola revertida

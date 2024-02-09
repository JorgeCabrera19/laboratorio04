def parentesis_balanceados(cadena):
    pila = []                        #en esta pila se almacenaran los parentesis


    # Se empiezan a realizar iteraciones para agregar parentesis
    for caracter in cadena:
        if caracter == '(':     
            pila.append(caracter)
        elif caracter == ')':
            if len(pila) == 0:
                return False
            else:
                pila.pop()


    return len(pila) == 0

#Aca de define cada cadena de prueba
cadena1 = input("Cadena1: ")
cadena2 = input("Cadena2: ")
cadena3 = input("Cadena3: ")
cadena4 = input("Cadena4: ")
cadena5 = input("Cadena5: ")

#Por medio de los print comprobamos si las cadenas estan balanceadas o no para mostrarlas
print("Cadena 1 balanceada:", parentesis_balanceados(cadena1))
print("Cadena 2 balanceada:", parentesis_balanceados(cadena2))
print("Cadena 3 balanceada:", parentesis_balanceados(cadena3))
print("Cadena 4 balanceada:", parentesis_balanceados(cadena4))
print("Cadena 5 balanceada:", parentesis_balanceados(cadena5))

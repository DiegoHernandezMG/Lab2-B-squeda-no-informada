from estructuras import Pila, ListaGenerica

# Función para generar los estados vecinos del estado actual
def generar_vecinos(estado):
    vecinos = []
    for i in range(len(estado) - 1):
        # Intercambiar elementos adyacentes
        vecino = estado[:]
        vecino[i], vecino[i + 1] = vecino[i + 1], vecino[i]
        vecinos.append(vecino)
    return vecinos

# Función para realizar DFS
def dfs_4_puzzle(estado_inicial, estado_objetivo):
    # Inicializamos la pila (frontera) y la lista (nodos visitados)
    frontera = Pila()
    visitados = ListaGenerica()
    
    # Agregar el estado inicial a la frontera
    frontera.push(estado_inicial)
    
    while not frontera.is_empty():
        # Sacamos el último nodo de la pila (Frontera)
        estado_actual = frontera.pop()
        
        # Verificar si el estado actual es el estado objetivo
        if estado_actual == estado_objetivo:
            print("¡Solución encontrada!")
            print("Estado final:", estado_actual)
            return
        
        # Si no hemos visitado este estado, lo agregamos a la lista de visitados
        if not visitados.buscar(estado_actual):
            visitados.insertar(estado_actual)
            
            # Generamos los vecinos del estado actual
            vecinos = generar_vecinos(estado_actual)
            
            # Agregamos cada vecino a la frontera
            for vecino in vecinos:
                if not visitados.buscar(vecino):  # Evitamos agregar nodos visitados
                    frontera.push(vecino)
    
    print("No se encontró una solución.")

# Uso
if __name__ == "__main__":
    estado_inicial = [2, 4, 1, 3]  # Ejemplo de estado inicial
    print(f"El estado inicial es: ", estado_inicial	)
    estado_objetivo = [1, 2, 3, 4]  # El estado objetivo es siempre [1, 2, 3, 4]
    
    dfs_4_puzzle(estado_inicial, estado_objetivo)

def is_valid_move(maze, position, visited):
    row, col = position
    # Verificar si la posición está dentro de los límites del laberinto
    if 0 <= row < len(maze) and 0 <= col < len(maze[0]):
        # Verificar si es un camino (0) y no ha sido visitado antes
        return maze[row][col] == 0 and position not in visited
    return False

def dfs_maze(maze, current, end, path, visited):
    # Si hemos alcanzado la posición final, retornar el camino
    if current == end:
        path.append(current)
        return True

    # Obtener la posición actual
    row, col = current
    
    # Marcar la posición actual como visitada
    visited.add(current)
    path.append(current)

    # Direcciones posibles de movimiento: abajo, arriba, derecha, izquierda
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    
    # Explorar cada dirección
    for dr, dc in directions:
        next_position = (row + dr, col + dc)
        if is_valid_move(maze, next_position, visited):
            if dfs_maze(maze, next_position, end, path, visited):
                return True

    # Si ninguna dirección es válida, hacer backtrack
    path.pop()
    return False

def solve_maze(maze, start, end):
    visited = set()  # Mantener un conjunto de posiciones visitadas
    path = []        # Lista para almacenar el camino
    if dfs_maze(maze, start, end, path, visited):
        return path
    else:
        return "No hay camino posible"

# Definición del laberinto
maze = [
    [1, 0, 1, 1, 1],
    [1, 0, 0, 0, 1],
    [1, 1, 1, 0, 1],
    [1, 0, 0, 0, 0],
    [1, 1, 1, 1, 1]
]

# Posición inicial y final
start = (0, 1)
end = (3, 4)

# Resolver el laberinto
path = solve_maze(maze, start, end)

print("Camino encontrado:" if isinstance(path, list) else path)
print(path)
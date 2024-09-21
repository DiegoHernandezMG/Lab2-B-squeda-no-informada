# estructuras.py

class Pila:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None

    def is_empty(self):
        return len(self.items) == 0

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        return None

    def size(self):
        return len(self.items)


class Cola:
    def __init__(self):
        self.items = []

    def insertar(self, item):
        self.items.insert(0, item)

    def quitar(self):
        if not self.is_empty():
            return self.items.pop()
        return None

    def is_empty(self):
        return len(self.items) == 0

    def recorrer(self):
        for item in self.items:
            print(item)

    def buscar(self, item):
        return item in self.items


class ListaGenerica:
    def __init__(self):
        self.items = []

    def insertar(self, item):
        self.items.append(item)

    def buscar(self, item):
        return item in self.items

    def mostrar(self):
        for item in self.items:
            print(item)

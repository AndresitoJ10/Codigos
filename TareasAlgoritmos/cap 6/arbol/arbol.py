class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None

class ArbolBinario:
    def __init__(self):
        self.raiz = None
    
    def insertar(self, valor):
        if self.raiz is None:
            self.raiz = Nodo(valor)
        else:
            self._insertar(valor, self.raiz)
    
    def _insertar(self, valor, nodo_actual):
        if valor < nodo_actual.valor:
            if nodo_actual.izquierda is None:
                nodo_actual.izquierda = Nodo(valor)
            else:
                self._insertar(valor, nodo_actual.izquierda)
        elif valor > nodo_actual.valor:
            if nodo_actual.derecha is None:
                nodo_actual.derecha = Nodo(valor)
            else:
                self._insertar(valor, nodo_actual.derecha)
        else:
            print("El valor ya existe en el árbol.")
    
    def inorden(self, nodo_actual):
        if nodo_actual is not None:
            self.inorden(nodo_actual.izquierda)
            print(nodo_actual.valor, end=" ")
            self.inorden(nodo_actual.derecha)
    
    def preorden(self, nodo_actual):
        if nodo_actual is not None:
            print(nodo_actual.valor, end=" ")
            self.preorden(nodo_actual.izquierda)
            self.preorden(nodo_actual.derecha)
    
    def postorden(self, nodo_actual):
        if nodo_actual is not None:
            self.postorden(nodo_actual.izquierda)
            self.postorden(nodo_actual.derecha)
            print(nodo_actual.valor, end=" ")

# Ejemplo de uso
arbol = ArbolBinario()
arbol.insertar(5)
arbol.insertar(3)
arbol.insertar(7)
arbol.insertar(1)
arbol.insertar(4)
arbol.insertar(6)
arbol.insertar(8)

print("Recorrido inorden:")
arbol.inorden(arbol.raiz)
print()

print("Recorrido preorden:")
arbol.preorden(arbol.raiz)
print()

print("Recorrido postorden:")
arbol.postorden(arbol.raiz)
print()

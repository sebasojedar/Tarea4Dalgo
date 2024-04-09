import sys
from collections import deque

def convertir_a_lista_de_adyacencia(lista_de_tuplas):
    grafo = {}
    for arista in lista_de_tuplas:
        # Desempaquetamos la tupla en dos vértices
        v1, v2 = arista

        # Para cada vértice, agregamos el otro vértice a su lista de adyacencia
        if v1 in grafo:
            grafo[v1].add(v2)
        else:
            grafo[v1] = {v2}

        if v2 in grafo:
            grafo[v2].add(v1)
        else:
            grafo[v2] = {v1}

    # Convertimos los sets a listas para obtener la lista de adyacencia final
    grafo_lista_de_adyacencia = {v: list(adyacentes) for v, adyacentes in grafo.items()}
    return grafo_lista_de_adyacencia



def texto_a_lista(lista):
    i = 0
    grafo = []
    texto = ["[","]",",","(",")"]
    while i <= (len(lista)-1):
        if lista[i] not in texto:
            tupla = (lista[i],lista[i+2])
            grafo.append(tupla)
            i+=4
        else:
            i+=1
    return grafo



def fakenews(origen,grafo):
    cola = deque([origen])
    visitados = set([origen])
    horas = -1  # Inicializamos en -1 porque el primer nivel se cuenta antes de procesar

    # Mientras haya nodos por visitar en la cola
    while cola:
        nivel_tamano = len(cola)
        for _ in range(nivel_tamano):
            nodo_actual = cola.popleft()
            # Agregar vecinos no visitados del nodo actual a la cola
            for vecino in grafo[nodo_actual]:
                if vecino not in visitados:
                    visitados.add(vecino)
                    cola.append(vecino)
        horas += 1  # Incrementar las horas después de procesar un nivel completo

    return horas     


def main():
    origen = 0
    grafo = []
    numero_casos = int(sys.stdin.readline())
    for __ in range(numero_casos):
        case_list = list(map(str, sys.stdin.readline().split()))
        for i in range(len(case_list)):
            if i == 0:
                origen = case_list[i][0]
            else:
                grafo = texto_a_lista(case_list[i])
        
        grafo_lista_ady = convertir_a_lista_de_adyacencia(grafo)
        resp = fakenews(origen,grafo_lista_ady)
        print(resp)


main()

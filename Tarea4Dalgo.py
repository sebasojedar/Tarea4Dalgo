####
####   Tarea 4 Diseno y Analisis de Algoritmos
####
####   Integrantes y Codigo:
####   Juan Sebastian Ojeda Romero - 202110289
####   Johan Alejandro Charry Acevedo - 202111151
####

import sys

def conversor(lista):
    grafo = {}
    for arco in lista:
        v1, v2 = arco

        if v1 in grafo:
            grafo[v1].append(v2)
        else:
            grafo[v1] = []
            grafo[v1].append(v2)

        if v2 in grafo:
            grafo[v2].append(v1)
        else:
            grafo[v2] = []
            grafo[v2].append(v1)

    return grafo


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
    cola = []
    cola.append(origen)
    visitados = []
    visitados.append(origen)
    t = -1 

    while cola:
        por_visitar = len(cola)
        for _ in range(por_visitar):
            nodo_actual = cola.pop(0)
 
            for vecino in grafo[nodo_actual]:
                if vecino not in visitados:
                    visitados.append(vecino)
                    cola.append(vecino)
        t += 1 

    return t     


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
        
        grafo_lista_ady = conversor(grafo)
        resp = fakenews(origen,grafo_lista_ady)
        print(resp)

main()

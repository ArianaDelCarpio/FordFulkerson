import networkx as nx
import graphviz
import random
import os
import numpy as np
import heapq

def dibujar_menu():
    flow_navigator_word = [
        " _______  __        ______   ____    __    ____ ",
        "|   ____||  |      /  __  \  \   \  /  \  /   / ",
        "|  |__   |  |     |  |  |  |  \   \/    \/   /  ",
        "|   __|  |  |     |  |  |  |   \            /   ",
        "|  |     |  `----.|  `--'  |    \    /\    /    ",
        "|__|     |_______| \______/      \__/  \__/     ",
        "                                                                                                  ",
        ".__   __.      ___   ____    ____  __    _______      ___   .___________.  ______   .______       ",
        "|  \ |  |     /   \  \   \  /   / |  |  /  _____|    /   \  |           | /  __  \  |   _  \      ",
        "|   \|  |    /  ^  \  \   \/   /  |  | |  |  __     /  ^  \ `---|  |----`|  |  |  | |  |_)  |     ",
        "|  . `  |   /  /_\  \  \      /   |  | |  | |_ |   /  /_\  \    |  |     |  |  |  | |      /      ",
        "|  |\   |  /  _____  \  \    /    |  | |  |__| |  /  _____  \   |  |     |  `--'  | |  |\  \----. ",
        "|__| \__| /__/     \__\  \__/     |__|  \______| /__/     \__\  |__|      \______/  | _| `._____| ",
        "                                                                                                  "
    ]
    for line in flow_navigator_word:
        print(line)
    print("-----------------MENU-------------------")
    print("1. Algoritmo Ford Fulkerson\n")
    print("2. Creditos\n")
    print("3. Salir\n")

def dibujar_menu_matriz ():
    print("-----------Menu MATRIZ-----------\n")
    print("1. Generar matriz aleatoria\n")
    print("2. Asignar valores a la matriz\n")
if __name__ == '__main__':
    while True:
        opcion = 0
        os.system("cls" if os.name == "nt" else "clear")  # Limpiar la pantalla
        dibujar_menu()
        while opcion < 1 or opcion > 3:
            opcion = int(input("Elija una opción (1, 2 o 3): "))

        if opcion == 1:
                os.system("cls" if os.name == "nt" else "clear")  # Limpiar la pantalla
                dibujar_menu_matriz()
                opcion_matriz = 0
                while opcion_matriz < 1 or opcion_matriz > 2:
                    opcion_matriz = int(input("Elija una opción (1 o 2): "))
                    
            
        elif opcion == 2:
            retroceder = False
            while not retroceder:
                os.system("cls" if os.name == "nt" else "clear")  # Limpiar la pantalla
                print("                                                ___                    _     _                                          ")
                print("                                               (  _`\\                 ( ) _ ( )_                                        ")
                print("                                               | ( (_) _ __   __     _| |(_)| ,_)   _     ___                           ")
                print("                                               | |  _ ( '__)/'__`\\ /'_` || || |   /'_`\\ /',__)                          ")
                print("                                               | (_( )| |  (  ___/( (_| || || |_ ( (_) )\\__, \\                          ")
                print("                                               (____/'(_)  `\\____)`\\__,_)(_)`\\__)`\\___/'(____/                         ")
                print("                                                                                                                        ")
                print("                                                                                                                        ")
                print("                         __                                                                              ")
                print("                       .'  '.                                                                            ")
                print("                    .-'/  | 0|                                                                           ")
                print("       ,       _.-'  ,|  /    `.                                                                         ")
                print("      /|    .-'       `--''-._.'=================================-,                                      ")
                print("      | '-'`        .___.--._)===================================|                                      ")
                print("       |            .'      |          Integrantes               |                                      ")
                print("        |     /,_.-'        |  Arroyo Ormeño, André Alonso       | ")
                print("      _/   _.' (            |  Del Carpio Flores, Ariana Ileen   |                                      ")
                print("     /  ,-' |  |            |  Peña Rivera, Manuel Sebastian     |                                      ")
                print("     |  |    `-'            |  Ramirez Contreras, Zaid Valentino |                                      ")
                print("      `-'                   |  Ramirez Rodriguez, Diego Nicolás  |   ")
                print("                            '------------------------------------'                                      ")
                print("                                                                                                         ")
                retroceder = input("Presione Enter para volver al menú...")
        elif opcion == 3:
            print("Usted ha salido del programa")
            break

def agregar_arista(grafo, nodo_1, nodo_2, capacidad, dirigido=True):
    grafo.add_edge(nodo_1, nodo_2, capacity=capacidad)
    if not dirigido:
        grafo.add_edge(nodo_2, nodo_1, capacity=capacidad)

def generar_matriz_aleatoria(n):
    matriz = []
    for fila in range(n):
        fila_actual = []
        for columna in range(n):
            fila_actual.append(0)
        matriz.append(fila_actual)

    conectar_fuente_sumidero(matriz)
    conectar_nodos_intermedios_asimetrico(matriz)
    return matriz

def conectar_fuente_sumidero(matriz):
    n = len(matriz)
    for i in range(1, n - 1):
        matriz[0][i] = random.randint(1, 50)  # Conectar fuente a nodos intermedios
        matriz[i][n - 1] = random.randint(1, 50)  # Conectar nodos intermedios al sumidero

def conectar_nodos_intermedios_asimetrico(matriz):
    n = len(matriz)
    for i in range(1, n - 1):
        for j in range(1, n - 1):
            if i != j:
                matriz[i][j] = random.randint(1, 50)  # Conectar nodos intermedios entre sí
                matriz[j][i] = 0  # Asignar 0 a la arista inversa

def mostrar_matriz(matriz):
    n = len(matriz)
    
    # Imprimir encabezado de columnas con índices
    header = "    " + " ".join(str(i).rjust(4) for i in range(n))
    print(header)
    
    for i in range(n):
        # Imprimir índice de fila
        fila_str = str(i).rjust(2) + " |"
        for j in range(n):
            fila_str += str(matriz[i][j]).rjust(4) + " "
        print(fila_str)

def matriz_a_grafo(matriz):
    n = len(matriz)
    grafo = nx.DiGraph()

    for i in range(n):
        for j in range(n):
            capacidad = matriz[i][j]
            if capacidad > 0:
                agregar_arista(grafo, f'N{i}', f'N{j}', capacidad)

    return grafo

def mostrar_grafo_with_graphviz(grafo_original, grafo_fulkerson, flujo_dict, flujo_maximo):
    grafo_original_graphviz = graphviz.Digraph(format='png')
    
    grafo_original_graphviz.attr(rankdir='LR')  # Configurar dirección horizontal
    grafo_original_graphviz.attr(size='8000,6000')    # Ajustar tamaño de la imagen

    for u, v, data in grafo_original.edges(data=True):
        capacidad = data['capacity']
        flujo = flujo_dict.get(u, {}).get(v, 0)  # Obtener el flujo o 0 si no hay flujo definido
        etiqueta_arista = f"{capacidad}/{flujo}"
        grafo_original_graphviz.node(u)
        grafo_original_graphviz.node(v)
        grafo_original_graphviz.edge(u, v, label=etiqueta_arista)

    flujo_maximo_label = f"Flujo Máximo: {flujo_maximo}"
    grafo_original_graphviz.attr(label=flujo_maximo_label, labelloc='t')  # Coloca la etiqueta en la parte superior
    
    grafo_original_graphviz.view()

def encontrar_camino_aumentante(grafo_residual, nodo_fuente, nodo_destino):
    # Inicializamos las estructuras de datos
    visitados = set()  # Conjunto de nodos visitados
    padres = {}  # Diccionario para almacenar los padres de cada nodo en el camino
    cola_prioridad = []  # Cola de prioridad para explorar los nodos

    # Agregamos el nodo fuente a la cola de prioridad y lo marcamos como visitado
    heapq.heappush(cola_prioridad, (0, nodo_fuente))
    visitados.add(nodo_fuente)
    camino_encontrado = False  # Variable para indicar si se encontró un camino

    while cola_prioridad:
        _, nodo_actual = heapq.heappop(cola_prioridad)

        if nodo_actual == nodo_destino:
            camino_encontrado = True
            break

        # Exploramos los vecinos del nodo actual
        for vecino in grafo_residual.neighbors(nodo_actual):
            if grafo_residual[nodo_actual][vecino]['capacity'] > 0 and vecino not in visitados:
                visitados.add(vecino)
                padres[vecino] = nodo_actual
                heapq.heappush(cola_prioridad, (grafo_residual[nodo_actual][vecino]['capacity'], vecino))

    # Si encontramos un camino, lo reconstruimos
    if camino_encontrado:
        camino = []
        nodo = nodo_destino
        while nodo != nodo_fuente:
            camino.append(nodo)
            nodo = padres[nodo]
        camino.append(nodo_fuente)
        return camino[::-1]  # Devolvemos el camino invertido
    else:
        return None

def ford_fulkerson(grafo, nodo_fuente, nodo_destino):
    grafo_residual = grafo.copy()
    flujo_maximo = 0
    flujo_dict = {}  # Diccionario para almacenar el flujo en cada arco del grafo

    camino_aumentante = encontrar_camino_aumentante(grafo_residual, nodo_fuente, nodo_destino)
    iteracion = 1

    while camino_aumentante is not None:
        capacidad_minima = float('inf')

        # Encontramos la capacidad mínima en el camino aumentante
        for i in range(len(camino_aumentante) - 1):
            capacidad = grafo_residual[camino_aumentante[i]][camino_aumentante[i+1]]['capacity']
            capacidad_minima = min(capacidad_minima, capacidad)

        # Actualizamos el grafo residual y el flujo máximo
        for i in range(len(camino_aumentante) - 1):
            nodo_actual = camino_aumentante[i]
            nodo_siguiente = camino_aumentante[i+1]

            grafo_residual[nodo_actual][nodo_siguiente]['capacity'] -= capacidad_minima

            if not grafo_residual.has_edge(nodo_siguiente, nodo_actual):
                grafo_residual.add_edge(nodo_siguiente, nodo_actual, capacity=0)

            grafo_residual[nodo_siguiente][nodo_actual]['capacity'] += capacidad_minima

        flujo_maximo += capacidad_minima

        # Actualizamos el diccionario de flujo
        for i in range(len(camino_aumentante) - 1):
            u = camino_aumentante[i]
            v = camino_aumentante[i+1]
            flujo_dict[u] = flujo_dict.get(u, {})
            flujo_dict[u][v] = flujo_dict[u].get(v, 0) + capacidad_minima

        visualizar_recorrido(iteracion, camino_aumentante, capacidad_minima)
        iteracion += 1
        camino_aumentante = encontrar_camino_aumentante(grafo_residual, nodo_fuente, nodo_destino)

    return flujo_maximo, flujo_dict

def visualizar_recorrido(iteracion, camino, capacidad):
    print(f"Iteración {iteracion}: {'->'.join(map(str, camino))} capacidad {capacidad}")

def validar_nodo_fuente(n, matriz):
    while True:
        fuente = input(f"Ingrese el nodo fuente (N0 a N{n-1}): ")
        if fuente == 'N0':
            return fuente
        else:
            print("El nodo fuente no debe tener aristas entrantes")
            input("Presione Enter para continuar...")
            os.system('cls' if os.name == 'nt' else 'clear')
            mostrar_matriz_usuario(matriz)  # Volver a mostrar la matriz del usuario

def validar_nodo_sumidero(n, fuente, matriz):
    while True:
        sumidero = input(f"Ingrese el nodo sumidero (N0 a N{n-1}): ")
        if sumidero == fuente:
            print("El nodo sumidero no puede ser igual al nodo fuente.")
            input("Presione Enter para continuar...")
            os.system('cls' if os.name == 'nt' else 'clear')
            mostrar_matriz_usuario(matriz)  # Volver a mostrar la matriz del usuario
        elif sumidero == f'N{n-1}':
            return sumidero
        else:
            print("El nodo sumidero no puede tener aristas salientes")
            input("Presione Enter para continuar...")
            os.system('cls' if os.name == 'nt' else 'clear')
            mostrar_matriz_usuario(matriz)  # Volver a mostrar la matriz del usuario

def matriz_aleatoria_ford_fulkerson():
    n = 0    
    while n < 5 or n > 15:
        n = int(input("Ingrese un valor n entre 5 y 15: "))
    
    matriz_aleatoria = generar_matriz_aleatoria(n)
    print("-------------MATRIZ----------------------\n")
    mostrar_matriz(matriz_aleatoria)

    fuente = validar_nodo_fuente(n, matriz_aleatoria)
    sumidero = validar_nodo_sumidero(n, fuente, matriz_aleatoria)
    grafo_original = matriz_a_grafo(matriz_aleatoria)
    grafo_fulkerson = grafo_original.copy()

    flujo_maximo, flujo_dict = ford_fulkerson(grafo_fulkerson, fuente, sumidero)
    
    print("--------------Ford Fulkerson-----------------\n")
    print(f"Flujo máximo: {flujo_maximo}")
    print("Flujo por arista:")
    for u in flujo_dict:
        for v, flujo in flujo_dict[u].items():
            print(f"({u}, {v}): {flujo}")

    mostrar_grafo_with_graphviz(grafo_original, grafo_fulkerson, flujo_dict, flujo_maximo)
    input("Presione Enter para volver al menú...")
    os.system("cls")

def generar_matriz_usuario(n):
    matriz = np.zeros((n, n), dtype=int)  # Crear una matriz de ceros de tamaño nxn
    mostrar_matriz_usuario(matriz)
    llenar_matriz_usuario(matriz)
    return matriz

def mostrar_matriz_usuario(matriz):
    n = len(matriz)

    # Imprimir encabezado de columnas con índices
    header = "    " + " ".join(str(i).rjust(4) for i in range(n))
    print(header)

    for i in range(n):
        # Imprimir índice de fila
        fila_str = str(i).rjust(2) + " |"
        for j in range(n):
            fila_str += str(matriz[i][j]).rjust(4) + " "
        print(fila_str)

def llenar_matriz_usuario(matriz):
    n = matriz.shape[0]
    elementos_ingresados = 0
    
    for fila in range(n):
        for columna in range(n):
            if fila == columna:
                matriz[fila][columna] = 0
            elif matriz[fila][columna] == 0:
                os.system('cls' if os.name == 'nt' else 'clear')
                mostrar_matriz_usuario(matriz)
                
                if matriz[columna][fila] != 0:
                    print("La posición ({}, {}) ya tiene un valor asignado.".format(columna, fila))
                else:
                    if fila == n - 1:  # Comprobación de la fila n-1
                        matriz[fila][columna] = 0  # Se establece automáticamente en 0
                    else:
                        while True:
                            valor = int(input("Ingrese un valor (puede ser 0) para la posición ({}, {}): ".format(fila, columna)))
                            if valor >= 0:
                                matriz[fila][columna] = valor
                                elementos_ingresados += 1
                                break
                            else:
                                print("El valor debe ser un número no negativo.")
                
                os.system('cls' if os.name == 'nt' else 'clear')
                mostrar_matriz_usuario(matriz)
                
            if matriz[fila][columna] > 0 and matriz[columna][fila] == 0:
                matriz[columna][fila] = 0

    return matriz
def matriz_llenada_usuario_ford_fulkerson():
    n = 0    
    while n < 5 or n > 15:
        n = int(input("Ingrese un valor n entre 5 y 15: "))
    
    matriz_usuario = generar_matriz_usuario(n)
    fuente = validar_nodo_fuente(n, matriz_usuario)
    sumidero = validar_nodo_sumidero(n, fuente, matriz_usuario)
    grafo_original_usuario = matriz_a_grafo(matriz_usuario)
    grafo_usuario_fulkerson = grafo_original_usuario.copy()
    flujo_maximo, flujo_dict = ford_fulkerson(grafo_usuario_fulkerson, fuente, sumidero) #Ford Fulkerson
    
    print("--------------Ford Fulkerson-----------------\n")
    print(f"Flujo máximo: {flujo_maximo}")
    print("Flujo por arista:")
    for u in flujo_dict:
        for v, flujo in flujo_dict[u].items():
            print(f"({u}, {v}): {flujo}")

    mostrar_grafo_with_graphviz(grafo_original_usuario, grafo_usuario_fulkerson, flujo_dict, flujo_maximo)
    input("Presione Enter para volver al menú...")
if __name__ == '__main__':
    while True:
        opcion = 0
        dibujar_menu()
        while opcion < 1 or opcion > 3:
            opcion = int(input("Elija una opción (1, 2 o 3): "))
        
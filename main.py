import time

from utils.functions import (
    amostrar_sem_reposicao, 
    normalizar_probabilidades, 
    pre_processar_arestas,
    ConjuntoSolucao
)

# A variável vertices representa os vértices do grafo 
vertices = ['a', 'b', 'c']
# A variável arestas representa as arestas do grafo no formato (vértice1, vértice2, peso)
arestas = [
    ('a', 'b', 10),
    ('a', 'c', 8),
    ('b', 'c', 2)
]
# A cardinalidade da solução desejada
m = 3

def heuristica_roleta_russa(grafo, arestas, m):
    qtd_solucao_repetida = 0
    maior_solucao = float('-inf')
    melhor_solucao = None
    probabilidades = {v: 1 / len(grafo) for v in grafo}

    while qtd_solucao_repetida < 10:
        vetor_solucao = amostrar_sem_reposicao(probabilidades, m)
        conjunto_solucao = ConjuntoSolucao(arestas)
        for v in vetor_solucao:
            conjunto_solucao.adicionar_vertice(v)
        soma_pesos = conjunto_solucao.obter_soma()

        print("\nProbabilidades:", probabilidades)
        print("Solução atual:", vetor_solucao)
        print("Soma da solução atual:", soma_pesos)
        print("Maior solução:", maior_solucao)

        if soma_pesos > maior_solucao:
            maior_solucao = soma_pesos
            melhor_solucao = vetor_solucao
            for v in vetor_solucao:
                probabilidades[v] *= 1.3  
            qtd_solucao_repetida = 0
        elif soma_pesos == maior_solucao:
            qtd_solucao_repetida += 1
            for v in vetor_solucao:
                probabilidades[v] *= 1.1
        else:
            qtd_solucao_repetida = 0
            for v in vetor_solucao:
                probabilidades[v] *= 0.9  

        normalizar_probabilidades(probabilidades)

        time.sleep(1)

    if melhor_solucao is not None:
        print("\nMelhor solução encontrada:", melhor_solucao, "=>", maior_solucao)
        return melhor_solucao
    else:
        print("Nenhuma solução encontrada.")
        return None

arestas_pre_processadas = pre_processar_arestas(arestas)
heuristica_roleta_russa(vertices, arestas_pre_processadas, m)

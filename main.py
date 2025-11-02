import random
import time

vertices = ['a', 'b', 'c', 'd']
arestas = [
    ('a', 'b', 8),
    ('a', 'c', 5),
    ('a', 'd', 2),
    ('b', 'c', 6),
    ('b', 'd', 10),
    ('c', 'd', 7)
]
m = 3

def amostrar_sem_reposicao(probabilidades: dict[str, float], m: int) -> list[str]:
    """Seleciona m elementos distintos com base em pesos, sem reposição."""
    vertices = list(probabilidades.keys())
    pesos = list(probabilidades.values())
    selecionados = []

    for _ in range(min(m, len(vertices))):
        escolhido = random.choices(vertices, weights=pesos, k=1)[0]
        selecionados.append(escolhido)
        idx = vertices.index(escolhido)
        del vertices[idx]
        del pesos[idx]

    return selecionados


def soma_solucao(solucao, arestas):
    """Soma os pesos das arestas entre os vértices da solução."""
    soma = 0
    for i in range(len(solucao)):
        for j in range(i + 1, len(solucao)):
            u, v = solucao[i], solucao[j]
            for a, b, peso in arestas:
                if (a == u and b == v) or (a == v and b == u):
                    soma += peso
                    break
    return soma


def normalizar_probabilidades(probabilidades: dict[str, float]):
    """Garante que a soma dos pesos seja 1.0"""
    total = sum(probabilidades.values())
    if total == 0:
        n = len(probabilidades)
        for k in probabilidades:
            probabilidades[k] = 1 / n
    else:
        for k in probabilidades:
            probabilidades[k] /= total


def heuristica_roleta_russa(grafo, arestas, m):
    qtd_solucao_repetida = 0
    maior_solucao = float('-inf')
    melhor_solucao = None
    probabilidades = {v: 1 / len(grafo) for v in grafo}

    while qtd_solucao_repetida < 10:
        vetor_solucao = amostrar_sem_reposicao(probabilidades, m)
        soma_pesos = soma_solucao(vetor_solucao, arestas)

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

heuristica_roleta_russa(vertices, arestas, m)

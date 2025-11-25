import random

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
    n = len(solucao)

    for i in range(n):
        for j in range(i + 1, n):
            u, v = solucao[i], solucao[j]
            soma += arestas[u].get(v, 0) 
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

def pre_processar_arestas(arestas):
    arestas_final = {}
    for a, b, peso in arestas:
        arestas_final.setdefault(a, {})[b] = peso
        arestas_final.setdefault(b, {})[a] = peso
    return arestas_final
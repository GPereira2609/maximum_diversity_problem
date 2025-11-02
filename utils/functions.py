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
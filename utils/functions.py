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
    """Converte uma lista (u, v, peso) em um dict de adjacência."""
    adj = {}
    for u, v, w in arestas:
        adj.setdefault(u, {})[v] = w
        adj.setdefault(v, {})[u] = w
    return adj

class ConjuntoSolucao:

    def __init__(self, arestas):
        self.arestas = arestas
        self.vertices = []
        self.soma = 0

    def adicionar_vertice(self, vertice):
        for u in self.vertices:
            self.soma += self.arestas[u].get(vertice, 0)
        self.vertices.append(vertice)

    def obter_soma(self):
        return self.soma    
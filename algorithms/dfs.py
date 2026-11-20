from puzzle.base_search import BaseSearch
from puzzle.state import State
from puzzle.result import SearchResult

DEFAULT_DEPTH_LIMIT = 50


class DFS(BaseSearch):

    def __init__(self, depth_limit: int = DEFAULT_DEPTH_LIMIT):
        self.depth_limit = depth_limit

    def search(self, initial: State) -> SearchResult:
        pilha = [initial]
        visitados = {initial.tiles: 0}
        expandidos = 0
        gerados = 1
        max_fronteira = 1

        while pilha:
            atual = pilha.pop()

            if atual.is_goal:
                return SearchResult(atual, expandidos, gerados, max_fronteira, atual.cost)

            if atual.cost >= self.depth_limit:
                continue

            expandidos += 1
            for filho in atual.neighbors():
                # so visita de novo se chegou por um caminho mais curto
                if filho.tiles not in visitados or filho.cost < visitados[filho.tiles]:
                    visitados[filho.tiles] = filho.cost
                    pilha.append(filho)
                    gerados += 1

            max_fronteira = max(max_fronteira, len(pilha))

        return SearchResult(None, expandidos, gerados, max_fronteira, 0)

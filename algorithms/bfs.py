from collections import deque
from puzzle.base_search import BaseSearch
from puzzle.state import State
from puzzle.result import SearchResult


class BFS(BaseSearch):

    def search(self, initial: State) -> SearchResult:
        fronteira = deque([initial])
        visitados = {initial.tiles}
        expandidos = 0
        gerados = 1
        max_fronteira = 1

        while fronteira:
            atual = fronteira.popleft()

            if atual.is_goal:
                return SearchResult(atual, expandidos, gerados, max_fronteira, atual.cost)

            expandidos += 1
            for filho in atual.neighbors():
                if filho.tiles not in visitados:
                    visitados.add(filho.tiles)
                    fronteira.append(filho)
                    gerados += 1

            max_fronteira = max(max_fronteira, len(fronteira))

        return SearchResult(None, expandidos, gerados, max_fronteira, 0)

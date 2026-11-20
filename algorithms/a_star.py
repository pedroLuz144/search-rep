import heapq
from puzzle.base_search import BaseSearch
from puzzle.state import State
from puzzle.result import SearchResult


class AStar(BaseSearch):

    def heuristic(self, state: State) -> int:
        # distancia de Manhattan
        total = 0
        for i, peca in enumerate(state.tiles):
            if peca != 0:
                destino = peca - 1
                total += abs(i // 3 - destino // 3) + abs(i % 3 - destino % 3)
        return total

    def search(self, initial: State) -> SearchResult:
        contador = 0  # desempate na heap
        fronteira = [(self.heuristic(initial), contador, initial)]
        melhor_custo = {initial.tiles: 0}
        expandidos = 0
        gerados = 1
        max_fronteira = 1

        while fronteira:
            _, _, atual = heapq.heappop(fronteira)

            if atual.is_goal:
                return SearchResult(atual, expandidos, gerados, max_fronteira, atual.cost)

            # ignora se ja achou um caminho melhor pra esse estado
            if atual.cost > melhor_custo[atual.tiles]:
                continue

            expandidos += 1
            for filho in atual.neighbors():
                if filho.tiles not in melhor_custo or filho.cost < melhor_custo[filho.tiles]:
                    melhor_custo[filho.tiles] = filho.cost
                    contador += 1
                    f = filho.cost + self.heuristic(filho)
                    heapq.heappush(fronteira, (f, contador, filho))
                    gerados += 1

            max_fronteira = max(max_fronteira, len(fronteira))

        return SearchResult(None, expandidos, gerados, max_fronteira, 0)

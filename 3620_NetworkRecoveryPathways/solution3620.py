from typing import List
from collections import deque



def meineLoesung(edges: List[List[int]],online: List[bool],k: int) -> int:

    queue = deque()
    target = len(online) - 1
    best_score = -1

    for start, end, cost in edges:
        if start == 0:
            queue.append((start,end,
                cost,   # Kosten der aktuellen Kante
                cost,   # bisherige Gesamtkosten
                cost    # bisher kleinste Kante
            ))

    while queue:
        here_node, next_node, edge_cost, total_cost, min_edge = queue.popleft()

        if total_cost > k:
            continue
        if not online[next_node]:
            continue
        if next_node == target:
            best_score = max(best_score, min_edge)
            continue

        for next_start, next_end, next_edge_cost in edges:
            if next_start == next_node:
                new_total_cost = total_cost + next_edge_cost
                new_min_edge = min(min_edge, next_edge_cost)

                queue.append((next_start,next_end,next_edge_cost,new_total_cost,new_min_edge))

    return best_score


def optimaleLoesung(edges: List[List[int]],online: List[bool],k: int) -> int:
    """
    Dies ist ein DAG (Directed Acyclic Graph, gerichteter azyklischer Graph, also Kanten haben Richtungen und es ist kein KReis)
    meine BFS-Lösung war zu langsam, deshalb per Binärsuche mit
    Adjazenzliste (Adjacent) und topologische Sortierung (DP-Dynamic Programming, hier bester Pfad zu diesem Node)
    weil Kanten verschiedene Kosten, dadurch bedeutet weniger Kanten nicht automatisch geringere Kosten! BFS kann den direkten Weg zuerst finden,
    aber nicht den günstigsten.
    """
    n = len(online)
    
    #für jeden Knoten eigene leere Liste später mit endNode und cost befüllen pro startNode
    graph = [[] for _ in range(n)]

    # für jeden Node Anzahl eingehender Kanten
    indegree = [0] * n

    for start, end, cost in edges:
        graph[start].append((end, cost))
        indegree[end] += 1

    # Topologische Reihenfolge bestimmen
    queue = deque()

    for node in range(n):
        if indegree[node] == 0:
            queue.append(node)

    topological_order = []

    while queue:
        node = queue.popleft()
        topological_order.append(node)

        for next_node, edge_cost in graph[node]:
            indegree[next_node] -= 1

            if indegree[next_node] == 0:
                queue.append(next_node)

    # Prüft, ob ein gültiger Pfad mit unseren Bedingungen (BottleNecks):
    # Mindestkante >= min_score 
    # nur online nodes
    # k nicht überschreiten
    # existiert
    def can_reach(min_score: int) -> bool:
        infinity = float("inf")

        # Liste aus n-Elementen von unendlich (distanz-werte von Knoten 0 zu Knoten index) -> Kostwerte von 0 zum jeweiligen Knoten, anfangs noch unbekannt,
        # bzw. unendlich hoch also noch nicht erreicht.
        distance = [infinity] * n
        distance[0] = 0

        for node in topological_order:
            if distance[node] == infinity:
                continue

            # Offline-Zwischenknoten nicht weiterverwenden
            if node != 0 and node != n - 1 and not online[node]:
                continue

            for next_node, edge_cost in graph[node]:
                # Kante erfüllt den gewünschten Mindestscore nicht
                if edge_cost < min_score:
                    continue

                # Offline-Zwischenknoten dürfen nicht betreten werden
                if (
                    next_node != n - 1
                    and not online[next_node]
                ):
                    continue

                new_cost = distance[node] + edge_cost

                if new_cost < distance[next_node]:
                    distance[next_node] = new_cost

        return distance[n - 1] <= k

    # Alle unterschiedlichen Kantenkosten aufsteigend sortieren, da nur diese Werte als möglicher Pfad-Score infrage kommen
    # Sorted List aus Set aus Kosten aller Edges.
    possible_scores = sorted({cost for _, _, cost in edges})

    left = 0
    right = len(possible_scores) - 1
    answer = -1

    # Binärsuche über possibleScores.
    while left <= right:
        middle = (left + right) // 2
        score = possible_scores[middle]

        if can_reach(score):
            answer = score
            left = middle + 1
        else:
            right = middle - 1

    return answer

def main():
    input=[[0,1,5],[1,3,10],[0,2,3],[2,3,4]]
    input2=[True,True,True,True]
    input3=10

    print("--- meine Lösung ---")
    print(meineLoesung(input,input2,input3))
    print("--- optimale Lösung ---")
    print(optimaleLoesung(input,input2,input3))

if __name__=="__main__":
    main()
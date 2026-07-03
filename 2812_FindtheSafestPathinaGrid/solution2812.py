from typing import List
from collections import deque
import heapq


def meineLoesung( grid: List[List[int]]) -> int:
    """
        BFS -> Breadth First Search Algorithmus, per queue Ebenen durchsuchen/abarbeiten, im Gegensatz zu Rekursiv/Depth-First-Search
    """
    n = len(grid)
    distances = [[-1] * n for _ in range(n)]
    queue = deque()

    for r in range(n):
        for c in range(n):
            if grid[r][c] == 1:
                distances[r][c] = 0
                queue.append((r, c))

    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    while queue:
        r, c = queue.popleft()

        for dr, dc in directions:
            nr = r + dr
            nc = c + dc

            if 0 <= nr < n and 0 <= nc < n and distances[nr][nc] == -1:
                distances[nr][nc] = distances[r][c] + 1
                queue.append((nr, nc))

    max_heap = [(-distances[0][0], 0, 0)]
    visited = [[False] * n for _ in range(n)]

    while max_heap:
        safeness, r, c = heapq.heappop(max_heap)
        safeness = -safeness

        if visited[r][c]:
            continue

        visited[r][c] = True

        if r == n - 1 and c == n - 1:
            return safeness

        for dr, dc in directions:
            nr = r + dr
            nc = c + dc

            if 0 <= nr < n and 0 <= nc < n and not visited[nr][nc]:
                next_safeness = min(safeness, distances[nr][nc])
                heapq.heappush(max_heap, (-next_safeness, nr, nc))

    return 0
        

def optimaleLoesung():
    return

def main():
    input=[[1,0,0],[0,0,0],[0,0,1]]
    print("--- meine Lösung ---")
    print(meineLoesung(input))
    print("--- optimale Lösung ---")
    print(optimaleLoesung())

if __name__=="__main__":
    main()
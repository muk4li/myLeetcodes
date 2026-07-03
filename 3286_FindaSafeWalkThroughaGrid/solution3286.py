from typing import List
import heapq

def meineLoesung( grid: List[List[int]], health: int) -> bool:
    zeilen = len(grid)
    spalten = len(grid[0])

    startHP = health - grid[0][0]

    if startHP <= 0:
        return False
    
    maxHeap = [(-startHP,0,0)]
    optimaleHP = [[-1] * spalten for _ in range(zeilen)]
    optimaleHP[0][0] = startHP

    directions = [(1,0),(-1,0),(0,1),(0,-1)]

    while maxHeap:
        aktuelleHP, zeile, spalte = heapq.heappop(maxHeap)
        aktuelleHP = -aktuelleHP

        if zeile == zeilen -1 and spalte == spalten - 1:
            return True

        if aktuelleHP < optimaleHP[zeile][spalte]:
            continue

        for x,y in directions:
            naechsteZeile = zeile + x
            naechsteSpalte = spalte + y

            if 0 <= naechsteZeile < zeilen and 0 <= naechsteSpalte < spalten:
                HP = aktuelleHP - grid[naechsteZeile][naechsteSpalte]

                if HP > 0 and HP > optimaleHP[naechsteZeile][naechsteSpalte]:
                    optimaleHP[naechsteZeile][naechsteSpalte]= HP
                    heapq.heappush(maxHeap,(-HP,naechsteZeile,naechsteSpalte))
    return False





def optimaleLoesung():
    return

def main():
    input1=[[0,1,0,0,0],[0,1,0,1,0],[0,0,0,1,0]]
    input2=1
    print("--- meine Lösung ---")
    print(meineLoesung(input1,input2))
    print("--- optimale Lösung ---")
    print(optimaleLoesung())

if __name__=="__main__":
    main()
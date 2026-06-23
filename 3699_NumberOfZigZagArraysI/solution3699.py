def meineLoesung(n, l, r):
    MOD = 10**9 + 7

    länge = n
    _range = range(l, r + 1)

    # dp[i][dir][x] = Anzahl Folgen der Länge i,
    # die bei Wert x enden und als nächstes Richtung dir brauchen
    #
    # dir = 0 bedeutet: nächster Wert muss kleiner sein
    # dir = 1 bedeutet: nächster Wert muss größer sein

    dp = {}

    # Start: Folgen der Länge 1
    for jedeZahl in _range:
        dp[(1, 0, jedeZahl)] = 1
        dp[(1, 1, jedeZahl)] = 1

    # Folgen von Länge 2 bis n aufbauen
    for aktuelleLänge in range(1, länge):
        neueDp = {}

        for (alteLänge, richtung, letzteZahl), anzahl in dp.items():

            # Nur Zustände der aktuellen Länge weiterverarbeiten
            if alteLänge != aktuelleLänge:
                continue

            for jedeZahl in _range:

                # nächster Wert muss größer sein
                if richtung == 1 and jedeZahl > letzteZahl:
                    neueRichtung = 0
                    key = (aktuelleLänge + 1, neueRichtung, jedeZahl)

                    if key not in neueDp:
                        neueDp[key] = 0

                    neueDp[key] += anzahl
                    neueDp[key] %= MOD

                # nächster Wert muss kleiner sein
                if richtung == 0 and jedeZahl < letzteZahl:
                    neueRichtung = 1
                    key = (aktuelleLänge + 1, neueRichtung, jedeZahl)

                    if key not in neueDp:
                        neueDp[key] = 0

                    neueDp[key] += anzahl
                    neueDp[key] %= MOD

        dp = neueDp

    if n == 1:
        return r - l + 1

    output = 0

    for (aktuelleLänge, richtung, letzteZahl), anzahl in dp.items():
        if aktuelleLänge == n:
            output += anzahl
            output %= MOD

    return output

def optimaleLoesung():
    return

def main():
    inputN=3
    inputL=4
    inputR=5 
    print("--- meine Lösung ---")
    print(meineLoesung(inputN,inputL,inputR))
    print("--- optimale Lösung ---")
    print(optimaleLoesung())

if __name__=="__main__":
    main()
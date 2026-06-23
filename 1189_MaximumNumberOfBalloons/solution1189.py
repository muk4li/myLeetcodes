def meineLoesung(text):
    # balloon = {'b': 1, 'a': 1, 'l': 2, 'o': 2, 'n': 1}
    balloon = {char: "balloon".count(char) for char in dict.fromkeys("balloon")}
    output =0
    vergleich = dict.fromkeys("balloon", 0)
    for char in text:
        if char in balloon:
            vergleich[char] += 1
    
    while True:
        for match in balloon:
            vergleich[match] -= balloon[match]

        if any(value < 0 for value in vergleich.values()):
            break

        output += 1

    return output

def optimaleLoesung1runtime(text):
    from collections import defaultdict
    d = defaultdict(int)
    word = "balloon"
    for t in text:
        if t in word:
            d[t] +=1
    
    if any(t not in d for t in word):
        return 0
    else:
        return min(d['b']//1, d['a']//1, d['l']//2, d['o']//2, d['n']//1)

def optimaleLoesung2memory(text):
    """
    ein Set, reine Sammlung von einzigartigen Objekten, unsortiert, ohne Index. nur zum abgleichen wie oft die jeweiligen Buchstaben
    von balloon in text vorkommen, bei den doppelt vorkommenden ganzzahlig durch zwei und dann den kleinsten Wert der Vorkommnisse nehmen.
    """
    BALLOON_LETTERS = set("balon")
    DOUBLE_LETTERS = set("lo")

    letters = {ch: 0 for ch in BALLOON_LETTERS}

    for ch in text:
        if ch in letters:
            letters[ch] += 1

    for ch in DOUBLE_LETTERS:
        letters[ch] //= 2

    return min(letters.values())

def main():
    input="nlaebolko" 
    print("--- meine Lösung ---")
    print(meineLoesung(input))
    print("--- optimale Lösung runtime---")
    print(optimaleLoesung1runtime(input))
    print("--- optimale Lösung memory---")
    print(optimaleLoesung2memory(input))

if __name__=="__main__":
    main()
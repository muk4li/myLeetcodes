def meineLoesung(input:str):
    buchstabenAnzahl = len(input)
    bestmatch = ""

    for start in range(buchstabenAnzahl):
        palitest = ""
        palicontrol = ""

        for i in range(start, buchstabenAnzahl):
            palitest = palitest + input[i]
            palicontrol = input[i] + palicontrol

            if palitest == palicontrol and len(palitest) > len(bestmatch):
                bestmatch = palitest
    return bestmatch

def meineLoesung2(s: str):
    """
    Python-idiomatischer
    [start:stop:step] -> bei start stop leer (anfang und ende default) und step -1,
    step wert auf negativ kehrt die default-Werte um.
    """
    bestmatch = ""

    for start in range(len(s)):
        for end in range(start + 1, len(s) + 1):
            substring = s[start:end]

            if substring == substring[::-1] and len(substring) > len(bestmatch):
                 bestmatch = substring

    return bestmatch

def optimaleLoesung(s):
    """
    Early Exit, Hilfsfunktion die zwischen den zwei angegeben Stellen des Strings (bei identischen Stellen ist es der eine Buchstabe odd-länge)
    die Mitte des Palindroms definiert und von da aus prüft ob das jeweilige Palindrom noch größer sein könnte, es werden die Indizes 
    der höchstmöglichen Anzahl/Länge des Palindroms gespeichert.
    Für jeden Index des String findet diese Abfrage statt, sobald eine gefundene Palindromlänge größer ist als die vorige werden die Indizes
    gespeichert. Am Ende werden die zuletzt gespeicherten Indizes für die Ausgabe des Substrings verwendet.
    """
    if not s:
        return ""

    def expand_around_center(s: str, left: int, right: int):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return right - left - 1


    start = 0
    end = 0

    for i in range(len(s)):
        odd = expand_around_center(s, i, i)
        even = expand_around_center(s, i, i + 1)
        max_len = max(odd, even)
        
        if max_len > end - start:
            start = i - (max_len - 1) // 2
            end = i + max_len // 2
    
    return s[start:end+1]

def main():
    input="labubusixseven"
    print("--- meine erste falsche Lösung ---")
    print(meineLoesung(input))
    print("--- meine Lösung2 ---")
    print(meineLoesung2(input))
    print("--- optimale Lösung ---")
    print(optimaleLoesung(input)) 

if __name__=="__main__":
    main()
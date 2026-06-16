def meineLoesung(x):
    x_string=str(x)

    is_negative=False
    if x_string.startswith("-"):
        x_string=x_string.removeprefix("-")
        is_negative = True

    reversed_x_string=""
    for letter in x_string:
        reversed_x_string= letter + reversed_x_string
    
    if is_negative:
        reversed_x_string = "-" + reversed_x_string

    reversed_x=int(reversed_x_string)

    if reversed_x < -2147483647 or reversed_x > 2147483647:
        return 0
    
    return reversed_x

def optimaleLoesung(x):
    """
    Bit-Shifting um int32-Grenzen zu berechnen (verschiebe binär 1 um 31 Bits nach links, diese Zahl dann -1 um die positive Grenze zu bekommen)
    Vorzeichen-Logik über kleiner als null und abs(). Über Modulo 10 die letzte Stelle (digit) bekommen und zur ersten/nächsten Stelle umwandeln.
    Checken ob unsere nächste result ausrechnung int32 sprengen würde.
    """
    #INT_MIN = -(1 << 31)
    INT_MAX = (1 << 31) - 1

    sign = -1 if x < 0 else 1
    x = abs(x)

    result = 0

    while x != 0:
        digit = x % 10
        x //= 10

        # Overflow-Check, bevor result * 10 + digit passiert
        if result > (INT_MAX - digit) // 10:
            return 0

        result = result * 10 + digit

    return sign * result

def main():
    input=-200 
    print("--- meine Lösung ---")
    print(meineLoesung(input))
    print("--- optimale Lösung ---")
    print(optimaleLoesung(input))

if __name__=="__main__":
    main()
def meineLoesung(s):
    output = ""

    for char in s:
        match char:
            case "*":
                output = output[:-1]

            case "#":
                output += output

            case "%":
                output = output[::-1]

            case _:
                output += char

    return output

def optimaleLoesung():
    """
    Meine war schon die beste 100% runtime| 98% memory
    """
    return

def main():
    input="" 
    print("--- meine Lösung ---")
    print(meineLoesung(input))
    print("--- optimale Lösung ---")
    print(optimaleLoesung())

if __name__=="__main__":
    main()
def meineLoesung(input_string,rows):
    output=None
    if rows == 1 or rows >= len(input_string):
        return input_string
    
    jaggy=[""]*rows

    while input_string != "":
        for i in range(rows):
            if input_string=="":
                break
            jaggy[i] += input_string[0]
            input_string= input_string[1:]

        for i in range(rows-2,0,-1):
            if input_string=="":
                break
            jaggy[i] += input_string[0]
            input_string= input_string[1:]

    output="".join(jaggy)

    return output

def optimaleLoesung(s, rows):
    """
    Performanter durch Abarbeitung von s und keine String-Manipulation (ersten char löschen, wie bei meiner Lösung)
    und Char-Liste.append und nicht array/list aus Zeilen-String (weniger Speicher/Manipulation). 
    Über Index-Speicherung (current row) und "Navigation" (direction) keine verschachtelte Schleife.

    """
    if rows == 1 or rows >= len(s):
        return s

    jaggy = [[] for _ in range(rows)] # Liste aus Char-List
    current_row = 0
    direction = 1

    for char in s:
        jaggy[current_row].append(char)

        if current_row == 0:
            direction = 1
        elif current_row == rows - 1:
            direction = -1

        current_row += direction

    return "".join("".join(row) for row in jaggy)

def main():
    input1="P     I    N\n"\
        "A   L S  I G\n"\
        "Y A   H R\n"\
        "P     I" 
    legitinput1="PAYPALISHIRING"
    input2=4
    print("--- meine Lösung ---")
    print(meineLoesung(legitinput1,input2))
    print("--- optimale Lösung ---")
    print(optimaleLoesung())

if __name__=="__main__":
    main()
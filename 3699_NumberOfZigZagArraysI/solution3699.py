def meineLoesung(n,l,r):
    output=0
    länge = n
    _range= range(l,r+1)
    
    dp =[]
    direction=[0,1]

    def getdp(startwert,alle,dir):
        array=[startwert]

        for index in range(länge-1):
            for nächsterwert in alle:
                if dir==1:
                    if nächsterwert > array[index]:
                        array.append(nächsterwert)
                        dir = 0
                        break
                if dir==0:
                    if nächsterwert < array[index]:
                        array.append(nächsterwert)
                        dir = 1
                        break
        dp.append(array)

    for zahl in _range:
        for richtung in direction:
            getdp(zahl,_range,richtung)

    output = len(dp)

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
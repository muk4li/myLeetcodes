def meineLoesung(n):
    stringOfN = str(n)
    sum = 0
    stringOfX ="0"
    for digit in stringOfN:
        if digit != "0":
            sum += int(digit)
            stringOfX = stringOfX + digit
    return sum * int(stringOfX)


def optimaleLoesung(n):
    if n==0:
        return 0
    digits = []
    n2 = n
    while n2:
        d = n2%10
        if d>0:
            digits.append(d)
        n2 = n2 // 10
    s = sum(digits)
    ans = 0
    for i, d in enumerate(digits):
        ans += (d*10**i)
    return ans*s

def optimaleLoesung2(n):
    temp = str(n)
    sum=0
    x=""
    for i in temp:
        if int(i)!=0:
            x+=i
            sum+=int(i)
    
    if x=="":
        x=0
    return int(x)*sum

def main():
    input=10203004
    print("--- meine Lösung ---")
    print(meineLoesung(input))
    print("--- optimale Lösung Performance---")
    print(optimaleLoesung(input))
    print("--- optimale Lösung Memory---")
    print(optimaleLoesung2(input))

if __name__=="__main__":
    main()
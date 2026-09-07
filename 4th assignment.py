while True:
    def fibonacci_serise (a , serise = None ):
        if serise is None:
            serise = {}

        if a <= 1:
            return a
        if a in serise:
            return serise[a]

        serise[a] = fibonacci_serise(a - 1, serise) + fibonacci_serise(a - 2,serise)
        return serise[a]

    a = int(input("enter your values :"))
    print("fibonacci number using memoization :",fibonacci_serise(a))
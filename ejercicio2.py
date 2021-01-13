def numeros():
    numeros = 1 #1
    while numeros <= 100: #100
        numeros = numeros + 1 #1

        if numeros % 3 == 0 and numeros % 5 == 0:  #1
            print("Fizz Buzz") #1
        elif numeros%3==0: #1
            print("Fizz") #1
        elif numeros%5==0: #1
            print("Buzz") #1
        else:
            print(numeros) #1

numeros()

#complejidad big-o es 100
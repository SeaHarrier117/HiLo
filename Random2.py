print("Think of a number between 0 and 100")
hi=100
lo=0
guess = False

while guess == False:
    answer = (hi+lo)/2
    print(answer)
    response = input("Is this your number?")
    if response == "y":
        guess = True
        print("Finished")
    elif response == "n":
        hilo = input("High or Low?")
        if hilo == "High":
            hi = answer
        if hilo == "Low":
            lo = answer
    else:
        print("Unknown command")
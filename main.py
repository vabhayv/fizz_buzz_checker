print("Welcome to the Fizz Buzz Game Checker!!")
know = input("If you wanna know about How to play Fizz Buzz Game press y and hit enter.\nOr \njust tap enter to check.").lower()
if know == "y":
    print("Its very simple and interesting game.\n\nWe have to call the numbers starting from 1\nbut however the number is divisible by 3 we have to say fizz\nand if the number is divisible by 5 we have to say buzz\nand if the number is divisible by 3&5 we have to say fizzbuzz")
    print(f"Example :")
    for i in range(1,16):
        if i%3==0 and i%5==0:
            print("fizzbuzz")
        elif i%3==0:
            print("fizz")
        elif i%5==0:
            print("buzz")
        else :
            print(i)
    print("So thats the game! It's interesting right?")
else:
    start = int(input("you wanna check from : "))
    end = int(input("till? : "))
    for fizzbuzz in range(start,end+1):
        if fizzbuzz%3==0 and fizzbuzz%5==0:
            print("Fizzbuzz")
        elif fizzbuzz%3==0:
            print("Fizz")
        elif fizzbuzz%5==0:
            print("Buzz")
        else:
            print(fizzbuzz)
    

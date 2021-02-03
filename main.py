import mymodule

if __name__ == "__main__":
    file1 = open("finalTraverse.txt", "w")
    while True:
        userInput = input()
        if userInput == "end":
            break
        primeCheck = mymodule.primecheck(int(userInput))
        print(primeCheck)
        file1.write(userInput + " ")
        file1.write(primeCheck + "\n")
    file1.close()

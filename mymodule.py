def primecheck(num):
    file = open("prime.txt")
    prime_list = file.readlines();
    print(prime_list)
    for i in range(len(prime_list)):
        prime_list[i] = prime_list[i][:-1]

    if 0 < num < 21:
        if str(num) in prime_list:
            return "prime"
        else:
            return "not prime"
    else:
        return "out of range"

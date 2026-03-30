class Calculator:
    
    def add(n1,n2):
        return n1 + n2

    def sub(n1,n2):
        return n1 - n2

    def mul(n1,n2):
        return n1 * n2

    def div(n1,n2):
        return n1 / n2

    def mod(n1,n2):
        return n1 % n2

    def exp(n1,n2):
        return n1 ** n2

    choice = "yes"
    while choice.lower() == "yes":
        
        print("please enter your option-\n"
                "1. Add\n"
                "2. Subtract\n"
                "3. Multiply\n"
                "4. Divide\n"
                "5. Modulus\n"
                "6. Exponential\n")

        sel = int(input("Select operation (1-6): "))
        n1 = int(input("Enter first number: "))
        n2 = int(input("Enter second number: "))




        if sel == 1:
            print(n1, "+", n2, "=", add(n1,n2))
        elif sel == 2:
            print(n1, "-", n2, "=", sub(n1,n2))
        elif sel == 3:
            print(n1, "*", n2, "=", mul(n1,n2))
        elif sel == 4:
            print(n1, "/", n2, "=", div(n1,n2))
        elif sel == 5:
            print(n1, "%", n2, "=", mod(n1,n2))
        elif sel == 6:
            print(n1, "**", n2, "=", exp(n1,n2))
        else:
            print("Invalid input")

        choice = input("Do you want to continue? (yes/no): ")

print("Ok, Bye")




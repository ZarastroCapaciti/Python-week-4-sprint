def calculate(input):
    answer = eval(input)
    return answer
while True:
    calcbool = input("Do you have an equation you want solved? (Y/N) ")
    if calcbool[0].lower() == "y":
        string = input("Enter your equation: ")
        print(string + " =")
        print(str(calculate(string)))
    elif calcbool[0].lower() == "n":
        print("See you next time")
        exit()
    else:
        print("Invalid input")
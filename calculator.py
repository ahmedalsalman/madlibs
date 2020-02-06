def main():

    number1 = input("Enter first number:  ")
    number2 = input("Enter second number:  ")
    operation = str(input("Choose the operation (+, -, /, *):"))

    if  number1.isnumeric() and number2.isnumeric() == True:
            number1 = int(number1)
            number2 = int(number2)

            if operation == "+":
                print(f"the answer is {number1 + number2}")
            elif operation == "-":
                print(f"the answer is {number1 - number2}")
            elif operation == "*":
                print(f"the answer is {number1 * number2}")
            elif operation == "/":
                print(f"the answer is {number1 / number2}")
            else:
                print("Invalid operation, try again")


    else:
            print("One or both numbers are invalid.")



if __name__ == '__main__':
    main()

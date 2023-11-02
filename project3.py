#Ryan Chung #100867856

class BasicCalculator:
    def add(self, num1, num2):#basic adddition calculator
        return num1 + num2

    def subtract(self, num1, num2):#basic subtract calculator
        return num1 - num2

    def multiply(self, num1, num2):#basic product calculator
        return num1 * num2

    def divide(self, num1, num2):#basic quotient calculator
        return num1 / num2


class AdvancedCalculator(BasicCalculator):
    def add(self, num1, num2): #advanced addition 
        try:
            result = num1 + num2
        except TypeError:
            print("Invalid input type")
        else:
            return result

    def subtract(self, num1, num2):# advanced subtraction
        try:
            result = num1 - num2
        except TypeError:
            print("Invalid input type")
        else:
            return result

    def multiply(self, num1, num2):#advanced product
        try:
            result = num1 * num2
        except TypeError:
            print("Invalid input type")
        else:
            return result

    def divide(self, num1, num2):#advanced quotient
        try:
            result = num1 / num2
        except TypeError:
            print("Invalid input type")
        except ZeroDivisionError:
            print("Cannot divide by zero")
        else:
            return result
if __name__ == '__main__': #calling functions
    calc = AdvancedCalculator()

    operations = []
    try:
        while True:
            operation = input("What operation would you like to perform? ")
            if operation.lower() == "addition" or operation == "+": #calling addition function
                num1 = float(input("Enter the first number: "))
                num2 = float(input("Enter the second number: "))
                result = calc.add(num1, num2)
                print(f"{num1} + {num2} = {result}")
            elif operation.lower() == "subtraction" or operation == "-":#calling subtraction function
                num1 = float(input("Enter the first number: "))
                num2 = float(input("Enter the second number: "))
                result = calc.subtract(num1, num2)
                print(f"{num1} - {num2} = {result}")
            elif operation.lower() == "multiplication" or operation == "*":#calling product function
                num1 = float(input("Enter the first number: "))
                num2 = float(input("Enter the second number: "))
                result = calc.multiply(num1, num2)
                print(f"{num1} * {num2} = {result}")
            elif operation.lower() == "division" or operation == "/":#calling quotient function
                num1 = float(input("Enter the first number: "))
                num2 = float(input("Enter the second number: "))
                result = calc.divide(num1, num2)
                print(f"{num1} / {num2} = {result}")
            elif operation.lower() == "stop": #ending program with "stop"
                break
            else:
                print("Invalid operation")
                continue
    except:
        print("Error: you did not enter a operation")

#End#
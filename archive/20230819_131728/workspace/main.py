from calculator import Calculator

def main():
    calculator = Calculator()
    while True:
        print("\n1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")
        choice = int(input("Enter your choice: "))
        if choice == 5:
            break
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        if choice == 1:
            print("Result: ", calculator.add(num1, num2))
        elif choice == 2:
            print("Result: ", calculator.subtract(num1, num2))
        elif choice == 3:
            print("Result: ", calculator.multiply(num1, num2))
        elif choice == 4:
            print("Result: ", calculator.divide(num1, num2))

if __name__ == "__main__":
    main()

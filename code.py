def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

def exponentation(x, y):
    return x ** y

def modulo(x, y):
    return x % y

print("select operation:")
print("1.add")
print("2.subtract")
print("3.multiply")
print("4.divide")
print("5.exponentation")
print("6.modulo")

while True:
    
    choice = input("enter choice(1/2/3/4/5): ")

    if choice in ('1', '2', '3', '4', '5', '6'):
        num1 = float(input("enter first number: "))
        num2 = float(input("enter second number: "))

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))
            
        elif choice == '5':
            print(num1, "^", num2, "=", exponentation(num1, num2))
            
        elif choice == '6':
            print(num1, "%", num2, "=", modulo(num1, num2))
        
        next_calculation = input("let's do next calculation? (y/n): ")
        if next_calculation == "n":
          break
    
    else:
        print("wrong input")

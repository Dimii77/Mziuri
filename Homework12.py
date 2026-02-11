#1
print("----#1----")
while True:
    try:
        num1 = float(input("Enter First Number: "))
        num2 = float(input("Enter Second Number: "))

        result = num1 / num2
        print("Result:", result)
        break

    except ValueError:
        print("Error, Enter a Valid Number.")
    except ZeroDivisionError:
        print("Error, Division by zero.")

#2
print("----#2----")
def divide_numbers(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Error, Division by zero."
    except TypeError:
        return "Error, Both must be numbers."

print(divide_numbers(15, 5))
print(divide_numbers(67, 0))
print(divide_numbers("a", 9))

#3
print("----#3----")
try:
    numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    index = int(input("Enter index (0-9): "))
    print("Elementia:", numbers[index])
except IndexError:
    print("Error, Index out of range.")
except ValueError:
    print("Error, Enter a digit.")

#3
print("----#4----")
try:
    file = open("myresult.txt", "r")
    content = file.read()
    print(content)
except FileNotFoundError:
    print("Error, File does not exist.")


#5
print("----#5----")

import math

try:
    e = float(input("sheiyvane 'e' koeficienti: "))
    f = float(input("sheiyvane 'f' koeficienti: "))
    h = float(input("sheiyvane 'h' koeficienti: "))

    if e == 0:
        raise ValueError("koeficienti 'a' ar sheidzleba iyos 0.")

    discriminant = f ** 2 - 4 * e * h

    if discriminant < 0:
        raise ValueError("Uaryofit diskriminants ar aqvs fesvi")

    x1 = (-f + math.sqrt(discriminant)) / (2 * e)
    x2 = (-f - math.sqrt(discriminant)) / (2 * e)

    print("Fesvebia:", x1, "da", x2)

except ValueError as e:
    print("Error:", e)

#6
print("----#6----")

try:
    x = int(input("Enter first side: "))
    y = int(input("Enter second side: "))
    z = int(input("Enter third side: "))

    if x + y > z and x + z > y and y + z > x:
        average = (x + y + z) / 3
        print("Arithmetic mean:", average)
    else:
        raise ValueError("Ver warmoiqmneba samkutxedi")

except ValueError as j:
    print("Error:", j)
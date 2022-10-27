import math
import os
import sys

print("Welcome.")
print("Type the number of the operation you select.")
print("Math:")
print("1. Addition➕")
print("2. Subtraction➖")
print("3. Multiplication✖")
print("4. Division➗")
print("5. Area Calculator(Rectangle)")
print("6. Area Calculator(circle)")
print("7. Fahrenheit to Celsius")
print("8. Celsius to Fahrenheit")
print("9. Hypotenuse calculator")
print("10. Area Calculator (Prism)")
print("11. Kinetc Energy Calculator(fixed)")
oper = input("Enter it here: ")
if oper == "1":
    add1 = float(input("enter first number: "))
    add2 = float(input("enter second number: "))
    addsum = add1 + add2
    print(f"the sum is: {addsum}")
    if addsum == 69420.0:
        print("Stop it, get some help.")


elif oper == "2":
    sub1 = float(input("enter first number: "))
    sub2 = float(input("enter second number: "))
    subsum = sub1 - sub2
    print(f"The sum is: {subsum}")

elif oper == "3":
    mul1 = float(input("enter first number: "))
    mul2 = float(input("enter second number: "))
    mulsum = mul1 * mul2
    print(f"The sum is {mulsum}")

elif oper == "4":
    div1 = float(input("enter first number: "))
    div2 = float(input("enter second number: "))
    divsum = div1 / div2
    print(f"The sum is {divsum}")

elif oper == "5":
    l = float(input("pls enter the length "))
    w = float(input("pls enter the width "))
    area = l * w
    print(f"the area is {area}cm^2")

elif oper == "6":
    radius = float(input("Enter the radius of the circle: "))
    areac = math.pi * pow(radius, 2)
    print(f"The area of the circle is {areac}cm^2")

elif oper == "7":
    tempf = float(input("Enter the temperature in Fahrenheit: "))
    tempf = round((tempf - 32) * 5 / 9, 1)
    print(f"The temperature in Celsius is {tempf} degrees")

elif oper == "8":
    tempc = float(input("Enter The temperature in Celsius: "))
    tempc = round((9 * tempc) / 5 + 32, 1)
    print(f"The temperature in Fahrenheit is {tempc}")

elif oper == "9":
    a = float(input("Enter side A: "))
    b = float(input("Enter side B: "))
    c = math.sqrt(pow(a, 2) + pow(b, 2))
    print(f"Side C is {c}")

elif oper == "10":
    l = float(input("pls enter the length "))
    w = float(input("pls enter the width "))
    v = float(input("Enter the volume: "))
    area = l * w * v
    print(f"the area is {area}cm^2")

elif oper == "11":
    m11_string = input("Enter the object's mass in kilograms: ")
    m11 = float(m11_string)
    v11_string = input("Enter the object's speed in meters per second: ")
    v11 = float(v11_string)

    e = 0.5 * m11 * v11 * v11
    print("The object has " + str(e) + " joules of energy.")






else:
    print("Invalid operation")
    os.execl(sys.executable, sys.executable, *sys.argv)

RunAgain = input("calculate again?(y/n): ")

if RunAgain == "y":
    os.execl(sys.executable, sys.executable, *sys.argv)

elif RunAgain == "n":
    print("See you next time.")

else:
    "Invalid Input"

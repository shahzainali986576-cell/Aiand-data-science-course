# Assignment # 02: Practicing Control-Flow (Decision-Making Structures and Loops)

# 1. Check if a number is positive, negative, or zero
num = int(input("Enter a number: "))
if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")


# 2. Find the larger of two numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
if a > b:
    print("Larger number is:", a)
else:
    print("Larger number is:", b)


# 3. Find the largest of three numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
if a >= b and a >= c:
    print("Largest number is:", a)
elif b >= a and b >= c:
    print("Largest number is:", b)
else:
    print("Largest number is:", c)


# 4. Check if "Mass" is in "Saylani Mass IT"
text = "Saylani Mass IT"
if "Mass" in text:
    print("String found")
else:
    print("String not found")


# 5. Check age category (minor, adult, senior citizen)
age = int(input("Enter your age: "))
if age < 18:
    print("Minor")
elif age < 60:
    print("Adult")
else:
    print("Senior Citizen")


# 6. Check if number is even or odd
num = int(input("Enter a number: "))
if num % 2 == 0:
    print("Even")
else:
    print("Odd")


# 7. Calculator: Perform +, -, x, /
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
op = input("Enter operator (+, -, x, /): ")
if op == '+':
    print("Result:", a + b)
elif op == '-':
    print("Result:", a - b)
elif op == 'x':
    print("Result:", a * b)
elif op == '/':
    if b != 0:
        print("Result:", a / b)
    else:
        print("Cannot divide by zero")
else:
    print("Invalid operator")


# 8. Check if number is in range 20–40 (20 included, 40 excluded)
num = int(input("Enter a number: "))
if 20 <= num < 40:
    print("Number is in range")
else:
    print("Number is out of range")


# 9. Check if number is divisible by 2, 3, or both
num = int(input("Enter a number: "))
if num % 2 == 0 and num % 3 == 0:
    print("Divisible by both 2 and 3")
elif num % 2 == 0:
    print("Divisible by 2")
elif num % 3 == 0:
    print("Divisible by 3")
else:
    print("Not divisible by 2 or 3")


# 10. Check pass/fail (pass if score > 60)
score = int(input("Enter your score: "))
if score > 60:
    print("Pass")
else:
    print("Fail")


# 11. Check if number is prime
num = int(input("Enter a number: "))
is_prime = True
if num <= 1:
    is_prime = False
else:
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            is_prime = False
            break

if is_prime:
    print("Prime number")
else:
    print("Not a prime number")


# 12. Check temperature condition (freezing, moderate, hot)
temp = float(input("Enter temperature in Celsius: "))
if temp < 0:
    print("Freezing temperature")
elif temp < 26:
    print("Moderate temperature")
else:
    print("Hot temperature")

# -----------------------------
# Part-2: Loops
# -----------------------------

# 1. Print numbers from 1 to 30 using for loop
for i in range(1, 31):
    print(i)

# 2. Print even numbers from 1 to 50 using while loop
i = 2
while i <= 50:
    print(i)
    i += 2

# 3. Print multiplication table of a given number
num = int(input("Enter a number: "))
for i in range(1, 11):
    print(num, "x", i, "=", num * i)

# 4. Print odd numbers from 1 to 50 using while loop
i = 1
while i <= 50:
    print(i)
    i += 2

# 5. Sum of all numbers from 1 to 50 using for loop
total = 0
for i in range(1, 51):
    total += i
print("Sum:", total)

# 6. Print each character of a string
text = input("Enter a string: ")
for char in text:
    print(char)

# 7. Compute factorial using while loop
num = int(input("Enter a number: "))
fact = 1
while num > 0:
    fact *= num
    num -= 1
print("Factorial:", fact)

# 8. Print numbers from 10 down to 1
for i in range(10, 0, -1):
    print(i)

# 9. Ask user for password until correct one is entered
correct_password = "admin123"
password = ""
while password != correct_password:
    password = input("Enter password: ")
print("Access granted")

# 10. Print square of each number from 1 to 10 using for loop
for i in range(1, 11):
    print(i, "squared is", i * i)

# 11. Calculate and print sum of even and odd numbers (1–50)
even_sum = 0
odd_sum = 0
for i in range(1, 51):
    if i % 2 == 0:
        even_sum += i
    else:
        odd_sum += i
print("Even sum:", even_sum)
print("Odd sum:", odd_sum)

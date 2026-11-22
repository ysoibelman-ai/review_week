# Targil 1
first_name = "David"
last_name = "Cohen"
age = 225
city = "Tel Aviv"
email = "david@gmail.com"

print (f"""
===== User Details =====
First Name: {first_name}
Last Name: {last_name}
Age: {age}
City: {city}
Email: {email}
========================
""")

# Targil 2
birth_year = 2000
current_year = 2026

print (f"You are approximately {current_year-birth_year} years old")

# Targil 3
width = 10
height = 2

print (f"Shetach of the rectangle is {width*height}")
print (f"Hekef of the triangle is {width + height*2}")

# Targil 4
name = "David"
age = 25
height = 1.78
is_student = True
salary = 8500

print (f"Type of: name-{type(name)} age-{type(age)} height-{type(height)} is_student-{type(is_student)} salary-{type(salary)}")


# Targil 5
firt_name = input ("Enter first name: ")
last_name = input ("enter last name: ")
city = input ("enter city: ")
age = int(input ("Enter age: "))

print (f"welcome {first_name} {last_name} from {city}. You are {age} years old!!!")

# Targil 6
num1 = int(input("enter first numbers: "))
num2 = int(input ("Enter second number: "))

print(f"ADD = {num1+num2}, MINUS = {num1-num2}, TIMES = {num1*num2}, DEVIDE = {num1/num2}")

# Targil 7
product = input ("Enter product name: ")
price= int (input ("Enter product Price: "))
amount = int (input ("Enter product amount: "))

print (f"""
====== Purchase Receipt ======
Product: {product}
Price: {price}
Quantity: {amount}
Total: {price*amount}
==============================
""")

# Targil 9
worker_name = input ("Enter worker name: ")
work_hours_per_month = int (input("enter work hours per month: "))
hour_salary = int(input("Wnter hourly salary: "))

monthy_salary = work_hours_per_month*hour_salary

print (f"your monthly salary is {monthy_salary}")

#Targil 10

cheshbon = int(input("Enter Cheshbon amount: "))
tip = int(input("enter Tip: "))
dinning = int(input("Enter amount of people dinning: "))

print (f"Tip amount is: {tip}. Total price = {tip+cheshbon}. price per dinner{(tip+cheshbon)/dinning}")

# Targil 12
a = 10
b = 20
c = a
a =b
b=c
print (a, b)


# Mini Project

print ("please enter first name, family name, age, school, course, months in course and monthly price -> one after the other. Hit enter after every input/")
fname = input()
lname = input()
age = int(input())
school = input()
course = input()
duration = int(input())
monthly_price=float(input())

print (f"""
================================
       STUDENT REGISTRATION
================================

Student: {fname} {last_name}
Age: {age}
Institution: {school}
Course: {course}
Duration: {duration}
Monthly Price: {monthly_price}
Total Course Price: {duration*monthly_price}

=============================
Registration completed!
=============================
""")






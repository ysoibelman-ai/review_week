# #Targil 1
# num1 = 25
# num2 = 7
# print (f"{num1+num2},{num1-num2},{num1*num2},{num1/num2},{num1//num2},{num1%num2},{num1**num2}")

# #Targil 2

# balance = 1000
# print(balance)
# balance += 250
# print(balance)
# balance-= 100
# print(balance)
# balance *= 2
# print(balance)
# balance /= 4
# print(balance)

# #Targil 3
# price = float(input ("Enter price"))
# discount = float(input("enter discount perc: "))
# print (f"Discount is {price*(1-discount)}")

# # targil 4
# sum = int(input("Enter amount of money: "))
# intrest = float(input("Enter yearly intrest perc: "))
# year_interest = sum*intrest
# total_sum = sum +year_interest

# #Targil 5
# print ("Enter 3 grades one after the other: ")
# grade1= float(input())
# grade2= float(input())
# grade3= float(input())

# average_grade = (grade1+grade2+grade3)/3
# print (f"Average Grade: {average_grade}")

# #Targil 6
# first_name = "David"
# last_name = "Cohen"
# city = "Tel Aviv"

# # Targil 7
# print (f"Hello, my name is {first_name} {last_name} and I live in {city}.")
# print("Hello, my name is " + first_name +" " +last_name + "and i live in ", city)

# full_name = input ("Enter full name: ")
# print (f"Name: {full_name}")
# print (f"length: {len(full_name)}")
# print (full_name.upper())
# print(full_name.lower())

# # Targil 8
# sentence = input("Enter Sentence: ")
# print (sentence.upper(),sentence.lower(),sentence.capitalize(),sentence.title())

# Targil 9
# name = input ("Enter name: ")
# print(name, name.strip(),len(name),len(name.strip()))

# #Targil 10
# sentence = "I love Java programming"
# sentence = sentence.replace("Java","Python")
# print (sentence)
# print(sentence.count("love"))

# print(sentence.startswith("I"))
# print(sentence.endswith("programming"))

#Targil 11
# word = "Programming"
# letter=word[0]
# lletter= word[-1]
# leter3 = word[2]
# lerere = word[:3]
# asdas = word[-4:]
# leter3_ = word[-1::-1]

# Targil 12
# a = "100"
# b = "25"
# c = 10
# d = 5.5
# a = int(a)
# b = float(b)
# c = str(c)
# d = int(d)
# my_list = [a,b,c,d]
# for letter in my_list:
#     print (letter, " ",type(letter))


# question 13
# age = input("Enter your age: ")
# becuase you cannot combine int type with str type

# question 14
# price = input("enter price: ")
# price = float(price)
# vat = 0.18
# new_price = price * (1+vat)

#question 15
# print ("enter fnmae,lname,age,monthly salary,experience")
# fname = input()
# lname = input()
# age = int(input())
# salary = float(input())
# experience = int(input())

# # yearly_salary = salary*12
# # yearly_salary_plus_bonus = yearly_salary * (1.05)
# # name_length = len(fname.strip()+lname.strip())


# # Targil 16
# sum = int(input("enter sum in shekesl"))
# usd_rate = 3.25
# print (f"Sum in Dollars: {sum*usd_rate}")
# print(f'sum in Euros: {sum*3.75}')
# print (f"total sum: {sum*1.02}")

# #Targil 17
# fname = input()
# lname = input()
# birth_year = int(input())

# email = fname+"."+lname+"."+str(birth_year)+"@gmail.com"
# print (email)

# # Targil 18
# sentence = input("Eter a sentence: ")
# print (sentence)
# print (len(sentence))
# print (sentence.upper())
# print (sentence.lower())
# print (sentence[-1::-1])
# print (sentence.count("a"))
# print (sentence.replace(" ", "-"))

# Project
name = input("Enter customer name: ")
product= input(" Enter product: ").upper()
price = float(input("Enter product price: "))
quantity = int(input("Enter product quantity: "))
discount = float(input("Enter discount: "))
vat = float(input("Enter Vat Amount: "))

print (f"""
================================
          PURCHASE INVOICE
================================

Customer: {name}
Product: {product}

Unit Price: {price}
Quantity: {quantity}

Subtotal: {price*quantity}
Discount: {discount}
After Discount: {price*quantity -discount}

VAT: {vat}%
VAT Amount: {vat/100*(price*quantity -discount)}

TOTAL: {vat/100*(price*quantity -discount) +price*quantity -discount }


================================
       THANK YOU FOR SHOPPING
================================


""")

#1
age = int(input("Enter age"))
if age >= 18:
    print ("Adult")
else:
    print ("Minor")
#2
num = int(input("Enter num: "))
if num > 0:
    print ("Larger than 0")
if num == 0:
    print ("num equals 0")
if num <0:
    print ("negative number")


#3
num = int(input())
if num % 2 ==0:
    print ("Even number")
else:
    print ("odd number")


#4
num1 = int(input())
num2 = int(input())
if num1==num2:
    print ("Numbers are eual")
else:
    print (f"the largest number is {max(num1,num2)}")

# 5
password = "Python123"
password_ = input("Enter password")
if password == password_:
    print ("Access Granted")
else:
    print ("Access denied")
# 6
num = int(input("enter Num"))
if 1<=num <=10:
    print ("group 1")
elif 11<=num<=50:
    print ("group 2")
elif 51<=num<=100:
    print ("gourp 3")
else:
    print ("out of range")


#7
grade = int(input("enter grade: "))
if 90<= grade <=100:
    print ("Excellent")
elif 80<= grade <=89:
    print ("very good")
elif 70<=grade <=79:
    print ("Good")
elif 60<=grade <= 69:
    print ("passed")
else:
    print ("Failed")
#8
username = input("Enter user name")
password = input ("enter password")
correct_username = "admin"
correct_password = "123456"
if username == correct_username and password == correct_password:
    print ("Login successful")
if password != correct_password:
    print ("Incorrect password")
if username != correct_username:
    print ("Incorrect username")




#9
age = int(input("Enter age: "))
price = int(input("Enter price of product"))

if age >60:
    price = price*0.8
elif age < 18:
    price = price*0.9


# 10
num = int(input("Enter num: "))
if num % 3 ==0 and num % 5 ==0:
    print ("divides by 3 and 5")

elif num % 3 == 0:
    print ("Divides by 3")
elif num % 5==0:
    print ("Divides by 5")
else:
    print ("doesnt divide by 5 or 3")

# 11
age = int(input("Enter age: "))
has_guide = input("1/0")
if has_guide == "1":
    has_guide = True
else:
    has_guide = False

if age >18 or has_guide:
    print ("You can enter")
else:
    print ("You cannot enter")

# 12
Memo_tzion = int(input("Enter your avg grade"))
monthly_salary = int(input("enter your monthly salary"))
if Memo_tzion > 90 or (Memo_tzion >85 and monthly_salary<5000):
    print ("you can get the scholarship")
# 13
password = "123456"
uesername = "654321"
user_username = input("Enter username")
user_password = input("Enter password")
is_active = input ("enter 1 if active 0 if not active")

if password == user_password and user_username == uesername and is_active ==1:
    print ("Allowed to enter")
else:
    print ("Denied entrance")

#14
num = int(input("enter number"))
if 20<= num <=80:
    print ("yes")
if not (num > 80) and not ( num <20):
    print ("Yes")
#15
balance = 5000
withdraw = int(input("Ener amount to withdraw: "))
if withdraw>0:
    if withdraw<=balance:
        balance-=withdraw
    else:
        print (f"Not enough if balance to withdraw {withdraw}")
else:
    print ("must withdraw a positive number")



# 16
age = int(input("Enter Age: "))
is_member = int(input(" Are you a member: 1-yes 0 -no"))
if age <12:
    price = 25
elif age <18:
    price = 35
else:
    price = 50
    
if is_member ==1:
    price*=0.9
    

# 17
eligible = True
age = int(input("Enter age: "))
if age <21:
    eligible = False
    print ("Too young")
salary = int(input("Enter salary: "))
if salary < 7000:
    eligible = False
    print ("Salary not high enough")
experience_in_years = int(input("Enter experience: "))
if experience_in_years < 1:
    eligible = False
    print ("Not enough experince")
if eligible:
    print ("you are eligible")
else:
    print ("You are not eligible")

# 18

vehicle_type = int(input ("enter chichcle type 1=motorcycle 2=private vehicle 3= commercial car"))
hours = int(input(""))

if vehicle_type ==1:
    price = 10
if vehicle_type ==2:
    price = 20
if vehicle_type == 3:
    price = 30

if hours <=1:
    price = price*0.9
elif hours> 5:
    price = price *0.85


#19
num1 = int(input())
num2 = int(input())
operator = input()

if operator =="+":
    print (num1+num2)
elif operator == "-":
    print (num1-num2)
elif operator =="*":
    print (num1*num2)
else:
    if num2!= 0:
        print (num1/num2)


#20
year = int(input("Enter year: "))
if year %400 ==0:
    print ("Meuberet")
elif year %4 ==0 and year%100 != 0:
    print (print *"Meuberet")
else:
    print ("not meuberet")

# 21
base_salary = 50
extra_salary =50*1.25
exrta_extra_salary = 50*1.5
hours = int(input("Enter months worked: "))

if hours <= 182:
    salary = hours * base_salary
else:
    first_salary = 182 * base_salary
    hours -= 182
    if hours <=2:
        first_salary += hours*extra_salary
    else:
        first_salary += 2*extra_salary
        hours -=2
        first_salary += hours * exrta_extra_salary


#project
age = int(input("Enter age: "))
sum = int(input("Enter sum of purchase: "))
member = int(input("are you a member: 1/0"))
opened = int(input("was the product opened? 1/0" ))
recipt = int(input("Fo you have a recipt?  1/0"))
days_post_purchase = int(input("enter the amount of days that passed since the purchase: "))


if recipt ==1 and opened == 0 and sum >0:
    if member ==1:
        print ("You are eligible for a return")
    elif days_post_purchase <14:
        print ("Too many days passed from purchase")
        print("no eligble for return")
elif recipt !=1:
    print ("Need a recipt")
elif opened ==1:
    print ("Package already opened")
elif sum <=0:
    print ("Sum is too smalll")
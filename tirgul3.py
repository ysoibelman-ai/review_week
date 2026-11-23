# Trargil 1
num = 1
while num <=10:
    print (num)
    num +=1

# Targil 2
num = 10
while num >=1:
    print (num)
    num -=1
print ('START')

# Targil 3
num = 1
while num <=50:
    if num%2 ==0:
        print (num)
    num +=1

# Targil 4
num = int(input("Enter number: "))
times = 1
while times <=5:
    print (times*num)

# Targil 5
sum = 0
num = 1 
while num <=100:
    sum+=num
    num +=1
print (sum)

# Targil 6
password = ""
while password != "Python123":
    password = input("Enter password")
print ("Welcome!")

# Targil 7
secret_number = 27
sum =0
while guess != secret_number:
    guess = int(input("Guess number: "))
    sum+=guess
print (sum)

#Targil 8
num = None
sum=0
while num !=0:
    num = int(input())
    sum+=num
print (sum)

#targil 9

grade_count = 0
sum_grades = 0
grade = 0
while grade != 999:
    grade= int(input())
    if grade != 999:
        grade_count +=1
        sum_grades +=grade

print (grade_count, sum_grades, sum_grades/grade_count )

#Targil 10:
num =0
sum = 0
count = 0
while num >=0:
    num = int(input("Enter a numebr: "))
    count +=1
    if num >=0:
        sum+=num
print (f"Sum of positive nums: {sum}. count of nums: {count}")

# #Targil 11
num = int(input("Enter a number: "))
counter = 1
while counter <=10:
    sum = num*counter
    print (f"{num} X {counter} = {sum}")
    counter +=1

# # Targil 12
num = int(input("Enter a number: "))
digits = 0
while num > 0:
    num = num // 10
    digits +=1
print (digits)

# targil 13
num = int(input("Enter a number: "))
my_num = 0
while num > 0:
    my_num = my_num*10 + num%10
    num = num // 10
print (my_num)


# # targil 14
num = int(input("Enter a number"))
divider = 2
if num == 1:
    print ("Its not a rishoni")
else:
    while divider <num:
        if num % divider == 0:
            print ("Is not a Rishoni")
            break
    print ("Is a Rishoni")


# # Targil 15
balace = 5000
enter = 0
while enter != "4":
    enter = input("Enter number")
    if enter =="1":
        print (balace)
    elif enter == "2":
        balance +=  int(input("Enter more amount: "))
    elif enter == "3":
        draw = int(input("Enter draw amount: "))
        if draw<= balance:
            balance -=  int(input("Enter more amount: "))
        else:
            print ("Cannot draw out that amount")
    elif enter == "4":
        break

# # tirgul 16
num = 1
while True:
    if num == 15:
        break
    print (num)
    num +=1

# Tirgul 17
num = 0
while num <=29:
    num +=1
    if num %3 ==0:
        continue
    else:
        print (num)

# tirgul 18
while True:
    num = int (input ("enter number"))
    if num ==0:
        print ("Number is 100")
        break

#Targil 19
for i in range (1,21):
    print (i)

#Targil 20
for i in range (0,101,5):
    print(i)

#Targil 21
sum =0
for i in range (1,100):
    sum += i

#Targil 22
num = int(input("Enter number"))
for i in range (1,10):
    print (num*i)
       
   # targil 23 
num1 = int(input())
num2 = int(input())
sum = 0
for num in range(num1,num2+1):
    sum += num
print(sum)
# targil 24
for num in range (1,100):
    if num % 3 ==0 and num % 5 ==0:
        print (num)

#targil 25
row = int(input())
column = int(input())
for i in range(row):
    for j in range(column):
        print ("*",end="")
    print

#Targil 26
for i in range(7):
    for j in range (i):
        print ("*",end="")
    print()

# targil 27
for i in range (0,100,10):
    for j in range (1,11):
        print (i+j,end = " ")
    print()

# targil 28
choice = 9
while choice != 3:
    print("""
===== MATH GAME =====

1. Start Game
2. View Instructions
3. Exit

Choose:
    """)

    if choice == "1":
        score = 0
        for i in range (10):
            question = int(input (f"1 + {i} =? "))
            if question == i+1:
                    score +=1
        print (f"Final Score: {score}")

    elif choice == "2":
         print ("""
=============
INSTRUCTIONS
============
if you enter 1:
you will be asked 10 questions. 
answer each one. at the end you will be shown your score.
""")
    if choice == "3":
              exit()
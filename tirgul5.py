# # #q1
# # numbers = [10,20,30,40,50]
# # print (numbers)
# # print(numbers[0])
# # print(numbers[-1])
# # print(numbers[2])

# # #q2
# # students =["yaakov","ephraim"]
# # print (len(students))
# # print (students[0],students[-1])
# # students[1] = "jo"
# # print (students)

# # #q3
# # grades = [10,20,30,40,50]
# # grades.append(60)
# # grades.insert(0,70)
# # grades[2] = 90
# # print (grades)

# #q4
# numbers = [10,20,30,40,50,1,2,3,4,5]
# print (numbers)
# numbers.pop(0)
# print (numbers)
# numbers.pop(-1)
# print (numbers)
# numbers.pop(2);print (numbers)

# #q5
# products = ["books","pencils","papers"]
# if "books" in products:
#     print ("in")
# if "glasses" not in products:
#     print ("not in")

# #q6
# numbers = [10,20,30,40,50,1,2,3,4,5]
# for num in numbers:
#     print (num)

# #q7
# numbers = [10,20,30,40,50,1,2,3,4,5]
# for num in numbers:
#     if num %2 == 0:
#         print (num)

# #q8
# sum = 0
# grades = [10,20,30,40,50,1,2,3,4,5]
# for grade in grades:
#     sum+=grade
# print (sum)

# #q9
# max = float('-inf')
# grades = [10,20,30,40,50,1,2,3,4,5]
# for grade in grades:
#     if grade > max:
#         max = grade
# # print (max)

# # #q10
# # names  =["yaakov","ephraim"]
# # name = input("Enter name: ")
# # if name in names:
# #     print ("In the list")
# # else:
# #     print ("not in the list")

# #q11
# numbers = [10,20,33,40,50,1,2,3,4,5]
# indexes =[]
# num = int(input("enter number"))
# for key, value in enumerate(numbers):
#     if value == num:
#         indexes.append(key)

# #q12
# numbers = [10,20,33,40,50,1,2,3,4,5]
# larger_than_50 = 0
# for num in numbers:
#     if num > 50:
#         larger_than_50 +=1


#question 13
# numbers = [10,20,33,40,50,1,2,3,4,5]
# new_list = []
# for num in numbers:
#     if num %2 == 0:
#         new_list.append(num)
# print (new_list)

# #question 14
# names =["yaakov","ephraim"]
# index = 0
# while len(names) > 0:
#     print (index,names[0])
#     index+=1
#     names.pop(0)

# question 15
# numbers = [10,20,33,40,50,1,2,3,4,5]
# print (numbers[0:4])
# print (numbers[-3:])
# print (numbers[2:7])
# print (numbers[::-1])

#question 16
# names = ["yaakov","ephraim","jo","shmo","michael","oriel","meir","finished"]
# # for i in range (len(names)):
# #     if i %2 ==0:
# #         print (names[i])

# # for i in range (len(names)):
# #     if i%2 != 0:
# #         print (names[i])

# # for name in names[::-2]:
# #     print (name)

# #question 17
# numbers = [10,20,33,40,50,1,2,3,4,5,10,20,33,40,50,1,2,3,4,5]
# new_numbers = numbers[0:10]
# new_numbers2 = numbers[10:]
# new_numbers3 = numbers[5:14]

# print (numbers,"\n",new_numbers,"\n",new_numbers2,"\n",new_numbers3)


# # question 18
# numbers = [10,20,33,40,50,1,2,3,4,5,10,20,33,40,50,1,2,3,4,5]
# first_half = numbers[:len(numbers)/2]
# second_half = numbers[len(numbers)/2:]

# # question 19
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# new_numbers = [num*2 for num in numbers]
# new_numbers = [num**2 for num in numbers]
# new_numbers = [num for num in numbers if num%2 ==0]
# new_numbers = [num*2 for num in numbers if num >5]

# #question 20
# grades = [55, 90, 67, 100, 45, 82, 73, 30]
# passing_grades = [grade for grade in grades if grade > 60]
# plus_five = [grade +5 for grade in grades]

#question 21
names = ["Moshe", "David", "Dana", "Noa", "Michael", "Avi"]
# long_names = [name for name in names if len(name) >4]
# upper_name = [name.upper() for name in names]
# # start_d = [name for name in names if name.startswith("D")]

# # # question 22
# # numbers = [12, 7, 25, 30, 9, 44, 18, 3]
# # new_list = [num for num in numbers if num %3==0 and num >10]

# # question 23
# list_ = []
# for i in range (10):
#     list_.append(int(input()))
# print (list_)
# max_num = float("-inf")
# min_num = float("inf")
# sum = 0
# for num in list_:
#     if num > max_num:
#         max_num = num
#     if num < min_num:
#         min_num = num
#     sum+=num
# print (min_num,max_num)
# avg = sum / len(list_)

# # question 24
# users = ["yaakov","ephraim","jack","sussi","Gad"]
# user = input ("enter user name: ")
# if user in users:
#     users.remove(user)
# else:
#     print ("user not in list")

# print (users)

# # question 25
# numbers = [12, 7, 25, 30, 9, 44, 18, 3,4,5]
# even_numbers = [num for num in numbers if num % 2 ==0]
# odd_numbers = [num for num in numbers if num % 2 !=0]
# large_nums = [num for num in numbers if num>20]

# question 26
numbers = [12, 7, 25, 30, 9, 44, 18, 3,4,5]
search_num  = int(input ("enter a number to search"))
num_indexes = [key for key,value in enumerate(numbers) if value == search_num]
if not num_indexes:
    print ("this numbers is not in the list")
print (num_indexes,len(num_indexes))

# question 27
numbers = [12, 7, 25, 30, 9, 44, 18, 3,4,5]
numbers2 = [12, 7, 25, 30, 9, 44, 18, 3,4,5]
numbers3 = numbers+numbers2
print (numbers3)
print (numbers3[:6])
print(numbers3[-5:])
print (numbers3[::-1])

# question 28
numbers = [12, 7, 25, 30, 9, 44, 18, 3,4,5]
num = int(input ("enter number: "))
found = False
for nums in numbers:
    if nums == num:
        found = True
        break
if found == False:
    numbers.append(num)
print (numbers)

#project

grades = [85, 72, 90, 55, 100, 63, 48, 77]

print ("""

===== Grades Management =====

1. Show all grades
2. Add a grade
3. Search for a grade
4. Remove a grade
5. Show passing grades
6. Show failing grades
7. Show highest and lowest grade
8. Show average grade
9. Show first 3 grades
10. Show grades in reverse
0. Exit
""")

choice = input ("Enter Menu selection: ")

if choice == "1":
    for num in grades:
        print (num)
elif choice == "2":
    grade = int(input("Enter grade: "))
    grades.append(grade)

elif choice == "3":
    grade = int(input("Enter Grade"))
    in_grades = False
    for grade_ in grades:
        if grade_ == grade:
            print (" grade in grades")
            break
elif choice == "4":
    pass
    
##################################################

# Display float number with 2 decimal places using

num = 458.54362

print(round(num, 2))

##########################################################

# Accept a list of 5 float numbers as an input from
# the user

input_string = input("Enter elements of a list seperated by space: ")
#print('\n')

user_list = input_string.split()
print('List: ', user_list)

for i in range(len(user_list)):
    user_list[i] = int(user_list[i])

print("sum =", sum(user_list))

#####################################

numbers = []

for i in range(0, 5):
    inputted = input("Enter elements of a list seperated by space: ")
    newlist = float(inputted)
    numbers.append(newlist)

print(numbers)

##########################################

# Write a program to take three names as input from a user in
# the single input() function call.

name1, name2, name3 = input("Enter thee string Emma Jessa Kelly: ").split()
print("Name 1: ", name1)
print("Name 2: ", name2)
print("Name 3: ", name3)

############################################

# Write a program to use string.format() method to format the
# following three variables as per the expected output

totalMoney = 1000
quantity = 3
price = 450
expectedOutput = "I have {2:2f} dollars so i can buy {0} football for {1} dollars"

print(expectedOutput.format(quantity, price, totalMoney))


##################################################################

# Write a program to create a function that takes two arguments
# , name and age, and print their value.

def callFunction(name, age):
    print("My name is ", name, "and i am ", age)

callFunction("Ayo", 32)

#################################################################

# Write a program to create function func1() to accept a variable
# length of arguments and print their value.

def funt1(*figures):
    for name in figures:
        print(name)

funt1(20, 40, 60)
funt1(80, 100)


###########################################################

# Write a program to create function calculation() such that it
# can accept two variables and calculate addition and subtraction.
# Also, it must return both addition and subtraction in a single
# return call.

def calculations(a, b):
    add = a + b
    sub = a - b

    return add, sub

print(calculations(40, 10))


#####################################################################


# Create a function with a default argument

def show_employee(name, salary = 9000):
    print("Name: ", name, "Salary", salary)

show_employee("Ben", 12000)
show_employee("Jessa")


#########################################################################

# Write a program to create a recursive function to calculate
# the sum of numbers from 0 to 10.

def addition(num):
    if num:
        return num + addition(num - 1)
    else:
        return 0

res = addition(10)
print(res)


########################################################


def display_student(name, age):
    print(name, age)


display_student

show_student = display_student


show_student("Emma", 26)


##################################################


# Generate a Python list of all the even numbers between 4 to 30

for i in range(4, 30):
    if i % 2 == 0:

        print(i, end=' ')

##################################################################


# Find the largest item from a given list

x = [4, 6, 8, 24, 12, 2]
print(max(x))


#######################################################

values = 2, 3, 5, 6

print(list(values))
print(tuple(values))

################################################################


# remove first and last element

color_list = ["Red", "Green", "White", "Black"]
color_list.pop(0)
color_list.remove("Black")
print(color_list)

##################################################################


# Write a Python program that accepts an
# integer (n) and computes the value of n+nn+nnn.

n = input("enter number: ")
temp = str(n)
t1 = temp + temp
t2 = temp + temp + temp
comp = int(n) + int(t1) + int(t2)
print(comp)


############################################################


# Write a Python program to calculate the sum of three given
# numbers. If the values are equal, return three times
# their sum.

def sum_thrice(x, y, z):

    sum = x + y + z
    if x == y == z:
        sum = sum * 3
    return sum

print(sum_thrice(1,2,3))
print(sum_thrice(3,3,3))


###########################################################################

# Write a Python program to get a newly-generated string from
# a given string where "Is" has been added to the front.
# Return the string unchanged if the given string already begins
# with "Is".

def new_string(text):
    if len(text) >= 2 and text [:2] == "Is":
        return text
    return "Is" + text

print(new_string("Array"))
print(new_string("IsEmpty"))


#########################################################


# Write a Python program that returns a string that is n
#  copies of a given string.

def larger_string(text, n):
    result = " "
    for i in range(n):
        result = result + text

    return result

print(larger_string('abc', 3))


######################################################################

# Write a Python program that determines whether a given number
# (accepted from the user) is even or odd, and prints an appropriate
# message to the user.

num = int(input("Enter any number: "))

if num % 2 == 0:
    print("This is an even number")

else:
    print("Ths is an odd number")


##################################################################

# Write a Python program to count the number 4 in a given list.

n = [2, 4, 5, 6, 7, 8, 9, 0, 4]
count = n.count(4)
print(count)

#################################################################




# Write a Python program to get n copies of the first 2 characters of a given
# string. Return n copies of the whole string if the length is
# less than 2.

def numOfCopies(text, n):
    flen = 2
    if flen > len(text):
        flen = len(text)

    substr = text[:flen]
    result = " "

    for i in range(n):
        result = result + substr
    return result

print(numOfCopies('abcd', 2))
print(numOfCopies("p", 3))

##################################################################
# Write a Python program to get n copies of the first 2 characters of a given
# # string. Return n copies of the whole string if the length is
# # less than 2.

def Numof(s, n):
    s = "house"
    firsttwo = s[:2]
    print(firsttwo)

    numberoftimes = firsttwo * n
    return numberoftimes

print(Numof("house", 4))


########################################################################

# Write a Python program to test whether a passed letter
# is a vowel or not.
def checkvowel(userInput):
#userInput = input("Enter a letter to check if it is a vowel: ")


    vowels = 'aeiou'

    for user in userInput:
        if userInput in vowels:
            print(True)
        else:
            print(False)
print(checkvowel("y"))

#################################################################

# # Write a Python program to test whether a passed letter
# # is a vowel or not.

def is_vowel(char):
    all_vowels = 'aeiou'
    return char in all_vowels

print(is_vowel('c'))
print(is_vowel("w"))


###########################################################

# Write a Python program that checks whether a specified value is
# contained within a group of values.
n = 9

group_Values = [1,5,3,4,8]

if n in group_Values:
    print(True)
else:
    print(False)

################################################################

# Write a Python program to print all even numbers from a given
# list of numbers in the same order and stop printing any after
# 237 in the sequence.

numbers = [
    386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345,
    399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217,
    815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717,
    958,743, 527
    ]

for i in numbers:
    if i == 237:
        print(i)
        break
    elif i % 2 == 0:
        print(i)

###############################################################





















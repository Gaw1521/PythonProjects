'''
Lab Set 2
Simple Functions
Gregory White - J00527454
'''


# Script 1
print("\n # Script Number 1")
def max(num1, num2):

    if (num1 >= num2):
        largest = num1
    elif (num2 > num1):
        largest = num2

    return largest

# Given Numbers
num1 = 100
num2 = 500
print("The largest number is: ", max(num1, num2))


# Script 2
print("\n # Script Number 2")
def max_of_three(num1, num2, num3):

    if (num1 > num2) and (num1 > num3):
        largest = num1
    elif (num2 > num1) and (num2 > num3):
        largest = num2
    elif (num3 > num1) and (num3 > num2):
        largest = num3
    else:
        largest = num1 #all numbers are the same

    return largest

# Given Numbers
num1 = 100
num2 = 500
num3 = 1000
print("The largest number is: ", max_of_three(num1, num2, num3))


# Script 3
print("\n # Script Number 3")
def find_len(string):
    counter = 0
    for i in string:
        counter += 1
    return counter

# Given Input
string = "Gregory White"
print("The length of the string is: ", find_len(string))


# Script 4
print("\n # Script Number 4")
def multiply_list(myList):  # first function in Script number 4 (multiply function)

    result = 1
    for i in myList:
        result = result * i
    return result

# Given Input
list = [1, 2, 3, 4]
print("The product of all the numbers within the list is:", multiply_list(list))


list = [1, 2, 3, 4] # creating the list


def sum(list, size):  # second function in Script number 4 (Sum function)
    if (size == 0):
        return 0
    else:
        return list[size - 1] + sum(list, size - 1)

total = sum(list, len(list))

print ("The sum of all the elements in the given list is: ", total)


# Script Number 5
print("\n # Script Number 5")
def reverse(string):
    str = ""
    for i in string:
        str = i + str
    return str

string = "I am testing."

print("The reversed string is : ", end="")  # Appends a space instead of a newline
print(reverse(string))


# Script Number 6
print("\n # Script Number 6")
def is_vowel(x):
    trueVowels = 'aeiou'
    return x in trueVowels


print(is_vowel('o'))  # Chosen character to test against is_vowel


# Script Number 7
print("\n # Script Number 7")

def is_member(x, a):
    for i in range(len(a)):
        if x == a[i]:
            return True
        else:
            return False

a = ['apple', 'watermelon', 'kiwi']

x = "orange"

print(x + " is a member of ")
print(a)

if is_member(x,a) == True:
    print("True")
else:
    print("False")


# Script Number 8
print("\n Script Number 8")

def overlapping(list1, list2):
    for i in range(len(list1)):
        for j in range(len(list2)):
            if list1[i] == list2[j]:
                return True


list1 = ["LeBron James", "Michael Jordan", "Steve Nash"]
list2 = ["James Jones", "Steve Nash", "Larry Bird"]

print("List 1:")
print(list1)
print("List 2:")
print(list2)
print("Are there any matching values:")
if overlapping(list1,list2) == True:
    print("True")
else:
    print("False")


# Script Number 9
print("\n Script Number 9")


def translate(word):
    rövarspråket = ""
    for c in word:
        if c in ['a', 'e', 'i', 'o', 'u', ' ', '', ',']:
            rövarspråket += c
        else:
            rövarspråket = rövarspråket + c + "o" + c

    return rövarspråket


sentence = "This is fun"
print("the original sentence is: " + sentence)
print("The word/sentence translated is: " + translate(sentence))











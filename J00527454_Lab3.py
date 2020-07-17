'''
Lab Set 3
Intermediate Functions
Gregory White - J00527454
'''

# Script 1
print("\n # Script Number 1")

def generate_n_chars(i,c):
    counter = 0
    answer = ""
    while counter < i:
        counter += 1
        answer += c
    print(answer)
i = int(input("Please enter an integer: "))
c = input("Please enter a character: ")
generate_n_chars(i,c)


# Script 2
print("\n # Script Number 2")

def max_in_list(list):
    max = 0
    for i in range(0,len(list)):
        if list[i] > max:
            max = list[i]
    return max
list = []
counter = 0
while counter < 3:
    counter += 1
    x = int(input("Please enter an integer: "))
    list.append(x)
print("The largest number is ", max_in_list(list))


# Script 3
print("\n # Script Number 3")

def find_longest_word(list):
    list2 = []
    for i in range(0, len(list)):
        list2.append(len(list[i]))
    max = 0
    index = 0
    for i in range(0,len(list)):
        if list2[i] > max:
            max = list2[i]
            index = i
    return list[index]

list = []
counter = 0
while counter < 3:
    counter += 1
    x = input("Please enter a word: ")
    list.append(x)
print("the longest word entered is: ")
print(find_longest_word(list))


# Script 4
print("\n # Script Number 4")


def filter_long_words(x, n):
    list = []
    split = x.split(",")

    for i in split:
        if len(i) > n:
            list.append(i)
    return list


x = input("Enter words (separated by commas):")

n = int(input("Enter a number: "))

longerList = filter_long_words(x, n)

print("Words entered longer than ", end="")
print(n, end="")
print(":")
for i in longerList:
    print(i, end=" ")


# Script 5
print("\n # Script Number 5")
import string

def ispangram(str):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for char in alphabet:
        if char not in str.lower():
            return False
    return True


string = input("Enter a string to check for pangram: ")

if ispangram(string):
    print("Yes, the string is a pangram")
else:
    print("No, the string is not a pangram")


# Script 6
print("\n # Script Number 6")


def bottles(start, end):
    for j in (range(start, end, -1)):
        print(j, "bottles of beer on the wall,", j, "bottles of beer.\nTake one down, pass it around,", j-1, "bottles of beer on the wall.\n")


bottles(99, 0)

# Script 7
print("\n # Script Number 7")


def char_freq(inputString):
    dictionary = {}
    keyword = ""

    print(inputString)

    for i in range(len(inputString)):

        if inputString[i] in dictionary:
            dictionary[inputString[i]] = int(dictionary.get(inputString[i]))+1
        else:
            dictionary[inputString[i]] = 1

    return dictionary


myString = input("Enter a string: ")
print("Letter frequencies for that string: ")
print(str(char_freq(myString)))








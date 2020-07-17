'''
Lab Set 5
Intermediate Functions
Gregory White - J00527454
'''


# Script 1
print("\n # Script Number 1")

# Created Dictionary
dict = {'a':'alfa', 'b':'bravo', 'c':'charlie', 'd':'delta', 'e':'echo', 'f':'foxtrot',
     'g':'golf', 'h':'hotel', 'i':'india', 'j':'juliett', 'k':'kilo', 'l':'lima',
     'm':'mike', 'n':'november', 'o':'oscar', 'p':'papa', 'q':'quebec', 'r':'romeo',
     's':'sierra', 't':'tango', 'u':'uniform', 'v':'victor', 'w':'whiskey',
     'x':'x-ray', 'y':'yankee', 'z':'zulu'}


def printICAO(string):
    wordlist = string.split(" ")

    for word in wordlist:
        # print word
        print(word, "-->", sep=" ", end=" ")
        # print the looked up value and dash for each one -- no dash on the end
        wordlen = len(word)
        count = 0
        word = word.lower()
        for x in word:
            count += 1
            if x in dict:
                print(dict[x], sep="", end="")
                if count < wordlen:
                    print("-", sep="", end="")
            else:
                print(x)
        print()


string = input("Please, provide a list of words: ")
printICAO(string)


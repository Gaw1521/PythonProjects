'''
Lab Set 3
Intermediate Functions
Gregory White - J00527454
'''
import sys

# Script 1
print("\n # Script Number 1")

import re


# Created Dictionary
dictionary = {"merry" : "god",
              "christmas" : "jul",
              "and" : "och",
              "happy" : "gott",
              "new" : "nytt",
              "year" : "år"}


def translate(inputString):

    translatedString = ""

    for i in inputString.split(" "):

        if (str(dictionary.get(i))) != "None":
            translatedString = translatedString+str(dictionary.get(i))+" "
        else:
            translatedString = ""
            return translatedString
    return translatedString


inputString = "merry christmas and happy new year"
print("The starting string to be translated:", inputString, sep=" ")
if (translate(inputString)) == "":
    print("The sentence can not be translated")
else:
    print("Translated string: ", end="");
    print(str(translate(inputString)))


# Script 2
print("\n # Script Number 2")

# Program to illustrate Ceasar Cipher Tecnique
def encrypt(text,s):
    result = ""  # the string we are building

    # transverse text
    for i in range(len(text)):
        char = text[i]
        newchar = char
        inewchar = ord(char)

        if char.isupper():
            bUpper = True
        else:
            bUpper = False

        # Encrypt uppercase characters
        newchar = newchar.lower()
        inewchar = ord(newchar)

        if (ord(newchar) < 97) | (ord(newchar) > 122):
            result += char
        else:
            inewchar = ord(newchar) - 97
            inewchar = inewchar + s
            if (inewchar > 26):
                inewchar = (inewchar - 26)

            newchar = chr(inewchar + 97)

            if (bUpper == True):
                result += newchar.upper()
            else:
                result += newchar

    return result


def decrypt(text,s):
    result = ""  # the string we are building

    # transverse text
    for i in range(len(text)):
        char = text[i]
        newchar = char
        inewchar = ord(char)

        if char.isupper():
            bUpper = True
        else:
            bUpper = False

        # Encrypt uppercase characters
        newchar = newchar.lower()
        inewchar = ord(newchar)

        if(ord(newchar) < 97) | (ord(newchar)> 122):
            result += char
        else:
            inewchar = ord(newchar) - 97
            inewchar = inewchar - s
            if (inewchar < 0):
                inewchar = 26 + inewchar

            newchar = chr(inewchar + 97)

            if (bUpper == True):
                result += newchar.upper()
            else:
                result += newchar

    return result


text = "Pnrfne pvcure? V zhpu cersre Pnrfne fnynq!"
s = 13

print("Script #2")
print("Starting Text  :  " + text)
print("Shift : " + str(s))
print("Decrypt: " + decrypt(text, s))

text = "Caesar cipher? I much prefer Caesar salad!"
print("Encrypt: " + encrypt(text, s))


print("Script #4")

infile = ""
outfile = ""
bdecrypt = False

if len(sys.argv) > 0:
    if "-i" in sys.argv:
        infile = sys.argv[sys.argv.index("-i") + 1]
    if "-o" in sys.argv:
        outfile = sys.argv[sys.argv.index("-o") + 1]

    if "-d" in sys.argv:
        print("decrypted file:", infile, "to", outfile, sep=" ")
        bdecrypt = True

    if "-e" in sys.argv:
        print("encrypted file:", infile, "to", outfile, sep=" ")

with open(infile, 'r') as reader:
    with open(outfile, 'w') as writer:
        # Read and print the entire file line by line
        line = reader.readline()
        while line != '':  # The EOF char is an empty string
            if bdecrypt:
                writer.write(decrypt(line, s))
            else:
                writer.write(encrypt(line, s))

            line = reader.readline()
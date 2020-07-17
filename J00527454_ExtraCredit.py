'''
Lab Set 3
Intermediate Functions
Gregory White - J00527454
'''
import sys


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
            if (inewchar > 25):
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

        if(ord(newchar) < 97) | (ord(newchar) > 122):
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


s = 13

print("Script to use Ceasar Cipher with added command line option:")

infile = ""
outfile = ""
bdecrypt = False

# testing commandline parameters
# -i abc.txt -o decryptAbc.txt -r 13 -d
# -i decryptAbc.txt -o encryptAbc9.txt -r 9 -e
# -i encryptAbc9.txt -o decryptAbc9.txt -r 9 -d

if len(sys.argv) > 0:
    if "-i" in sys.argv:
        infile = sys.argv[sys.argv.index("-i") + 1]
    if "-o" in sys.argv:
        outfile = sys.argv[sys.argv.index("-o") + 1]

    if "-r" in sys.argv:
        s = int(sys.argv[sys.argv.index("-r") + 1])

    if "-d" in sys.argv:
        print("decrypted file:", infile, "to", outfile, "using rotate by", s, sep=" ")
        bdecrypt = True

    if "-e" in sys.argv:
        print("encrypted file:", infile, "to", outfile, "using rotate by", s, sep=" ")

if (len(infile) > 0):
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

from random import randint, seed

def convertHexToDec(hexSubString):
    return chr(int(hexSubString, 16))

message = (input("Enter the encrypted message:"))
variable1= ""
outString = ""
for i in range(0, len(message), 2):
    subStr = message[i] + message[i+1]
    outString += convertHexToDec(subStr)

n= int(input("Enter the seed:"))
seed(n)
for i in outString:
    key= randint(1,10)
    asc = ord(i)
    xor = asc ^ key
    decrypt= chr(xor)
    variable1 += decrypt
print("After decrypting:",variable1)


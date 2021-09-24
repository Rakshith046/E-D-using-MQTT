from random import randint, seed

message= input("Enter the text:")
variable = ""
variable1 = ""
#FOR ENCRYPTION:
s=int(input("Set the SEED:"))
seed(s)
for i in message:
    key= randint(1,10)
    print(key,end=" ")
    asc_val= ord(i)
    xor_= asc_val ^ key
    encrypted =chr(xor_)
    variable += encrypted
print()
print("After Encrypting:",variable, end="")
print()

#FOR DECRYPTION:
n= int(input("To Decrypt enter the seed:"))
seed(n)
for i in variable:
    key= randint(1,10)
    print(key,end=" ")
    asc = ord(i)
    xor = asc ^ key
    decrypt= chr(xor)
    variable1 += decrypt
print()
print("After Decrypting:",variable1, end="")
print()

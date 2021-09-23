# 🔒 Encrption and Decryption using MQTT
### About the project:
■ Encryption is the process through which data is encoded so that it remains hidden from or inaccessible to unauthorized users and Decryption is a process of converting encoded/encrypted data in a form that is readable and understood by a human or a computer.
<br>

■ This Encryption and Decryption is carried out through MQTT server in this project.
<br>

■ MQTT is a publish-and-subscribe protocol, meaning that instead of communicating with a server, client devices and applications publish and subscribe to topics handled by a broker.

## Code for Encryption and Decryption using Python:
   
   ### In the file project.py:
   ``` python
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
    binary= bin(xor_)[2:].zfill(8)
    encrypted =chr(xor_)
    variable += encrypted
    #print(binary, end=" ")  
print()
print("After Encrypting:",variable, end="")
print()

#FOR DECRYPTION:
n= int(input("Enter the seed:"))
seed(n)
for i in variable:
    key= randint(1,10)
    print(key,end=" ")
    asc = ord(i)
    xor = asc ^ key
    binary_= bin(xor)[2:].zfill(8)
    decrypt= chr(xor)
    variable1 += decrypt
    #print(binary_, end=" ")
print()
print("After Decrypting:",variable1, end="")
print()
```

 ■ This code encrypts and decrypts the text or message entered by user:
 
   ⇨ It ask's the user to enter the messege which must be encrypted.
   <br>
   
   ⇨ It say's to set the [SEED](https://www.geeksforgeeks.org/random-seed-in-python/#:~:text=Seed%20function%20is%20used%20to,number%20generated%20by%20the%20generator)

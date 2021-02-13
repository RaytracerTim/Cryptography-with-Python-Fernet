import datetime
from cryptography.fernet import Fernet

userInput=input()
b=bytes(userInput,'utf-8')
key= Fernet.generate_key()
keyFile=open("key.txt","a")
crypto=Fernet(key)

encrypted=crypto.encrypt(b)
decrypted=crypto.decrypt(encrypted)
keyFile.write("The Key is "+str(key)+"\nKey was created on "+str(datetime.datetime.now())+"\n")
keyFile.write("Encrypted text is "+str(encrypted)+"\nDecrypted text is "+str(decrypted)+"\n\n")
print("The Key is "+str(key)+"\nKey was created on "+str(datetime.datetime.now())+"\n")
print("Encrypted text is "+str(encrypted)+"\nDecrypted text is "+str(decrypted)+"\n\n")
keyFile.close()

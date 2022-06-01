import re 

mail_adress=input("Enter your mail adress: ")
username=mail_adress.split('@', 1)#Utilisation du @ comme séparateur avec 1 occurence
print("Your username is: ", username[0])
print("Your domain is: ", username[1])


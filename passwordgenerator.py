import random
import string

print("~~~~~~~~~~~~~Password Generator~~~~~~~~~~~~~~~")


character_one= string.ascii_uppercase 

character_two= string.digits

character_three= string.punctuation

character_four=string.ascii_lowercase



char=len(character_three)-1

condition=True

while condition is True:
    word=input(" Want a New password? : ")
    if word=="Yes":
        x= int(input(" Enter the length of your password: "))

        password="".join(character_one[random.randint(0,25)]+character_two[random.randint(0,8)]+character_three[random.randint(0,char)]+character_four[random.randint(0,25)] for i in range(0,int(x/2)))

        print("Your new password is :             ",end="")
        print("".join(password[0:x]))

        y=input(" Want to change? : ")

        if y=="No":
            break

        
    else:
        print(" Thank you for using our service :)")
        condition=False    
        

    



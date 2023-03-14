import string
import random

#Define functiona and declare variables
def gen():
    pg1 = string.ascii_uppercase
    
    pg2 = string.ascii_lowercase
    
    pg3 = string.digits
    
    pg4 = string.punctuation

#To accept input from user

    passlen = int(input("Enter the length of the password:"))

#To generate the password and collate all variable as one string
    pg = []
    pg.extend(list(pg1))
    pg.extend(list(pg2))
    pg.extend(list(pg3))
    pg.extend(list(pg4))


#To shuffle the password
    random.shuffle(pg)
    
#To print the password and print the password length based on user input
    pas = ("".join(pg[0:passlen]))
    print('Your', passlen, 'Digit Password is:', pas)


gen()
#Code ends here, By Liberace!!




#This code will cretae a password and specify it starts with upper case letters, lower case letters, numbers and special characters
"""
pg=random.choices(string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation, k=passlen)
    for i in range(passlen):
        print(random.choice(pg),end="")"""
import random
import string

passwords={}

#load existing password file 

try:
    with open("password.txt","r") as file:
      for line in file:
       website ,pwd =line.strip().split(":")
       passwords[website]=pwd

except:
    pass

def generate_password():
    chars=string.ascii_letters+string.digits+"!$%#&@"
    password ="".join(random.choice(chars) for _ in range(8))

    return password

while True:
    print("\n-----PERSONAL PASSWORD MANAGER-----")
    print("1. Save password")
    print("2. View password")
    print("3. Generate password")
    print("4. Exit")

    choice=input("Enter your choice:")

    if choice=="1":
        site=input("Enter Website:")
        pwd=input("Enter Password:")

        passwords[site]=pwd

        with open("password.txt","a") as file:
            file.write(f"{site}:{pwd}\n")
            print("Saved!")

    elif choice=="2":
        if not passwords:
            print("No Data")

        else:
            for site,pwd in passwords.items():
                   print(site,":",pwd)
        

    elif choice=="3":
        print("Generate password",generate_password())

    elif choice=="4":
        print("Ok Bye...")
        break

    else:
        print("Invalid Input")
            


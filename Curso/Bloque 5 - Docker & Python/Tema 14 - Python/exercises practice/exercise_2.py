""" Suppose you are a system administrator and you need to validate user access to a website. Create a script that checks if the entered username and password are correct and allows access only if both are correct.

tips:
- inside the loop, check with an if statement if the entered username and password match the data in your lists.
- maybe use a boolean?
- with enumerate it's cleaner than in range. """

usernames = ["gerard1", "coline2", "marc3"]
passwords = ["pwd1", "pwd2", "pwd3"]

user = input("Username: ")
pwd = input("Password: ")
access = False

# for i in range(len(usernames)):
#     if usernames[i] == user and passwords[i] == pwd:
#         access = True
#         break

for i, username in enumerate(usernames):
    if user == username and pwd == passwords[i]:
        access = True
        break

if access:
    print("Access granted")
else:
    print("Wrong password")

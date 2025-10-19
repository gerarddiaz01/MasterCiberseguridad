# Loops, indexes and lists

## 1-
Suppose you are the owner of an online store and you have a list of sales from the last 30 days. You want to analyze the sales by day of the week to identify the days with the highest sales.

tips:
- make a new list with 7 free spots for each day to add the sales with a loop.
- use a variable to keep count of the week day and reset to 0 when it gets to 7.
- use enumerate for the print to terminal.

sales = [120, 80, 140, 200, 75, 100, 180, 220, 160, 110, 90, 120, 170, 190, 250, 300, 95, 110,
         140, 180, 200, 160, 120, 80, 170, 150, 210, 190, 230, 250]

days_of_week = ["Monday", "Tuesday", "Wednesday",
                "Thursday", "Friday", "Saturday", "Sunday"]

## 2-
Suppose you are a system administrator and you need to validate user access to a website. Create a script that checks if the entered username and password are correct and allows access only if both are correct.

tips:
- inside the loop, check with an if statement if the entered username and password match the data in your lists.
- maybe use a boolean?
- with enumerate it's cleaner than in range.

usernames = ["gerard1", "coline2", "marc3"]
passwords = ["pwd1", "pwd2", "pwd3"]

# Tuples and Sets

## 3-
A social network has a database of users and their corresponding friends.
Create a program that takes a social network database as a list of tuples, where each tuple contains the user's name and a list of their friends.
Repeated names in the friends list correspond to users with several different accounts.
You must remove the duplicate accounts and then return a tuple of tuples containing the real number of friends per user and the user with the most friends.

tips:
- 1. Remove duplicate friends for each user with a loop using sets
- Unpacking to separate values can be useful.
- Create another list with the user and friends non-duplicated.
- 2. Count the number of friends for each user with a for loop and another new list.
- 3. To find the user with the most friends, separate users and friend counts into two lists, find the index of the highest friend count in another variable and use that index to get the user.

social_network = [
    ("Juan", ["Maria", "Pedro", "Luis"]),
    ("Maria", ["Juan", "Pedro", "Juan"]),
    ("Pedro", ["Juan", "Maria"]),
    ("Luis", ["Juan"])
]

## 4- 
A library has a list of books and their authors. Create a program that takes the list of books and their authors as a list of tuples, where each tuple contains the title of the book and the name of the author, and returns a new list of tuples that contains the title of the book and the author's last name.

tips:
- Make a new empty list for the tuples (title, last_name).
- Unpack de tuple so it's easier to handle.
- don't over complicate things, make the whole code a single loop.
- .split()[-1] is used to select the last word.

book_list = [("El aleph", "Jorge Luis Borges"),
             ("Cien años de soledad", "Gabriel Garcia Márquez"),
             ("La ciudad y los perros", "Mario Vargas Llosa")]

## 5-
A company has two customer databases. The first database contains the customer's name, email address, and phone number. The second database contains the customer's name, address, and order history. Write a program that takes both databases as lists of tuples and returns a new list of tuples containing only the customers who appear in both databases with all the information. Customers are considered the same if they have the same name.

tips:
- Separate names into different sets with compressed loops and put the ones that are on both lists in another list with an intersection.
- Open an empty list to add the tuples with all the info from the two main databases, use nested loops and if statements to add only the names in both lists.


database1 = [("Juan", "juan@example.com", "555-1234"),
               ("Maria", "maria@example.com", "555-5678"),
               ("Pedro", "pedro@example.com", "555-9012")]

database2 = [("Juan", "Calle 123", ["Libro1", "Libro2"]),
               ("Maria", "Calle 456", ["Libro3"]),
               ("Luis", "Calle 789", ["Libro4"])]
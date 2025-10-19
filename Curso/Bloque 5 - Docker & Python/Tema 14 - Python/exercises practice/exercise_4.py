""" A library has a list of books and their authors. Create a program that takes the list of books and their authors as a list of tuples, where each tuple contains the title of the book and the name of the author, and returns a new list of tuples that contains the title of the book and the author's last name.

tips:
- Make a new empty list for the tuples (title, last_name).
- Unpack de tuple so it's easier to handle.
- don't over complicate things, make the whole code a single loop.
- .split()[-1] is used to select the last word. """


book_list = [("El aleph", "Jorge Luis Borges"),
             ("Cien años de soledad", "Gabriel Garcia Márquez"),
             ("La ciudad y los perros", "Mario Vargas Llosa")]

titles_last_name = []

for i in book_list:
    title, author = i
    # Only the last word of author is saved into last_name
    last_name = author.split()[-1]
    # We make a list of tuples witht he title and last name
    titles_last_name.append((title, last_name))

print(titles_last_name)

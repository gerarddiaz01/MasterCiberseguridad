""" A company has two customer databases. The first database contains the customer's name, email address, and phone number. The second database contains the customer's name, address, and order history. Write a program that takes both databases as lists of tuples and returns a new list of tuples containing only the customers who appear in both databases. Customers are considered the same if they have the same name. 

tips:
- Separate names into different sets with compressed loops and put the ones that are on both lists in another list with an intersection.
- Open an empty list to add the tuples with all the info from the two main databases, use nested loops and if statements to add only the names in both lists. """

database1 = [("Juan", "juan@example.com", "555-1234"),
             ("Maria", "maria@example.com", "555-5678"),
             ("Pedro", "pedro@example.com", "555-9012")]

database2 = [("Juan", "Calle 123", ["Libro1", "Libro2"]),
             ("Maria", "Calle 456", ["Libro3"]),
             ("Luis", "Calle 789", ["Libro4"])]

names1 = set(person[0] for person in database1)
names2 = set(person[0] for person in database2)

names = names1.intersection(names2)

clients = []
for person1 in database1:
    if person1[0] in names:
        for person2 in database2:
            if person2[0] == person1[0]:
                clients.append(
                    (person1[0], person1[1], person1[2], person2[1], person2[2]))

print(clients)

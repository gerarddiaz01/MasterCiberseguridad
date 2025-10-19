""" A social network has a database of users and their corresponding friends.
Create a program that takes a social network database as a list of tuples, where each tuple contains the user's name and a list of their friends.
Repeated names in the friends list correspond to users with several different accounts.
You must remove the duplicate accounts and then return a tuple of tuples containing the real number of friends per user and the user with the most friends.

tips:
- 1. Remove duplicate friends for each user with a loop using sets
- Unpacking to separate values can be useful.
- Create another list with the user and friends non-duplicated.
- 2. Count the number of friends for each user with a for loop and another new list.
- 3. To find the user with the most friends, separate users and friend counts into two lists, find the index of the highest friend count in another variable and use that index to get the user. """

social_network = [
    ("Juan", ["Maria", "Pedro", "Luis"]),
    ("Maria", ["Juan", "Pedro", "Juan"]),
    ("Pedro", ["Juan", "Maria"]),
    ("Luis", ["Juan"])
]

non_duplicated_list = []

# 1- Remove duplicate friends for each user
for user, friends in social_network:
    friends = list(set(friends))
    non_duplicated_list.append((user, friends))  # making it a tuple here
print("")
print(f"Non-duplicated list: {non_duplicated_list}")
print("")

count_number_friends = []

# 2- Count the number of friends for each user
for user, friends in non_duplicated_list:
    number_friends = len(friends)
    count_number_friends.append(
        (user, number_friends))  # making it a tuple here

print(f"Users with their friends: {count_number_friends}")
print("")

# 3- Find the user with the most friends
# Separate users and friend counts into two lists
user_list = [user[0] for user in count_number_friends]
friends_count_list = [count[1] for count in count_number_friends]

# Find the index of the highest friend count
index_friends_count = friends_count_list.index(max(friends_count_list))

# Use the index to get the username witht he most friends
max_friends_count = user_list[index_friends_count]

print(f"The user with more friends is {max_friends_count}")

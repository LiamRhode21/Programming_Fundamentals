# 1. Create a file named hobbies.py in this folder.
# In that file create a list of the hobbies below in the exact order that they are listed. Hobbies on the list:
#     • playing squash
#     • programming
#     • reading
#     • petting cats
#     • playing golf
#     • visiting friends
#     • playing video games
#     • playing board games
#     • watching movies 
#         ◦ Print out the following in the program.
#             ▪ length of the list
#             ▪ the 5th item in the list
#             ▪ the first four items in the list in a sub list.
#             ▪ the last three items in the list.
# Run the program and make sure it works. Sample output should look like the following:
# Length of the list: 9
# Fifth item in the list: playing golf
# First four items in the list: ['playing squash', 'programming', 'reading', 'petting cats']
# last three items in the list: ['playing video games', 'playing board games', 'watching movies']


hobbies = ["playing squash", "programming", "reading", "petting cats", "playing golf", "visiting friends", 
           "playing video games", "playing board games", "watching movies"]

print(f"Length of the list: {len(hobbies)}")
print(f"The 5th item in the list is: {hobbies[4]}")
print(f"First four items in the list: {hobbies[:4]}")
print(f"Last three items in the list: {hobbies[-3:]}")
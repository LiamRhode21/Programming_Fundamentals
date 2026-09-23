# 2. Create a file named tech_shows.py in this folder.
# In that file create a list with the following tv shows and movies in the exact order that they are listed.  Shows on the list:
#     • Silicon Valley
#     • Halt and Catch Fire
#     • Blackberry
#     • The Billion Dollar Code
#     • Mr. Robot
#     • The IT Crowd
#     • WeCrashed
#     • The Social Network
#     • Severance
#     • Pirates of Silicon Valley
#         ◦ Print out the following information from the list.
#     • The first item on the list.
#     • The last item on the list.
#     • Change "WeCrashed" to "The Dropout"
#     • Change "The Social Network" to "Black Mirror"
#     • values from the 5th item up to (and including) the 9th item 
# Run the program and make sure it works. Sample output should look like the following:
# The best show is: Silicon Valley
# The most classic show is: Pirates of Silicon Valley
# The fourth to ninth shows on the list are:
# ['The Billion Dollar Code', 'Mr. Robot', 'The IT Crowd', 'The Dropout', 'Black Mirror', 'Severance']
tv_and_movies = ["Silicon Valley", "Halt and Catch Fire", "Blackberry", "The Billion Dollar Code", "Mr. Robot", "The IT Crowd", "WeCrashed",
                 "The Social Network", "Severance", "Pirates of Silicon Valley"]

print(f"The best show is: {tv_and_movies[0]}")
print(f"The most classic show is: {tv_and_movies[len(tv_and_movies) - 1]}")

tv_and_movies[6] = "The Dropout"
tv_and_movies[7] = "Black Mirror"

print(f"The fourth to ninth shows on the list are: {tv_and_movies[4:9]}")
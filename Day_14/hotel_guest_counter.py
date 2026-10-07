# Welcome to the Loop Inn! You are the front desk programmer. Before breakfast, the kitchen needs to know how many guests 
# are staying. Build a program that checks every room and counts everyone—even the late sleepers!
# Your task
#     1. Ask the user for the number of floors and the number of rooms per floor. Assume every floor has the same number of 
# rooms.

floors = int(input("Enter number of floors: "))
rooms = int(input("Enter number of rooms: "))

#     2. Use an outer for loop for floors and an inner for loop for rooms. Use range() and start numbering both at 1.


#     3. For each room, ask for the number of guests. Immediately print the floor, room, and number of guests entered.
guests_total = 0
room_records = []

for floor in range(1, floors + 1):
    for room in range(1, rooms + 1):
        guests_per_room = int(input(f"Floor {floor}, room {room} - Enter number of guests: "))
        print(f"Floor {floor}, Room {room}, Number of guests: {guests_per_room}")
        guests_total += guests_per_room
        room_records.append((floor, room, guests_per_room))

print("HOTEL ROOM SUMMARY\n")

for tuple in room_records:
    floor, room, guests_per_room = tuple
    print(f"Floor: {floor} | Room: {room} | Guests: {guests_per_room}")

print(f"\nTotal guests: {guests_total}")




print("HOTEL ROOM SUMMARY\n")
print(f"{"Floor":<8}{"Room":<8}{"Guests":<8}")
print("-" * 24)
for floor, room, guests_per_room in room_records:
    print(f"{floor:<8}{room:<8}{guests_per_room:<8}")
#     4. Keep a running total and print the total number of guests after all rooms have been checked.
# Assume the user enters valid whole numbers: at least 1 floor and 1 room per floor, and 0 or more guests per room.
# Sample run
# Number of floors: 2
# Rooms per floor: 2

# Floor 1, room 1 — enter number of guests: 2
# Floor 1, room 1 — number of guests: 2

# Floor 1, room 2 — enter number of guests: 0
# Floor 1, room 2 — number of guests: 0

# Floor 2, room 1 — enter number of guests: 3
# Floor 2, room 1 — number of guests: 3

# Floor 2, room 2 — enter number of guests: 1
# Floor 2, room 2 — number of guests: 1

# Total number of guests: 6
# Before you check out
# Test a hotel with 1 floor and 3 rooms. Enter 0, 4, and 2 guests. Your total should be 6. Then try all empty 
# rooms: the total should be 0.
# Hint: Set your total to 0 before either loop begins. Add each room’s guest count to the total inside the inner loop.

# Extra challenge
# Give the Loop Inn a room report
# The manager wants a room summary after you finish entering the guest counts. Extend your program to save the room details 
# in a list of tuples, then display them in a readable format.
#     5. Create an empty list called room_records before the loops begin.
#     6. Inside the inner loop, create a tuple in this order: (floor_number, room_number, number_of_guests). Append that 
# tuple to room_records.
#     7. After all rooms have been entered, print room_records once so you can inspect your list of tuples.
#     8. Loop through room_records and unpack each tuple into three variables. Print one labelled line per room, then 
# display the total number of guests.
# Expected list for the sample run
# [(1, 1, 2), (1, 2, 0), (2, 1, 3), (2, 2, 1)]
# Formatted room report
# HOTEL ROOM SUMMARY

# Floor 1 | Room 1 | Guests: 2
# Floor 1 | Room 2 | Guests: 0
# Floor 2 | Room 1 | Guests: 3
# Floor 2 | Room 2 | Guests: 1

# Total number of guests: 6
# Hint: Use append() to add a tuple to the list. Unpacking lets you give each value a meaningful variable name when printing 
# the report.
# Check your work
# The 2-floor, 2-room example should create four tuples. Include rooms with 0 guests, keep rooms in floor and room order, 
# and check that the guest counts still add up to 6.
# Use breakpoint() to use the python debugger
# l - list surrounding lines
# n - next line
# c - go to next breakpoint (continue)

floors = int(input("Enter number of floors: "))
rooms = int(input("Enter number of rooms: "))
# breakpoint()
guests_total = 0
room_records = []

for floor in range(1, floors + 1):
    for room in range(1, rooms + 1):
        guests_per_room = int(input(f"Floor {floor}, room {room} - Enter number of guests: "))
        print(f"Floor {floor}, Room {room}, Number of guests: {guests_per_room}")
        guests_total += guests_per_room
        room_records.append((floor, room, guests_per_room))

print("HOTEL ROOM SUMMARY\n")
# breakpoint()
for tuple in room_records:
    floor, room, guests_per_room = tuple
    print(f"Floor: {floor} | Room: {room} | Guests: {guests_per_room}")

print(f"\nTotal guests: {guests_total}")


print("HOTEL ROOM SUMMARY\n")
print(f"{"Floor":<8}{"Room":<8}{"Guests":<8}")
print("-" * 24)
for floor, room, guests_per_room in room_records:
    print(f"{floor:<8}{room:<8}{guests_per_room:<8}")
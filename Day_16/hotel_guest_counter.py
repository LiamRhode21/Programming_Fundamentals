floors = int(input("Number of floors: "))
rooms = int(input("Rooms per floor: "))

floor = 1
total_guests = 0
floor_guests_list = []

while floor <= floors:
    room = 1
    floor_guests = 0
    while room <= rooms:
        guests = int(input(f"Floor {floor}, Room {room} - number of guests: "))
        total_guests += guests
        floor_guests += guests
        room += 1
    floor += 1
    floor_guests_list.append(floor_guests)

print(f'Total guests: {total_guests}')
print(f"Guest per floor:\n")
for index, guest_per_floor in enumerate(floor_guests_list, start= 1):
    print(f"Floor {index}: {guest_per_floor}")
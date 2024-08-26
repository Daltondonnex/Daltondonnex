import random

# Initialize the room with a size of 4x4
room = [[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]]

def display(room):
    for rows in room:
        print(rows)
    print("Initially, all rooms are dirty")

# Display the initial state of the room
display(room)

# Randomly make rooms dirty or clean
for x in range(4):
    for y in range(4):
        room[x][y] = random.choice([0, 1])

# Display the room state after random dirt placement
print("Room state after random dirt placement:")
display(room)

# Initialize dirt_room counter
dirt_room = 0

# Clean the room and calculate performance
for x in range(4):
    for y in range(4):
        if room[x][y] == 1:
            print("Cleaning the room at position:", x, y)
            room[x][y] = 0
            dirt_room += 1

# Calculate performance
performance = (100 - (dirt_room / 16)) * 1000
print(f"Performance: {performance}")

# Display the final state of the room
print("Final state of the room after cleaning:")
display(room)
# Sample Python code that can be used to generate rooms in
# a zig-zag pattern.
#
# You can modify generate_rooms() to create your own
# procedural generation algorithm and use print_rooms()
# to see the world.


class Room:
    def __init__(self, id, name, description, x, y):
        self.id = id
        self.name = name
        self.description = description
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None
        self.x = x
        self.y = y
    def __repr__(self):
        if self.e_to is not None:
            return f"({self.x}, {self.y}) -> ({self.e_to.x}, {self.e_to.y})"
        return f"({self.x}, {self.y})"
    def connect_rooms(self, connecting_room, direction):
        '''
        Connect two rooms in the given n/s/e/w direction
        '''
        reverse_dirs = {"n": "s", "s": "n", "e": "w", "w": "e"}
        reverse_dir = reverse_dirs[direction]
        setattr(self, f"{direction}_to", connecting_room)
        setattr(connecting_room, f"{reverse_dir}_to", self)
    def get_room_in_direction(self, direction):
        '''
        Connect two rooms in the given n/s/e/w direction
        '''
        return getattr(self, f"{direction}_to")


class World:
    def __init__(self):
        self.grid = None
        self.width = 0
        self.height = 0
    def generate_rooms(self, size_x, size_y, num_rooms):
        '''
        Fill up the grid, bottom to top, in a zig-zag pattern
        '''

        # Initialize the grid
        self.grid = [None] * size_y
        self.width = size_x
        self.height = size_y
        for i in range( len(self.grid) ):
            self.grid[i] = [None] * size_x
        
        print(self.grid)
        # Start from lower-left corner (0,0)
        x = -1 # (this will become 0 on the first step)
        y = 0
        room_count = 0

        # Start generating rooms to the east
        direction = 1  # 1: east, -1: west


        # While there are rooms to be created...
        previous_room = None
        while room_count < num_rooms:

            # Calculate the direction of the room to be created
            if direction > 0 and x < size_x - 1:
                room_direction = "e"
                x += 1
            elif direction < 0 and x > 0:
                room_direction = "w"
                x -= 1
            else:
                # If we hit a wall, turn north and reverse direction
                room_direction = "n"
                y += 1
                direction *= -1

            # Create a room in the given direction
            room = Room(room_count, "A Generic Room", "This is a generic room.", x, y)
            # Note that in Django, you'll need to save the room after you create it

            # Save the room in the World grid
            self.grid[y][x] = room

            # Connect the new room to the previous room
            if previous_room is not None:
                previous_room.connect_rooms(room, room_direction)

            # Update iteration variables
            previous_room = room
            room_count += 1



    def print_rooms(self):
        '''
        Print the rooms in room_grid in ascii characters.
        '''

        # Add top border
        str = "# " * ((3 + self.width * 5) // 2) + "\n"

        # The console prints top to bottom but our array is arranged
        # bottom to top.
        #
        # We reverse it so it draws in the right direction.
        reverse_grid = list(self.grid) # make a copy of the list
        reverse_grid.reverse()
        for row in reverse_grid:
            # PRINT NORTH CONNECTION ROW
            str += "#"
            for room in row:
                if room is not None and room.n_to is not None:
                    str += "  |  "
                else:
                    str += "     "
            str += "#\n"
            # PRINT ROOM ROW
            str += "#"
            for room in row:
                if room is not None and room.w_to is not None:
                    str += "-"
                else:
                    str += " "
                if room is not None:
                    str += f"{room.id}".zfill(3)
                else:
                    str += "   "
                if room is not None and room.e_to is not None:
                    str += "-"
                else:
                    str += " "
            str += "#\n"
            # PRINT SOUTH CONNECTION ROW
            str += "#"
            for room in row:
                if room is not None and room.s_to is not None:
                    str += "  |  "
                else:
                    str += "     "
            str += "#\n"

        # Add bottom border
        str += "# " * ((3 + self.width * 5) // 2) + "\n"

        # Print string
        print(str)


w = World()
num_rooms = 100
width = 20
height = 5
w.generate_rooms(width, height, num_rooms)
w.print_rooms()


print(f"\n\nWorld\n  height: {height}\n  width: {width},\n  num_rooms: {num_rooms}\n")

# cords = []



# counter = 0
# for i in range(10):
#     print(counter)
#     if counter % 2 == 0:
#         for j in range(10):
#             cords.append({Foo(i, j)})
            
#     else:
#         for j in range(9, -1, -1):
#             cords.append({Foo(i, j)})
#     counter += 1
            

    
# print(cords)

# class Foo:
#     def __init__(self, d, h, color):
#         self.d = d
#         self.h = h
#         self.color = color

#     def __repr__(self):
#         return 'x: ' + f'{self.d}' + ', ' + 'y: ' +f'{self.h}' + ', ' + 'color: ' + f'{self.color}'

# data = [["A1", "A2", 0],
# ["A1", "B2", 1],
# ["A1", "C2", 2],
# ["A1", "D2", 3],
# ["A1", "I2", 8],
# ["A1", "J2", 9],
# ["B1", "A2", 1],
# ["B1", "B2", 1],
# ["B1", "C2", 1],
# ["B1", "D2", 1],
# ["B1", "E2", 1],
# ["B1", "F2", 1],
# ["B1", "G2", 1],
# ["B1", "H2", 1],
# ["B1", "J2", 1],
# ["C1", "A2", 2],
# ["C1", "D2", 2],
# ["C1", "E2", 2],
# ["C1", "F2", 1],
# ["C1", "G2", 2],
# ["C1", "H2", 2],
# ["C1", "I2", 2],
# ["C1", "J2", 3],
# ["D1", "C2", 3],
# ["D1", "D2", 3],
# ["D1", "G2", 1],
# ["D1", "H2", 3],
# ["D1", "I2", 1],
# ["D1", "J2", 3],
# ["E1", "A2", 4],
# ["E1", "B2", 4],
# ["E1", "D2", 4],
# ["E1", "E2", 4],
# ["E1", "G2", 4],
# ["E1", "H2", 4],
# ["E1", "I2", 4],
# ["F1", "A2", 5],
# ["F1", "B2", 5],
# ["F1", "C2", 5],
# ["F1", "D2", 5],
# ["F1", "E2", 5],
# ["F1", "F2", 5],
# ["F1", "G2", 5],
# ["F1", "H2", 5],
# ["F1", "I2", 5],
# ["F1", "J2", 5],
# ["G1", "A2", 6],
# ["G1", "C2", 6],
# ["G1", "D2", 6],
# ["G1", "G2", 6],
# ["G1", "H2", 6],
# ["G1", "I2", 6],
# ["H1", "A2", 7],
# ["H1", "C2", 7],
# ["H1", "D2", 7],
# ["H1", "E2", 7],
# ["H1", "F2", 7],
# ["H1", "G2", 7],
# ["H1", "H2", 7],
# ["H1", "J2", 7],
# ["I1", "A2", 8],
# ["I1", "C2", 8],
# ["I1", "D2", 8],
# ["I1", "E2", 8],
# ["I1", "F2", 8],
# ["I1", "G2", 8],
# ["I1", "H2", 8],
# ["I1", "I2", 8],
# ["I1", "J2", 8],
# ["J1", "A2", 9],
# ["J1", "C2", 9],
# ["J1", "D2", 9],
# ["J1", "F2", 9],
# ["J1", "G2", 9],
# ["J1", "H2", 9],
# ["J1", "I2", 9],
# ["J1", "J2", 9]]

# for i in range(len(data)):
#     data[i] = {Foo(data[i][0], data[i][1], data[i][2])}

# print(data)
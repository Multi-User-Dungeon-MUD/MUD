from django.contrib.auth.models import User
from adventure.models import Player, Room


Room.objects.all().delete()

# r_outside = Room(title="Outside Cave Entrance",
#                description="North of you, the cave mount beckons")

# r_foyer = Room(title="Foyer", description="""Dim light filters in from the south. Dusty
# passages run north and east.""")

# r_overlook = Room(title="Grand Overlook", description="""A steep cliff appears before you, falling
# into the darkness. Ahead to the north, a light flickers in
# the distance, but there is no way across the chasm.""")

# r_narrow = Room(title="Narrow Passage", description="""The narrow passage bends here from west
# to north. The smell of gold permeates the air.""")

# r_treasure = Room(title="Treasure Chamber", description="""You've found the long-lost treasure
# chamber! Sadly, it has already been completely emptied by
# earlier adventurers. The only exit is to the south.""")

<<<<<<< HEAD
# r_outside.save()
# r_foyer.save()
# r_overlook.save()
# r_narrow.save()
# r_treasure.save()
=======
r_hall = Room(title="hall", description="""As passage.""")

r_dead_end = Room(title="Dead End", description="""Nowhere to go.""")


r_foyer.save()
r_overlook.save()
r_narrow.save()
r_treasure.save()
r_hall.save()
r_dead_end.save()
>>>>>>> b02261b76dafcbb44474335787f6f3699a4b9a16

# # Link rooms together
# r_outside.connectRooms(r_foyer, "n")
# r_foyer.connectRooms(r_outside, "s")

# r_foyer.connectRooms(r_overlook, "n")
# r_overlook.connectRooms(r_foyer, "s")

# r_foyer.connectRooms(r_narrow, "e")
# r_narrow.connectRooms(r_foyer, "w")

# r_narrow.connectRooms(r_treasure, "n")
# r_treasure.connectRooms(r_narrow, "s")

<<<<<<< HEAD
# players=Player.objects.all()
# for p in players:
#   p.currentRoom=r_outside.id
#   p.save()
=======
r_treasure.connectRooms(r_hall, "n")
r_hall.connectRooms(r_treasure, "s")

r_hall.connectRooms(r_dead_end, "e")
r_dead_end.connectRooms(r_hall, "w")

players=Player.objects.all()
for p in players:
  p.currentRoom=r_outside.id
  p.save()
>>>>>>> b02261b76dafcbb44474335787f6f3699a4b9a16

#Objects
#objects = [[Room(title="some,numbers", description= "dungeon")] X10]

#Movements
#movements = [[somenumber, somenumber, somenumber, somenumber, somenumber, somenumber, somenumber, somenumber, somenumber, somenumber] X10]


def conNorth(index_1, index_2, object_array):
  object_array[index_1][index_2].connectRooms(object_array[index_1-1][index_2], "n")
def conSouth(index_1, index_2, object_array):
  object_array[index_1][index_2].connectRooms(object_array[index_1+1][index_2], "s")
def conEast(index_1, index_2, object_array):
  object_array[index_1][index_2].connectRooms(object_array[index_1][index_2+1], "e")
def conWest(index_1, index_2, object_array):
  object_array[index_1][index_2].connectRooms(object_array[index_1][index_2-1], "w")

#Save all rooms
#for i in range(0, 10):
##for j in range(0,10):
###objects[i][j].save

def map_room(room_movement_array, room_object_array):
  for i in range(0,10):
    for j in range(0,10):
      if room_movement_array[i][j] == 0:
        conNorth(i,j, room_object_array)
      elif room_movement_array[i][j] == 1:
        conEast(i,j, room_object_array)
      elif room_movement_array[i][j] == 2:
        conSouth(i,j, room_object_array)
      elif room_movement_array[i][j] == 3:
        conWest(i,j, room_object_array)
      elif room_movement_array[i][j] == 4:
        conNorth(i,j, room_object_array)
        conSouth(i,j, room_object_array)
      elif room_movement_array[i][j] == 5:
        conWest(i,j, room_object_array)
        conEast(i,j, room_object_array)
      elif room_movement_array[i][j] == 6:
        conNorth(i,j, room_object_array)
        conWest(i,j, room_object_array)
      elif room_movement_array[i][j] == 7:
        conNorth(i,j, room_object_array)
        conEast(i,j, room_object_array)
      elif room_movement_array[i][j] == 8:
        conEast(i,j, room_object_array)
        conSouth(i,j, room_object_array)
      elif room_movement_array[i][j] == 9:
        conWest(i,j, room_object_array)
        conSouth(i,j, room_object_array)
      elif room_movement_array[i][j] == 10:
        conNorth(i,j, room_object_array)
        conEast(i,j, room_object_array)
        conSouth(i,j, room_object_array)
      elif room_movement_array[i][j] == 11:
        conNorth(i,j, room_object_array)
        conWest(i,j, room_object_array)
        conSouth(i,j, room_object_array)
      elif room_movement_array[i][j] == 12:
        conWest(i,j, room_object_array)
        conEast(i,j, room_object_array)
        conNorth(i,j, room_object_array)
      elif room_movement_array[i][j] == 13:
        conWest(i,j, room_object_array)
        conEast(i,j, room_object_array)
        conSouth(i,j, room_object_array)
      elif room_movement_array[i][j] == 14:
        conNorth(i,j, room_object_array)
        conEast(i,j, room_object_array)
        conSouth(i,j, room_object_array)
        conWest(i,j, room_object_array)
      elif room_movement_array[i][j] == 15: 
        pass

#Map Rooms
#map_room(movements, objects)

#Connect Objects to Rooms
#objects[somenumber][somenumber].connectRooms(objects[somenumber][somenumber], "applicable direction")
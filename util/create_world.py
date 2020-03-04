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

r_hall = Room(title=" hall ", description="""As passage.""")

r_dead_end = Room(title=" Dead End", description="""Nowhere to go.""")

r_e_river = Room(title=" East River ", description=" You do not know how to swim and this River is deep. ")

r_volcano = Room(title=" Volcano ", description=" Supposedly inactive. ")

r_windy_cliff = Room(title=" Windy Cliff ", description=" Don't stand too close to the edge of the cliff. The winds will push you right off into the River below. ")

r_cave_entrance = Room(title=" Cave Entrance ", description=" Dark and mysterious. Something is in there. ")

r_waterfall = Room(title=" Waterfall ", description=" Beautiful and majestic. You cannot climb this waterfall or swim in it's river. ")

r_hell = Room(title=" Hell ", description=" You know why you're here. ")

r_chasm = Room(title=" The Chasm ", description=" The wind in this chasm is overpowering. You drop all of your items because of it. Ahead you can see a cave entrance. ")

r_chamber_of_swords = Room(title=" Chamber of Swords ", description=" Deep into the cave you are now in the Chamber of Swords. Crystals are jutting from the all surfaces.  ")

r_w_river = Room(title=" West River ", description=" River that runs west. You can cross if you are wearing boots. ")

r_ruins = Room(title=" Ruins ", description=" Seems to be several burned remenants of a town that used to be here.")

r_olms_dungeon = Room(title=" Olm's Dungeon ", description=" This European amphiphibian is roughly 100 years young. He is very blind. He pays you no mind.")

r_blind_cave_fish = Room(title=" Blind Cave Fish Tavern ", description=" Run by Mr. Blind-Cave-Fish. He has lived his whole life in this cave and only wishes to help others. ")

r_redtailed_racer = Room(title=" Redtailed Racer's Cavern", description=" A small cavern with a green snake coiled in the middle. Perhaps we should turn around. ")

r_river = Room(title=" Main River ", description=" The main river that feeds the waterfall.  ")

r_road = Room(title=" Road ", description=" Cobblestoned road with a wooden fence running along side of it. ")

r_beach = Room(title=" Beach ", description=" It is sunny year round and smells of the fresh water river ahead.")

r_camp = Room(title=" Camp ", description=" A place to rest.")

r_camp_fire = Room(title=" Camp Fire ", description=" A dangerous element being used for warmth.")

r_locked_door = Room(title=" Locked Door ", description=" A locked door that reads 'Aryas Room'.  ")

r_zeldas_apothacary = Room(title=" Zelda's Apothacary ", description=" Zelda is always ready to help you in your quest, if you have enough gold.")

r_foyer.save()
r_overlook.save()
r_narrow.save()
r_treasure.save()
r_hall.save()
r_dead_end.save()
r_zeldas_apothacary.save()
r_locked_door.save()
r_camp_fire.save()
r_beach.save()
r_road.save()
r_river.save()
r_redtailed_racer.save()
r_blind_cave_fish.save()
r_olms_dungeon.save()
r_ruins.save()
r_w_river.save()
r_chamber_of_swords.save()
r_chasm.save()
r_hell.save()
r_waterfall.save()
r_cave_entrance.save()
r_windy_cliff.save()
r_volcano.save()
r_e_river.save()


# # Link rooms together
# r_outside.connectRooms(r_foyer, "n")
# r_foyer.connectRooms(r_outside, "s")

# r_foyer.connectRooms(r_overlook, "n")
# r_overlook.connectRooms(r_foyer, "s")

# r_foyer.connectRooms(r_narrow, "e")
# r_narrow.connectRooms(r_foyer, "w")

# r_narrow.connectRooms(r_treasure, "n")
# r_treasure.connectRooms(r_narrow, "s")

r_treasure.connectRooms(r_hall, "n")
r_hall.connectRooms(r_treasure, "s")

r_hall.connectRooms(r_dead_end, "e")
r_dead_end.connectRooms(r_hall, "w")

players=Player.objects.all()
for p in players:
  p.currentRoom=r_outside.id
  p.save()

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
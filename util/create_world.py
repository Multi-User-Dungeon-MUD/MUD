from django.contrib.auth.models import User
from adventure.models import Player, Room
import random

Room.objects.all().delete()

fire_room = 0
for i in range(50):
  newRoom = Room(title=f"Fire Room {fire_room}",
               description="Flames")
  newRoom.save()
  fire_room += 1

def room_gen(rooms):
    def link_rooms_n_s(room1, room2):
      room1.connectRooms(room2, 'n')
      room2.connectRooms(room1, 's')
      room1.save()
      room2.save()
    def link_rooms_s_n(room1, room2):
      room1.connectRooms(room2, 's')
      room2.connectRooms(room1, 'n')
      room1.save()
      room2.save()
    def link_rooms_e_w(room1, room2):
      room1.connectRooms(room2, 'e')
      room2.connectRooms(room1, 'w')
      room1.save()
      room2.save()
    def link_rooms_w_e(room1, room2):
      room1.connectRooms(room2, 'w')
      room2.connectRooms(room1, 'e')
      room1.save()
      room2.save()
    direction1 = ['n']
    direction2 = ['e', 'w']
    for i in range(1, 50):
        if i % 2 != 0:
          random_choice = random.choice(direction1)
          if random_choice == direction1[0]:
            link_rooms_n_s(rooms.get(id=i), rooms.get(id=i + 1))
          else:
            link_rooms_s_n(rooms.get(id=i), rooms.get(id=i + 1))
        else:
          random_choice = random.choice(direction2)
          if random_choice == direction2[0]:
            link_rooms_e_w(rooms.get(id=i), rooms.get(id=i + 1))
          else:
            link_rooms_w_e(rooms.get(id=i), rooms.get(id=i + 1))

room_gen(Room.objects.all())
  
random_int = random.randint(1, 20)
      while random_int in used_int:
          random_int = random.randint(1, 20)
      
      used_int.append(random_int)
      print(used_int)
      if i in used_int:
        pass
      else:

r_outside = Room(title="Outside Cave Entrance",
               description="North of you, the cave mount beckons")

r_foyer = Room(title="Foyer", description="""Dim light filters in from the south. Dusty
passages run north and east.""")

r_overlook = Room(title="Grand Overlook", description="""A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""")

r_narrow = Room(title="Narrow Passage", description="""The narrow passage bends here from west
to north. The smell of gold permeates the air.""")

r_treasure = Room(title="Treasure Chamber", description="""You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""")

r_hall = Room(title="hall", description="""As passage.""")

r_dead_end = Room(title="Dead End", description="""Nowhere to go.""")

r_stairs = Room(title="stairs", description="""go to the balcony""")

r_balcony = Room(title="balcony", description="""Nowhere to go.""")

r_cave = Room(title="cave", description="""Nowhere to go.""")

r_study = Room(title="study", description="""Nowhere to go.""")

r_outside.save()
r_foyer.save()
r_overlook.save()
r_narrow.save()
r_treasure.save()
r_hall.save()
r_dead_end.save()
r_balcony.save()
r_stairs.save()
r_cave.save()
r_study.save()

# Link rooms together
r_outside.connectRooms(r_foyer, "n")
r_foyer.connectRooms(r_outside, "s")

r_foyer.connectRooms(r_overlook, "n")
r_overlook.connectRooms(r_foyer, "s")

r_foyer.connectRooms(r_narrow, "e")
r_narrow.connectRooms(r_foyer, "w")

r_narrow.connectRooms(r_treasure, "n")
r_treasure.connectRooms(r_narrow, "s")

r_treasure.connectRooms(r_hall, "n")
r_hall.connectRooms(r_treasure, "s")

r_hall.connectRooms(r_dead_end, "e")
r_dead_end.connectRooms(r_hall, "w")

r_dead_end.connectRooms(r_balcony, "s")
r_balcony.connectRooms(r_dead_end, "n")

r_dead_end.connectRooms(r_stairs, "e")
r_stairs.connectRooms(r_dead_end, "w")

r_stairs.connectRooms(r_cave, "n")
r_cave.connectRooms(r_stairs, "s")

r_cave.connectRooms(r_study, "w")
r_study.connectRooms(r_cave, "e")

players=Player.objects.all()
for p in players:
  p.currentRoom=r_outside.id
  p.save()

 # if room1.n_to != 0:
  #   setattr(room1, 'w_to', Room.objects.get(id=room2.id).id)
  #   setattr(room2, 'e_to', Room.objects.get(id=room1.id).id)
  # else:
  
  #if room1 doesn't have a n_to attribute assign
  #if room1 one already has n_to attribute assign e or w
  # reverse_dirs = {"n": "s", "s": "n", "e": "w", "w": "e"}
  # random_integer = random.randint(1, 4)
  # direction = ''
  # if random_integer == 1:
  #   direction = 'n'
  # elif random_integer == 2:
  #   direction = 's'
  # elif random_integer == 3:
  #   direction = 'e'
  # elif random_integer == 4:
  #   direction = 'w'
  
  # room1.connectRooms(room2, direction)
  # room2.connectRooms(room1, reverse_dirs[direction])


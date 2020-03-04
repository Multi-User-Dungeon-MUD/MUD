from django.contrib.auth.models import User
from adventure.models import Player, Room

Room.objects.all().delete()

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
r_stairs.save()
r_balcony.save()
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

r_dead_end.connectRooms(r_stairs, "e")
r_stairs.connectRooms(r_dead_end, "w")


r_dead_end.connectRooms(r_balcony, "s")
r_balcony.connectRooms(r_dead_end, "n")

r_stairs.connectRooms(r_cave, "n")
r_cave.connectRooms(r_stairs, "s")

r_cave.connectRooms(r_study, "w")
r_study.connectRooms(r_cave, "e")

players=Player.objects.all()
for p in players:
  p.currentRoom=r_outside.id
  p.save()


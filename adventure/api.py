from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
# from pusher import Pusher
from django.http import JsonResponse
from decouple import config
from django.contrib.auth.models import User
from .models import *
from rest_framework.decorators import api_view
import json

# instantiate pusher
# pusher = Pusher(app_id=config('PUSHER_APP_ID'), key=config('PUSHER_KEY'), secret=config('PUSHER_SECRET'), cluster=config('PUSHER_CLUSTER'))

@csrf_exempt
@api_view(["GET"])
def initialize(request):
    user = request.user
    player = user.player
    player_id = player.id
    uuid = player.uuid
    room = player.room()
    players = room.playerNames(player_id)
    return JsonResponse({'uuid': uuid, 'name':player.user.username, 'title':room.title, 'description':room.description, 'players':players}, safe=True)


# @csrf_exempt
@api_view(["POST"])
def move(request):
    dirs={"n": "north", "s": "south", "e": "east", "w": "west"}
    reverse_dirs = {"n": "south", "s": "north", "e": "west", "w": "east"}
    player = request.user.player
    player_id = player.id
    player_uuid = player.uuid
    data = json.loads(request.body)
    direction = data['direction']
    room = player.room()
    nextRoomID = None
    if direction == "n":
        nextRoomID = room.n_to
    elif direction == "s":
        nextRoomID = room.s_to
    elif direction == "e":
        nextRoomID = room.e_to
    elif direction == "w":
        nextRoomID = room.w_to
    if nextRoomID is not None and nextRoomID > 0:
        nextRoom = Room.objects.get(id=nextRoomID)
        player.currentRoom=nextRoomID
        player.save()
        players = nextRoom.playerNames(player_id)
        currentPlayerUUIDs = room.playerUUIDs(player_id)
        nextPlayerUUIDs = nextRoom.playerUUIDs(player_id)
        # for p_uuid in currentPlayerUUIDs:
        #     pusher.trigger(f'p-channel-{p_uuid}', u'broadcast', {'message':f'{player.user.username} has walked {dirs[direction]}.'})
        # for p_uuid in nextPlayerUUIDs:
        #     pusher.trigger(f'p-channel-{p_uuid}', u'broadcast', {'message':f'{player.user.username} has entered from the {reverse_dirs[direction]}.'})
        return JsonResponse({'name':player.user.username, 'title':nextRoom.title, 'description':nextRoom.description, 'players':players, 'error_msg':""}, safe=True)
    else:
        players = room.playerNames(player_id)
        return JsonResponse({'name':player.user.username, 'title':room.title, 'description':room.description, 'players':players, 'error_msg':"You cannot move that way."}, safe=True)


@csrf_exempt
@api_view(["POST"])
def say(request):
    # IMPLEMENT
    return JsonResponse({'error':"Not yet implemented"}, safe=True, status=500)

    
@csrf_exempt
@api_view(["GET"])
def show_map(request):
    data = [
    { 'x': "A1", 'y': "A2", 'color': "player" },
    { 'x': "A1", 'y': "B2", 'color': "not" },
    { 'x': "A1", 'y': "C2", 'color': "not" },
    { 'x': "A1", 'y': "E2", 'color': "not" },
    { 'x': "A1", 'y': "F2", 'color': "not" },
    { 'x': "A1", 'y': "G2", 'color': "not" },
    { 'x': "A1", 'y': "H2", 'color': "not" },
    { 'x': "A1", 'y': "I2", 'color': "not" },
    { 'x': "A1", 'y': "J2", 'color': "not" },
    { 'x': "B1", 'y': "A2", 'color': "not" },
    { 'x': "B1", 'y': "B2", 'color': "not" },
    { 'x': "B1", 'y': "C2", 'color': "not" },
    { 'x': "B1", 'y': "D2", 'color': "not" } ]

    print(data)
    # data = [["A1", "A2", 0],
    #     ["A1", "B2", 1],
    #     ["A1", "C2", 2],
    #     ["A1", "D2", 3],
    #     ["A1", "I2", 8],
    #     ["A1", "J2", 9],
    #     ["B1", "A2", 1],
    #     ["B1", "B2", 1],
    #     ["B1", "C2", 1],
    #     ["B1", "D2", 1],
    #     ["B1", "E2", 1],
    #     ["B1", "F2", 1],
    #     ["B1", "G2", 1],
    #     ["B1", "H2", 1],
    #     ["B1", "J2", 1],
    #     ["C1", "A2", 2],
    #     ["C1", "D2", 2],
    #     ["C1", "E2", 2],
    #     ["C1", "F2", 1],
    #     ["C1", "G2", 2],
    #     ["C1", "H2", 2],
    #     ["C1", "I2", 2],
    #     ["C1", "J2", 3],
    #     ["D1", "C2", 3],
    #     ["D1", "D2", 3],
    #     ["D1", "G2", 1],
    #     ["D1", "H2", 3],
    #     ["D1", "I2", 1],
    #     ["D1", "J2", 3],
    #     ["E1", "A2", 4],
    #     ["E1", "B2", 4],
    #     ["E1", "D2", 4],
    #     ["E1", "E2", 4],
    #     ["E1", "G2", 4],
    #     ["E1", "H2", 4],
    #     ["E1", "I2", 4],
    #     ["F1", "A2", 5],
    #     ["F1", "B2", 5],
    #     ["F1", "C2", 5],
    #     ["F1", "D2", 5],
    #     ["F1", "E2", 5],
    #     ["F1", "F2", 5],
    #     ["F1", "G2", 5],
    #     ["F1", "H2", 5],
    #     ["F1", "I2", 5],
    #     ["F1", "J2", 5],
    #     ["G1", "A2", 6],
    #     ["G1", "C2", 6],
    #     ["G1", "D2", 6],
    #     ["G1", "G2", 6],
    #     ["G1", "H2", 6],
    #     ["G1", "I2", 6],
    #     ["H1", "A2", 7],
    #     ["H1", "C2", 7],
    #     ["H1", "D2", 7],
    #     ["H1", "E2", 7],
    #     ["H1", "F2", 7],
    #     ["H1", "G2", 7],
    #     ["H1", "H2", 7],
    #     ["H1", "J2", 7],
    #     ["I1", "A2", 8],
    #     ["I1", "C2", 8],
    #     ["I1", "D2", 8],
    #     ["I1", "E2", 8],
    #     ["I1", "F2", 8],
    #     ["I1", "G2", 8],
    #     ["I1", "H2", 8],
    #     ["I1", "I2", 8],
    #     ["I1", "J2", 8],
    #     ["J1", "A2", 9],
    #     ["J1", "C2", 9],
    #     ["J1", "D2", 9],
    #     ["J1", "F2", 9],
    #     ["J1", "G2", 9],
    #     ["J1", "H2", 9],
    #     ["J1", "I2", 9],
    #     ["J1", "J2", 9]]

    # class Foo:
    #     def __init__(self, d, h, color):
    #         self.d = d
    #         self.h = h
    #         self.color = color

    #     # def __repr__(self):
    #     #     return 'x: ' + f'{self.d}' + ', ' + 'y: ' +f'{self.h}' + ', ' + 'color: ' + f'{self.color}'
    
    # for i in range(len(data)):
    #     data[i] = {Foo(data[i][0], data[i][1], data[i][2])}
        

    # print(data)
    return JsonResponse({'data': data}, safe=True)
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
    print(request)
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

data = [{x: "A1", y: "A2", color: 0},
{x: "A1", y: "B2", color: 1},
{x: "A1", y: "C2", color: 2},
{x: "A1", y: "D2", color: 3},
{x: "A1", y: "I2", color: 8},
{x: "A1", y: "J2", color: 9},
{x: "B1", y: "A2", color: 1},
{x: "B1", y: "B2", color: 1},
{x: "B1", y: "C2", color: 1},
{x: "B1", y: "D2", color: 1},
{x: "B1", y: "E2", color: 1},
{x: "B1", y: "F2", color: 1},
{x: "B1", y: "G2", color: 1},
{x: "B1", y: "H2", color: 1},
{x: "B1", y: "J2", color: 1},
{x: "C1", y: "A2", color: 2},
{x: "C1", y: "D2", color: 2},
{x: "C1", y: "E2", color: 2},
{x: "C1", y: "F2", color: 1},
{x: "C1", y: "G2", color: 2},
{x: "C1", y: "H2", color: 2},
{x: "C1", y: "I2", color: 2},
{x: "C1", y: "J2", color: 3},
{x: "D1", y: "C2", color: 3},
{x: "D1", y: "D2", color: 3},
{x: "D1", y: "G2", color: 1},
{x: "D1", y: "H2", color: 3},
{x: "D1", y: "I2", color: 1},
{x: "D1", y: "J2", color: 3},
{x: "E1", y: "A2", color: 4},
{x: "E1", y: "B2", color: 4},
{x: "E1", y: "D2", color: 4},
{x: "E1", y: "E2", color: 4},
{x: "E1", y: "G2", color: 4},
{x: "E1", y: "H2", color: 4},
{x: "E1", y: "I2", color: 4},
{x: "F1", y: "A2", color: 5},
{x: "F1", y: "B2", color: 5},
{x: "F1", y: "C2", color: 5},
{x: "F1", y: "D2", color: 5},
{x: "F1", y: "E2", color: 5},
{x: "F1", y: "F2", color: 5},
{x: "F1", y: "G2", color: 5},
{x: "F1", y: "H2", color: 5},
{x: "F1", y: "I2", color: 5},
{x: "F1", y: "J2", color: 5},
{x: "G1", y: "A2", color: 6},
{x: "G1", y: "C2", color: 6},
{x: "G1", y: "D2", color: 6},
{x: "G1", y: "G2", color: 6},
{x: "G1", y: "H2", color: 6},
{x: "G1", y: "I2", color: 6},
{x: "H1", y: "A2", color: 7},
{x: "H1", y: "C2", color: 7},
{x: "H1", y: "D2", color: 7},
{x: "H1", y: "E2", color: 7},
{x: "H1", y: "F2", color: 7},
{x: "H1", y: "G2", color: 7},
{x: "H1", y: "H2", color: 7},
{x: "H1", y: "J2", color: 7},
{x: "I1", y: "A2", color: 8},
{x: "I1", y: "C2", color: 8},
{x: "I1", y: "D2", color: 8},
{x: "I1", y: "E2", color: 8},
{x: "I1", y: "F2", color: 8},
{x: "I1", y: "G2", color: 8},
{x: "I1", y: "H2", color: 8},
{x: "I1", y: "I2", color: 8},
{x: "I1", y: "J2", color: 8},
{x: "J1", y: "A2", color: 9},
{x: "J1", y: "C2", color: 9},
{x: "J1", y: "D2", color: 9},
{x: "J1", y: "F2", color: 9},
{x: "J1", y: "G2", color: 9},
{x: "J1", y: "H2", color: 9},
{x: "J1", y: "I2", color: 9},
{x: "J1", y: "J2", color: 9}]
@csrf_exempt
@api_view(["GET"])
def show_map(request):
    return JsonResponse(data)
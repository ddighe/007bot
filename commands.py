import discord
import random
import time
import copy
tchannels = []
messages = []
players = []
Greet = ["Hello","Hey","Hi","Howdy","Yo","WHAZZUP","G'DAY"]
greet = ["hello","hey","hi","howdy","yo","whazzup","g'day"]






class comm(object):
    """docstring for comm"""
    def __init__(self, arg):
        super(comm, self).__init__()
        self.arg = arg
    async def test(message):
        if message.content == "$test":
            print("YAY")
    async def newchannel(message):
        if message.author.id not in players:
            players.append(message.author.id)
            await message.author.send("hello")
    async def assignments(client):
        random.shuffle(players)
        for i in range(0,len(players)-1):
            user = await client.fetch_user(players[i])
            print(user)
            tokill = await client.fetch_user(players[(i+1)%(len(players))])
            await user.send("Your assginment, if you choose to accept, is to inconspicuously kill "+ tokill)
            print(players[i],"buys for",players[(i+1)%(len(players))])



#gangs?
#people to trust (like the disable gifts for in secret santa)

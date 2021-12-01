import discord
import random
import time
tchannels = []
messages = []
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
			guild = message.guild
			nchannel = await guild.create_text_channel("{0.author.name}".format(message)+"'s terminal channel") 
			tchannels.append((nchannel.id, message.author.id))
			await nchannel.send("[{0.author.name}@".format(message)+message.guild.name+" **~**]$ ")


	async def terminals(message, channel):
		#create channel for only the message.author.id
		if (message.channel.id, message.author.id) in tchannels:
			if (message.content == "exit" or message.content == "stop"):
				await channel.delete()
		if(message.content.lower() == "f"):
			await message.add_reaction("🇫")
		if(message.content.lower() == "beep"):
			await message.channel.send("boop")
		#out of range beepboopbot
		for i in greet:
			if message.content.lower().startswith(i) or message.content.lower().endswith(i) or (" "+i+" ") in message.content.lower():
				a = await message.channel.send(Greet[random.randint(0,len(greet)-1)])
				await a.add_reaction("👋")

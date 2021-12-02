import discord
import random
import time
import os
import json
from commands import comm as com


tchannels = []

with open('../config.json') as f:
	config = json.load(f)
prefix = config['prefix']
token = config['token']
channel = 915264236941357066 


class MyClient(discord.Client):
	async def on_ready(self):
		print('Logged in as')
		print()
		print(self.user.id)
		print('------')
	async def on_message(self, message):
		
		
		async def voicechat(user):
			#if people in voicechannel
				#create text channel for only those in voice channel
			pass

		#adding messages to array
		
		# we do not want the bot to reply to itself
		if message.author.id == self.user.id:
			return
		else:
			#terminal code(checks to see if terminal)
			if message.channel.id == channel:
				#My exception
				if message.content == "$startx":
					await message.channel.send("**007 BOT ACTIVATED** Welcome {0.author.name}".format(message))
					await com.newchannel(message)
				if message.content=="startgame":
					await com.assignments(discord.Client)
				elif message.content.startswith("$"):
					#command()
					pass
					#for now
				#someone @s beepboopbot
				if message.content == '<@!915265523015643196>':
					await message.channel.send("WHAT DO YOU WANT {0.author.mention}".format(message))

client = MyClient()
client.run(token)



#regex




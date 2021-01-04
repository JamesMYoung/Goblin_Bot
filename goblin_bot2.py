#!/usr/bin/env python3.6
# https://github.com/Rapptz/discord.py/blob/async/examples/reply.py
import discord
import subprocess
import os.path
import random
import re
import json
import requests
import Levenshtein
import asyncio

from roll_bot import roll_goblin
from help_bot import help_goblin
from spell_lookup_bot import spell_lookup_goblin
from misc_bot import misc_goblin
from health_bot import health_goblin
from init_bot import init_goblin
from enemy_bot import enemy_goblin
from char_bot import char_goblin

from goblin_util import select_best


#if not discord.opus.is_loaded():
#	 # the 'opus' library here is opus.dll on windows
#	 # or libopus.so on linux in the current directory
#	 # you should replace this with the location the
#	 # opus library is located in and with the proper filename.
#	 # note that on windows this DLL is automatically provided for you
#	 discord.opus.load_opus('opus')


TOKEN = 'NTA2MzI2NzAyNDk0ODQyODgw.DrgqiA.DCiQQX5Ak5RZ_rOlB4teK8U-HKU'

client = discord.Client()

@client.event
async def on_message(message):
	channel = message.channel
	text = message.content.split()
	audio_lock = False
	# we do not want the bot to reply to itself
	if message.author == client.user:
		return
	print("message author:" + message.author.name)
	
		
	print("input text: ", text)
	print("input length", len(text))
	msg = ''
	
	if len(text) == 0:
		print('empty message / media')
	
	elif text[0] == '!G' or text[0] == '!G!':
		if text[0] == '!G!':
			# working here, need to read in string and then resplit text
			if input_history.get(message.author) == None:
				msg = 'No input history found for user'
				await channel.send(msg)
				return
			else:
				text = input_history[message.author].split()
				message.content = input_history[message.author]
	
		if text[1] == 'give' or 'take' or 'uwu' or 'fortune' or 'starwars' or 'cryptography':
			msg = Misc_Goblin.create_output(text)
		if text[1] == 'help':
			msg = Help_Goblin.create_output(text)
		if text[1] == 'roll':
			msg = Roll_Goblin.create_output(text)
			if msg == ':thinking:':
				pass
			else:
				msg = '```' + message.author.nick + ' rolled: \n' + msg[3:]
		if text[1] == 'lookup':
			msg = Spell_Lookup_Goblin.create_output(text)
		if text[1] == 'health':
			msg = Health_Goblin.create_output(text)
		if text[1] == 'init':
			msg = Init_Goblin.create_output(text)
		if text[1] == 'enemy':
			msg = Enemy_Goblin.create_output(text)
		if text[1] == 'char':
			msg = Char_Goblin.create_output(text)
			
		# Super handy for testing things on-line
		if text[1] == 'test':
			msg = test(text)
			
			
		#if text[1] == 'parse':
		#	 input_str = ''.join(text[2:])
		#	 msg = goblin_handle(input_str)

		#await client.send_message(message.channel, msg)
		
		input_history[message.author] = message.content
		try:
			await channel.send(msg)
		except:
			print("Error sending msg: \"" + msg + "\"")
			
	elif text[0] == '!Gflip':
		msg = '```The impartial goblin flips a coin and gets '
		if(random.randrange(0, 1) == 0):
			msg += "<heads>"
		else:
			msg += "<tails>"
		msg += ' as the result.```'
		await channel.send(msg)
	elif text[0] == '!G4':
		msg = message.author.name + " rolled a: "
		rand_num = str(random.randrange(1, 5))
		msg += rand_num
		if rand_num == '4':
			msg = '**' + str(msg) + '**' 
		await channel.send(msg)
	elif text[0] == '!G6':
		msg = message.author.name + " rolled a: "
		rand_num = str(random.randrange(1, 7))
		msg += rand_num
		if rand_num == '6':
			msg = '**' + str(msg) + '**' 
		await channel.send(msg)
	elif text[0] == '!G8':
		msg = message.author.name + " rolled a: "
		rand_num = str(random.randrange(1, 9))
		msg += rand_num
		if rand_num == '8':
			msg = '**' + str(msg) + '**' 
		await channel.send(msg)
	elif text[0] == '!G10':
		msg = message.author.name + " rolled a: "
		rand_num = str(random.randrange(1, 11))
		msg += rand_num
		if rand_num == '10':
			msg = '**' + str(msg) + '**' 
		await channel.send(msg)
	elif text[0] == '!G12':
		msg = message.author.name + " rolled a: "
		rand_num = str(random.randrange(1, 13))
		msg += rand_num
		if rand_num == '12':
			msg = '**' + str(msg) + '**' 
		await channel.send(msg)
	elif text[0] == '!G20':
		msg = message.author.name + " rolled a: "
		rand_num = str(random.randrange(1, 21))
		msg += rand_num
		if rand_num == '20':
			msg = '**' + str(msg) + '**' 
		await channel.send(msg)
	elif text[0] == '!G100':
		msg = message.author.name + " rolled a: "
		rand_num = str(random.randrange(1, 101))
		msg += rand_num
		if rand_num == '100':
			msg = '**' + str(msg) + '**' 
		await channel.send(msg)
	elif text[0] == 'sleep' and text[1] == 'tite' and text[2] == 'goblin' and message.author.name == "Xelasari":
		msg = "All in a day's work"
		await channel.send(msg)
		await client.logout()
		
	else:
		return
	
		
#def roll_range(x, y):
#	 #msg = message.author.name + " rolled a: "
#	 msg += str(random.randrange(x, y))
#	 if msg == '20':
#		 msg = '**' + str(msg) + '**' 
#	 #await client.send_message(message.channel, msg)
	
def test(text):
	#skill_keywords = [
	#"athletics", "acrobatics", "sleight_of_hand",
	#"stealth", "arcana", "history", "investigation",
	#"nature", "religion", "animal_handling",
	#"insight", "medicine", "perception", "survival",
	#"deception", "intimidation", "performance",
	#"persuasion"
	#]
	#
	#core_keywords = [
	#"strength", "dexterity", "constitution",
	#"intelligence", "wisdom", "charisma"		 
	#]
	
	char_list = []
	character1 = {}
	character2 = {}
	character3 = {}
	character1['name'] = 'Joe'
	character1['level'] = '10'
	char_list.append(character1)
	character2['name'] = 'Tim'
	character2['level'] = '21'
	char_list.append(character2)
	character3['name'] = 'Garm'
	character3['level'] = '20'
	char_list.append(character3)
	
	c_ptr = None
	
	for character in char_list:
		if character['name'] == text[2]:
			c_ptr = character
	
	
	msg = 'level: ' + str(c_ptr['level']) + '\n'
	c_ptr['level'] = -1
	msg += 'new level: ' + str(char_list[0]['level']) + '\n'
	msg += 'new level: ' + str(char_list[1]['level']) + '\n'
	msg += 'new level: ' + str(char_list[2]['level']) + '\n'
	
	#msg, best_keyword = select_best(skill_keywords, text[2])
	
	#msg = 'finished'
	
	return msg

async def update_presence_loop():
	#sec_count = 0
	await asyncio.sleep(30)
	while(True):

		#if sec_count == 30:
		#	sec_count = 0
		print("Changing Game Message...")
		game = discord.Game(random.choice(idle_messages))
		await client.change_presence(activity=game)
		
		#sec_count += 1
		await asyncio.sleep(30)
		
	
@client.event
async def on_ready():
	print('Logged in as')
	print(client.user.name)
	print(client.user.id)
	print('------')
	
	#act = discord.CustomActivity("Searching for Gold")
	game = discord.Game("Searching for Gold")
	await client.change_presence(activity=game)
	global Roll_Goblin 
	Roll_Goblin = roll_goblin()
	global Help_Goblin 
	Help_Goblin = help_goblin()
	global Spell_Lookup_Goblin 
	Spell_Lookup_Goblin = spell_lookup_goblin()
	global Misc_Goblin 
	Misc_Goblin = misc_goblin()
	global Health_Goblin
	Health_Goblin = health_goblin()
	global Init_Goblin
	Init_Goblin = init_goblin()
	global Enemy_Goblin
	Enemy_Goblin = enemy_goblin()
	global Char_Goblin
	Char_Goblin = char_goblin()
	
	global input_history
	input_history = {}
	global idle_messages
	idle_messages = [
		"Searching for Gold",
		"Digging for Gems",
		"Using Turbo Intellect",
		"Programming at Home",
		"Counting Gold"
		]

	print("--Finished Setup--")

def startup():
	client.loop.create_task(update_presence_loop())
	client.run(TOKEN)
	
if __name__ == "__main__":
	client.loop.create_task(update_presence_loop())
	client.run(TOKEN)
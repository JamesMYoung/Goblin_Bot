#!/usr/bin/env python3.5
# https://github.com/Rapptz/discord.py/blob/async/examples/reply.py
import discord
import subprocess
import os.path
import random
import re
import json
import requests

from roll_bot import roll_goblin
from help_bot import help_goblin
from spell_lookup_bot import spell_lookup_goblin
from misc_bot import misc_goblin
from health_bot import health_goblin

if not discord.opus.is_loaded():
    # the 'opus' library here is opus.dll on windows
    # or libopus.so on linux in the current directory
    # you should replace this with the location the
    # opus library is located in and with the proper filename.
    # note that on windows this DLL is automatically provided for you
    discord.opus.load_opus('opus')


TOKEN = 'NTA2MzI2NzAyNDk0ODQyODgw.DrgqiA.DCiQQX5Ak5RZ_rOlB4teK8U-HKU'

client = discord.Client()

@client.event
async def on_message(message):

    text = message.content.split()
    # we do not want the bot to reply to itself
    audio_lock = False
    if message.author == client.user:
        return
    print("message author:" + message.author.name)
    
        
    print("input text:", text)
    msg = ''
    if text[0] == '!G':
        if text[1] == 'give' or 'take' or 'uwu':
            msg = Misc_Goblin.create_output(text)
        if text[1] == 'help':
            msg = Help_Goblin.create_output(text)
        if text[1] == 'roll':
            msg = Roll_Goblin.create_output(text)
        if text[1] == 'lookup':
            msg = Spell_Lookup_Goblin.create_output(text)
        if text[1] == 'health':
            msg = Health_Goblin.create_output(text)
            
        await client.send_message(message.channel, msg)
    elif text[0] == '!Gflip':
        msg = '```The impartial goblin flips a coin and gets '
        if(random.randrange(0, 1) == 0):
            msg += "<heads>"
        else:
            msg += "<tails>"
        msg += ' as the result.```'
        await client.send_message(message.channel, msg)
    elif text[0] == '!G4':
        msg = message.author.name + " rolled a: "
        rand_num = str(random.randrange(1, 5))
        msg += rand_num
        if rand_num == '4':
            msg = '**' + str(msg) + '**' 
        await client.send_message(message.channel, msg)
    elif text[0] == '!G6':
        msg = message.author.name + " rolled a: "
        rand_num = str(random.randrange(1, 7))
        msg += rand_num
        if rand_num == '6':
            msg = '**' + str(msg) + '**' 
        await client.send_message(message.channel, msg)
    elif text[0] == '!G8':
        msg = message.author.name + " rolled a: "
        rand_num = str(random.randrange(1, 9))
        msg += rand_num
        if rand_num == '8':
            msg = '**' + str(msg) + '**' 
        await client.send_message(message.channel, msg)
    elif text[0] == '!G10':
        msg = message.author.name + " rolled a: "
        rand_num = str(random.randrange(1, 11))
        msg += rand_num
        if rand_num == '10':
            msg = '**' + str(msg) + '**' 
        await client.send_message(message.channel, msg)
    elif text[0] == '!G12':
        msg = message.author.name + " rolled a: "
        rand_num = str(random.randrange(1, 13))
        msg += rand_num
        if rand_num == '12':
            msg = '**' + str(msg) + '**' 
        await client.send_message(message.channel, msg)
    elif text[0] == '!G20':
        msg = message.author.name + " rolled a: "
        rand_num = str(random.randrange(1, 21))
        msg += rand_num
        if rand_num == '20':
            msg = '**' + str(msg) + '**' 
        await client.send_message(message.channel, msg)
    elif text[0] == '!G100':
        msg = message.author.name + " rolled a: "
        rand_num = str(random.randrange(1, 101))
        msg += rand_num
        if rand_num == '100':
            msg = '**' + str(msg) + '**' 
        await client.send_message(message.channel, msg)
    elif text[0] == 'sleep' and text[1] == 'tite' and text[2] == 'goblin' and message.author.name == "Xelasari":
        msg = "All in a day's work"
        await client.send_message(message.channel, msg)
        await client.logout()
        
    else:
        return
    
        
#def roll_range(x, y):
#    #msg = message.author.name + " rolled a: "
#    msg += str(random.randrange(x, y))
#    if msg == '20':
#        msg = '**' + str(msg) + '**' 
#    #await client.send_message(message.channel, msg)
    
    
@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    game = discord.Game(name="Searching for Gold")
    await client.change_presence(game=game)
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

client.run(TOKEN)
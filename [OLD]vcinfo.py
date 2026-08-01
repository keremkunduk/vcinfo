import discord
from discord import option
import asyncio
import random
from datetime import datetime
from datetime import date
from tkinter import *
from time import sleep as sl

client = discord.Bot()

guild_id = None # guild id comes here

global font 
font = 'Reddit Sans'
my_username = None # your discord tag comes here(not in the server, your main username on discord)

@client.event
async def on_ready():
    print("Ready\n")
    global guild
    guild = client.get_guild(guild_id)

@client.event
async def on_voice_state_update(member, before, after):
    today = str(date.today())
    output = None
    situation = '' #None
    am_i_here = False

    ch_name = str(after.channel)
    ch = after.channel
    if ch == None:
        ch = before.channel
    
    now = datetime.now()

    current_time = now.strftime("%H:%M:%S")

#DELETE THIS-----------------------------

    if after.self_stream:
        situation = ' On Stream'
    elif before.self_stream:
        situation = ' Off Stream'
    if after.self_mute:
        situation = ' Muted'
    elif before.self_mute:
        situation = ' Unmuted'
    if after.self_deaf:
        situation = ' Deafen'
    elif before.self_deaf:
        situation = ' Undeafen'

    # if after.self_mute:
    #     situation = ' Muted'
    # elif before.self_mute:
    #     situation = ' Unmuted'
    # if after.self_deaf:
    #     situation = ' Deafen'
    # elif before.self_deaf:
    #     situation = ' Undeafen'
    # if after.self_stream:
    #     situation = ' On Stream'
    # elif before.self_stream:
    #     situation = ' Off Stream'

#-----------------------------------------

#IS KEREMK HERE

    for i in ch.members:
        if i.name == my_username and member.name != my_username:
            am_i_here = True
    

    if not before.channel:
        output = str(member.name) + f' | Joined {ch_name}{situation}' + ' | ' + current_time + ' | ' + today

        if am_i_here:
            root = Tk()
            root.geometry("+0+0")
            root.overrideredirect(True)
            root.wm_attributes("-topmost", True)
            root.wm_attributes("-alpha", 0.01)
            root.resizable(0, 0)
            root.wm_attributes('-alpha', 0.7)
            display = Label(root, font=(font, 24, 'bold'), bg='black')
            display.config(text=f'{member.name} Joined', fg='cyan')
            display.pack()
            root.update()
            sl(2)
            root.destroy()
            root.update()

    if before.channel and after.channel:
        if str(before.channel) != str(ch_name): #if channels are same, then member didn't changed his channel, changed situation
            output = str(member.name) + f' | {before.channel} -> {ch_name}{situation}' + ' | ' + current_time + ' | ' + today

            for i in before.channel.members:
                if i.name == 'keremkunduk' and member.name != 'keremkunduk':
                    am_i_here = True

            if am_i_here:
                root = Tk()
                root.geometry("+0+0")
                root.overrideredirect(True)
                root.wm_attributes("-topmost", True)
                root.wm_attributes("-alpha", 0.01)
                root.resizable(0, 0)
                root.wm_attributes('-alpha', 0.7)
                display = Label(root, font=(font, 24, 'bold'), bg='black')
                # display.config(text=f'{member.name} {before.channel} -> {ch_name}', fg='cyan')
                display.config(text=f'{member.name} -> {ch_name}', fg='cyan')
                display.pack()
                root.update()
                sl(2)
                root.destroy()
                root.update()

        # elif after.self_mute:
            # situation = ' Muted'
        # elif before.self_mute:
            # situation = ' Unmuted'
        # if after.self_deaf:
            # situation = ' Deafen'
        # elif before.self_deaf:
            # situation = ' Undeafen'
        # if after.self_stream:
            # situation = ' On Stream'
        # elif before.self_stream:
            # situation = ' Off Stream'
    if before.channel and not after.channel:
        output = str(member.name) + f' | Left {before.channel}{situation}' + ' | ' + current_time + ' | ' + today #ch_name

        if am_i_here:
            root = Tk()
            root.geometry("+0+0")
            root.overrideredirect(True)
            root.wm_attributes("-topmost", True)
            root.wm_attributes("-alpha", 0.01)
            root.resizable(0, 0)
            root.wm_attributes('-alpha', 0.7)
            display = Label(root, font=(font, 24, 'bold'), bg='black')
            display.config(text=f'{member.name} Left', fg='cyan')
            display.pack()
            root.update()
            sl(2)
            root.destroy()
            root.update()

    if output == None:
        output = str(member.name) + ' |' + str(situation) + ' | ' + current_time + ' | ' + today
        if 'Stream' in situation or 'eafen' in situation:
            if am_i_here:
                root = Tk()
                root.geometry("+0+0")
                root.overrideredirect(True)
                root.wm_attributes("-topmost", True)
                root.wm_attributes("-alpha", 0.01)
                root.resizable(0, 0)
                root.wm_attributes('-alpha', 0.7)
                display = Label(root, font=(font, 24, 'bold'), bg='black')
                display.config(text=f'{member.name}{situation}', fg='cyan')
                display.pack()
                root.update()
                sl(2)
                root.destroy()
                root.update()
    
    print(output)
    op = open('vclog.txt', 'a', encoding='utf-8')
    op.write(output + '\n')
    op.close
        

client.run('')

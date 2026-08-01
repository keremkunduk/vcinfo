import discord
from discord import option
from datetime import datetime
from datetime import date
from tkinter import *
from time import sleep as sl
import requests
import ctypes


#----------------------------------
guild_id = None
your_discord_name = None
send_anyways = False #if you want to get notifications even if you are not connected, make it True
token = None

global font 
font = 'Reddit Sans' # i think it is both readable and look great but you need to download it. Your choice


#----------------------------------

GWL_EXSTYLE = -20
WS_EX_LAYERED = 0x00080000
WS_EX_TRANSPARENT = 0x00000020
WS_EX_NOACTIVATE = 0x08000000


url = "https://www.google.com.tr/?hl=tr"
timeout = 5

while True:
    try:
        request = requests.get(url, timeout=timeout)
        break
        #print("Connected to the Internet")
    except (requests.ConnectionError, requests.Timeout) as exception:
        pass
        sl(10)


client = discord.Bot()

global deffg
global deftext
global notify

def notify(deftext, deffg):
    root = Tk()
    root.geometry("+0+0")
    root.overrideredirect(True)
    root.wm_attributes("-topmost", True)
    root.wm_attributes("-alpha", 0.01)
    root.resizable(0, 0)
    root.wm_attributes('-alpha', 0.7)
    display = Label(root, font=(font, 24, 'bold'), bg='black')
    display.config(text=deftext, fg=deffg)
    display.pack()
    
    
    # Tkinter penceresinin Windows üzerindeki benzersiz kimliğini (HWND) alıyoruz
    hwnd = ctypes.windll.user32.GetParent(root.winfo_id())
    
    # Mevcut pencere stilini alıyoruz
    current_style = ctypes.windll.user32.GetWindowLongW(hwnd, GWL_EXSTYLE)
    
    # Saydamlık, tıklanamazlık ve odaklanamazlık özelliklerini birleştiriyoruz
    new_style = current_style | WS_EX_LAYERED | WS_EX_NOACTIVATE
    
    # Yeni stili pencereye giydiriyoruz
    ctypes.windll.user32.SetWindowLongW(hwnd, GWL_EXSTYLE, new_style)
    
    
    
    root.update()
    sl(2)
    root.destroy()
    root.update()




@client.event
async def on_ready():
    print("Ready\n")
    global guild
    guild = client.get_guild(guild_id)

@client.event
async def on_voice_state_update(member, before, after):
    global send_anyways
    
    try:
        send_anyways
    except:
        send_anyways = False

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

#DELETE THIS----------------------------- (((((idk why i added this but probably it is not necessary to remove)))))

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

#AM I HERE

    for i in ch.members:
        if i.name == your_discord_name and member.name != your_discord_name:
            am_i_here = True

    if not before.channel:
        output = str(member.name) + f' | Joined {ch_name}{situation}' + ' | ' + current_time + ' | ' + today

        if am_i_here or send_anyways and member.name != your_discord_name:
            if am_i_here:
                notify(f'{member.name} Joined', 'cyan')
            else:
                notify(f'{member.name} Joined {ch_name}', 'cyan')


    if before.channel and after.channel:
        if str(before.channel) != str(ch_name): #if channels are same, then member didn't changed his channel, changed situation
            output = str(member.name) + f' | {before.channel} -> {ch_name}{situation}' + ' | ' + current_time + ' | ' + today

            for i in before.channel.members:
                if i.name == your_discord_name and member.name != your_discord_name:
                    am_i_here = True

            if am_i_here:
                notify(f'{member.name} -> {ch_name}', 'cyan')


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

        if am_i_here or send_anyways and member.name != your_discord_name:

            if am_i_here:
                notify(f'{member.name} Left', 'cyan')
            else:
                notify(f'{member.name} Left {str(before.channel)}', 'cyan')
            

    if output == None:
        output = str(member.name) + ' |' + str(situation) + ' | ' + current_time + ' | ' + today
        if 'Stream' in situation or 'eafen' in situation:
            if am_i_here or send_anyways and member.name != your_discord_name:
                if 'Stream' in situation or am_i_here:
                    notify(f'{member.name}{situation}', 'cyan')

    
    print(output)
    op = open('vclog.txt', 'a', encoding='utf-8')
    op.write(output + '\n')
    op.close
    
    # if not before.channel and after.channel:
    #     kanalid = 1063747294215815230

    #     channel = client.get_channel(kanalid)
    #     members = channel.members
    #     if members != []:
    #         for x in members:
    #             if x.id == member.id:
    #                 print(f'{member} Bağlandı')
    #             else:
    #                 print(f'{member} Ayrıldı')
    #     else:
    #         print(f'{member} Ayrıldı')               

client.run(token)

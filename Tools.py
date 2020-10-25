

##### Currently has 1 features

##### 2. Invite grabber - binary converter 


import discord
from discord.ext import commands
from bs4 import BeautifulSoup
import requests
import re

mainbot = commands.Bot(command_prefix = "-")

channel_id = 717262662215532620

test_channel = 688447908613324867 ### Test 



######## Invite grabber 
@mainbot.command()
@commands.guild_only()
async def i(ctx,*,message):
    message = str(message).replace(" ","")
    message = re.sub("[^A-Za-z0-9]+","",message)
     
    await ctx.send("https://discord.gg/" + message)


########## Binary converter 
@mainbot.command()
@commands.guild_only()
async def b(ctx,*,message):


    binary_values = message.split()

    ascii_string = ""
    for binary_value in binary_values:
        an_integer = int(binary_value, 2)
        ascii_character = chr(an_integer)
        ascii_string += ascii_character
        ascii_string = str(ascii_string).replace(" ","")
        ascii_string = ascii_string.replace("https://discord.gg/"," ")
        
    await ctx.send("https://discord.gg/" + ascii_string)

    
token_RR = "NzA4MDAxODIwMTQ3OTc0MTk0.XvfcKA.ANFu-wYyHaNrRn57627-3JMuAyY"
token_test = "NzE0MDgzODU1MjU0MDI4MzA4.XvfNRg.aWHB5hzC2vd0gvsgJEhvHhzDWfY"


mainbot.run(token_RR)

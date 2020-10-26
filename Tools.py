

##### Currently has 1 features

##### 2. Invite grabber - binary converter 


import discord
from discord.ext import commands
from bs4 import BeautifulSoup
import requests
import re

mainbot = commands.Bot(command_prefix = "-")

mainbot.remove_command("help")

channel_id = 717262662215532620

test_channel = 688447908613324867 ### Test 



######## Invite grabber 
@mainbot.command()
@commands.guild_only()
async def i(ctx,*,message):
    message = str(message).replace(" ","").replace("https://discord.gg/","")
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


help_message = """
```
1) -i 
* Removes Whitespace 
* Removes symbols 
* Removes the ' https://discord.gg/ ' if its accidentally put in the code after -i so there is no duplicate. 

2) -b 
* converts binary to text and automatically puts it into a discord invite form for users to join
* Removes the ' https://discord.gg/ ' if its accidentally put in the code after -i so there is no duplicate.
```
"""

@mainbot.command()
async def help(ctx):

    await ctx.send(help_message)


        
token_RR = "NzA4MDAxODIwMTQ3OTc0MTk0.XvfcKA.ANFu-wYyHaNrRn57627-3JMuAyY"
token_test = "NzE0MDgzODU1MjU0MDI4MzA4.XvfNRg.aWHB5hzC2vd0gvsgJEhvHhzDWfY"


mainbot.run(token_RR)



##### Currently has 2 features

##### 1. Botbroker prices

##### 2. Invite grabber - binary converter 


import discord
from discord.ext import commands
from bs4 import BeautifulSoup
import requests
import re

mainbot = commands.Bot(command_prefix = "-")

channel_id = 717262662215532620

test_channel = 688447908613324867 ### Test 


class BotBroker():
    def __init__(self,url,thumbnail,bid_page):

        self.url = url 
        self.thumbnail = thumbnail
        self.bid_page = bid_page

        """
        Some bots do not sell lifetime so there is two functions.
        
        Only difference is that embed add fields 
        
        """

    def no_lifetime(self):

        r = requests.get(self.url)
        soup = BeautifulSoup(r.content,'html.parser')

        price1 = soup.findAll("a", {"class": "btn btn-light font-weight-bold text-left pl-md-4 btn-block"})
        price1 = str(price1).split()
        price1 = price1[8]  

        price2 = soup.findAll("a", {"class": "btn btn-light font-weight-bold btn-block pl-md-4 text-left"})
        price2 = str(price2).split()
        price2 = price2[8]  

        """
        Last three prices of the bot,
        including if its lifetime or renewal

        """

        last_price = soup.findAll("span",{"font-weight-bold"})
        last_price = str(last_price)
        last_price = re.findall("[$]+\d+",last_price)


        """
        Was it a renewal or a lifetime sale of the bot
        """

        sale_type = soup.findAll("div",{"class": "card-body border-transparent shadow-light bg-light mt-3 pt-3 pb-3 pl-4 pr-4"},"small")
        sale_type = str(sale_type)
        sale_type = re.findall(r"\bRenewal\b|\bLifetime\b",sale_type)

        """
        The time the user purchased the bot / group 
        """

        date_purchase = soup.findAll("span",{"class": "text-right pull-right mt-1"})
        date_purchase = str(date_purchase).replace('<span class="text-right pull-right mt-1">',"").replace("</span>","").replace(",","").replace('<i class="fas fa-clock ml-1"></i>',"").replace("[","").replace("]","").splitlines()



        embed = discord.Embed(title = "**BotBroker prices**", description = f"[Page Link]({self.url}) | [Twitter](https://twitter.com/BotBroker) | [Place a bid]({self.bid_page})")
        embed.set_author(name= "Botbroker", icon_url="https://pbs.twimg.com/profile_images/1202325425466134528/bQyROCKB_400x400.jpg")
        embed.add_field(name='**Lowest Ask (renewal)**', value="```" + price1 + "```")
        embed.add_field(name='**Highest Bid (renewal)**', value="```" + price2 + "```",inline=True)
        embed.add_field(name='**Last 3 sales**',value=f"```{last_price[0]} {sale_type[0]} - {date_purchase[1].strip()} ago\n{last_price[1]} {sale_type[1]} - {date_purchase[3].strip()} ago \n{last_price[2]} {sale_type[2]} - {date_purchase[5].strip()} ago```",inline=False)
        embed.set_thumbnail(url= self.thumbnail)
        return embed

    def lifetime(self):
        r = requests.get(self.url)
        soup = BeautifulSoup(r.content,'html.parser')

        price1 = soup.findAll("a", {"class": "btn btn-light font-weight-bold text-left pl-md-4 btn-block"})
        price1 = str(price1).split()
        price1 = price1[8]

        price2 = soup.findAll("a", {"class": "btn btn-light font-weight-bold btn-block pl-md-4 text-left"})
        price2 = str(price2).split()
        price2 = price2[8]

        """
        Last three sales of the bot.
        Including lifetime and renewal sale

        """

        last_price = soup.findAll("span",{"font-weight-bold"})
        last_price = str(last_price)
        last_price = re.findall("[$]+\d+",last_price)


        """
        Was it a renewal or a lifetime sale of the bot
        """
        sale_type = soup.findAll("div",{"class": "card-body border-transparent shadow-light bg-light mt-3 pt-3 pb-3 pl-4 pr-4"},"small")
        sale_type = str(sale_type)
        sale_type = re.findall(r"\bRenewal\b|\bLifetime\b",sale_type)

        """
        The time the user purchased the bot / group 
        """

        date_purchase = soup.findAll("span",{"class": "text-right pull-right mt-1"})
        date_purchase = str(date_purchase).replace('<span class="text-right pull-right mt-1">',"").replace("</span>","").replace(",","").replace('<i class="fas fa-clock ml-1"></i>',"").replace("[","").replace("]","").splitlines()


        embed = discord.Embed(title = "**BotBroker prices**", description = f"[Page Link]({self.url}) | [Twitter](https://twitter.com/BotBroker) | [Place a bid]({self.bid_page})")
        embed.set_author(name= "Botbroker", icon_url="https://pbs.twimg.com/profile_images/1202325425466134528/bQyROCKB_400x400.jpg")
        embed.add_field(name='**Lowest Ask (renewal)**', value="```" + price1 + "```")
        embed.add_field(name='**Highest Bid (lifetime)**', value="```" + price2 + "```",inline=True)
        embed.add_field(name='**Last 3 sales**',value=f"```{last_price[0]} {sale_type[0]} - {date_purchase[1].strip()} ago\n{last_price[1]} {sale_type[1]} - {date_purchase[3].strip()} ago \n{last_price[2]} {sale_type[2]} - {date_purchase[5].strip()} ago```",inline=False)
        embed.set_thumbnail(url=self.thumbnail)
        return embed




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

#############################################################################
####### >>>>>>>>>>>>>>>>>>>>>>>>>>  Bots  <<<<<<<<<<<<<<<<<<<<<<<<<< ########
#############################################################################

@mainbot.command(aliases=["splash","force","Splashforce","SplashForce","splashForce"])
@commands.guild_only()
async def splashforce(ctx):
    splashforce_post = BotBroker("https://botbroker.io/products/splashforce","https://i.imgur.com/br7M061.png","https://botbroker.io/bids/new/splashforce").no_lifetime()
    
    channel = mainbot.get_channel(channel_id)
    if channel.id == channel_id:

        await channel.send(embed = splashforce_post)



@mainbot.command(aliases=["Polaris"])
@commands.guild_only()
async def polaris(ctx):
    polaris_post = BotBroker("https://botbroker.io/products/polaris","https://res.cloudinary.com/dcbenpm7u/image/twitter_name/w_600/polarisaio.jpg","https://botbroker.io/bids/new/polaris").no_lifetime()

    channel = mainbot.get_channel(channel_id)
    if channel.id == channel_id:

        await channel.send(embed = polaris_post)

@mainbot.command(aliases=["Balko","BalkoBot","Balkobot","balkoBot","balkobot"])
@commands.guild_only()
async def balko(ctx):
    balko_post = BotBroker("https://botbroker.io/products/balko","https://i.imgur.com/InY7MMU.png","https://botbroker.io/bids/new/balko").lifetime()

    channel = mainbot.get_channel(channel_id)
    if channel.id == channel_id:

        await channel.send(embed = balko_post)

@mainbot.command(aliases=["Phantom"])
@commands.guild_only()
async def phantom(ctx):
    phantom_post = BotBroker("https://botbroker.io/products/phantom","https://i.imgur.com/8satPLU.png","https://botbroker.io/bids/new/phantom").lifetime()

    channel = mainbot.get_channel(channel_id)
    if channel.id == channel_id:

        await channel.send(embed = phantom_post)

@mainbot.command(aliases=["Dashe"])
@commands.guild_only()
async def dashe(ctx):
    dashe_post = BotBroker("https://botbroker.io/products/dashe","https://i.imgur.com/CV6MWXM.png","https://botbroker.io/bids/new/dashe").lifetime()

    channel = mainbot.get_channel(channel_id)
    if channel.id == channel_id:

        await channel.send(embed = dashe_post)

@mainbot.command(aliases=["Cyber"])
@commands.guild_only()
async def cyber(ctx):
    cyber_post = BotBroker("https://botbroker.io/products/cyber-aio","https://i.imgur.com/cvdVKqb.png","https://botbroker.io/bids/new/cyber-aio").lifetime()

    channel = mainbot.get_channel(channel_id)
    if channel.id == channel_id:

        await channel.send(embed = cyber_post)


@mainbot.command(aliases=["PD","pD","Pd","Project destoyer","project destoryer","project Destroyer","Project Destroyer"])
@commands.guild_only()
async def pd(ctx):
    pd_post = BotBroker("https://botbroker.io/products/project-destroyer","https://i.imgur.com/pF9aUGu.png","https://botbroker.io/bids/new/project-destroyer").lifetime()

    channel = mainbot.get_channel(channel_id)
    if channel.id == channel_id:

        await channel.send(embed = pd_post)


@mainbot.command(aliases=["Wrath"])
@commands.guild_only()
async def wrath(ctx):
    wrath_post = BotBroker("https://botbroker.io/products/wrath","https://i.imgur.com/2vkT90s.png","https://botbroker.io/bids/new/wrath").lifetime()

    channel = mainbot.get_channel(channel_id)
    if channel.id == channel_id:

        await channel.send(embed = wrath_post)


@mainbot.command(aliases=["Prism","PrismAIO","Prismaio","prismaio","prismAIO"])
@commands.guild_only()
async def prism(ctx):
    prism_post = BotBroker("https://botbroker.io/products/prism","https://i.imgur.com/NxL1ajE.png","https://botbroker.io/bids/new/prism").no_lifetime()

    channel = mainbot.get_channel(channel_id)
    if channel.id == channel_id:

        await channel.send(embed = prism_post)


@mainbot.command(aliases=["Mek","Mekpreme","MekPreme","mekpreme","mekPreme"])
@commands.guild_only()
async def mek(ctx):
    mek_post = BotBroker("https://botbroker.io/products/mekpreme","https://i.imgur.com/fcFl3u7.png","https://botbroker.io/bids/new/mekpreme").lifetime()

    channel = mainbot.get_channel(channel_id)
    if channel.id == channel_id:

        await channel.send(embed = mek_post)

@mainbot.command(aliases=["Adept"])
@commands.guild_only()
async def adept(ctx):
    adept_post = BotBroker("https://botbroker.io/products/adept-supreme","https://i.imgur.com/vFTqsqa.png","https://botbroker.io/bids/new/adept_supreme").lifetime()

    channel = mainbot.get_channel(channel_id)
    if channel.id == channel_id:

        await channel.send(embed = adept_post)

@mainbot.command(aliases=["Velox","Veloxpreme","VeloxPreme"])
@commands.guild_only()
async def velox(ctx):
    velox_post = BotBroker("https://botbroker.io/products/velox","https://i.imgur.com/dmKhHKd.jpg","https://botbroker.io/bids/new/velox").lifetime()

    channel = mainbot.get_channel(channel_id)
    if channel.id == channel_id:

        await channel.send(embed = velox_post)


@mainbot.command(aliases=["Scott","ScottBot","Scottbot","scottbot","scottBot"])
@commands.guild_only()
async def scott(ctx):
    scott_post = BotBroker("https://botbroker.io/products/scottbot","https://res.cloudinary.com/dklrin11o/image/twitter_name/w_600/scottbotv1.jpg","https://botbroker.io/bids/new/scottbot").no_lifetime()

    channel = mainbot.get_channel(channel_id)
    if channel.id == channel_id:

        await channel.send(embed = scott_post)


@mainbot.command(aliases=["Tohru","Tohruaio","TohruAIO","tohruaio"])
@commands.guild_only()
async def tohru(ctx):
    tohru_post = BotBroker("https://botbroker.io/products/tohruaio","https://res.cloudinary.com/dcbenpm7u/image/twitter_name/w_600/tohruaio.jpg","https://botbroker.io/bids/new/tohruaio").no_lifetime()

    channel = mainbot.get_channel(channel_id)
    if channel.id == channel_id:

        await channel.send(embed = tohru_post)

@mainbot.command(aliases=["Swift","SwiftAIO","Swiftaio","swiftAIO","swiftaio"])
@commands.guild_only()
async def swift(ctx):
    swift_post = BotBroker("https://botbroker.io/products/swftaio","https://i.imgur.com/RQYnXeq.png","https://botbroker.io/bids/new/swiftaio").no_lifetime()

    channel = mainbot.get_channel(channel_id)
    if channel.id == channel_id:

        await channel.send(embed = swift_post)



#############################################################################
####### >>>>>>>>>>>>>>>>>>>>>>>>>  Groups  <<<<<<<<<<<<<<<<<<<<<<<<< ########
#############################################################################



@mainbot.command(aliases=["Restockworld","Restock","world","restockWorld"])
@commands.guild_only()
async def restockworld(ctx):
    restockworld_post = BotBroker("https://botbroker.io/groups/restock-world","https://i.imgur.com/Ow5VHqq.jpg","https://botbroker.io/bids/new/restock-world").no_lifetime()

    channel = mainbot.get_channel(channel_id)
    if channel.id == channel_id:

        await channel.send(embed = restockworld_post)


@mainbot.command(aliases=["Peachypings","PeachyPings","peachy","Peachy","peachyPings"])
@commands.guild_only()
async def peachypings(ctx):
    peachy_post = BotBroker("https://botbroker.io/groups/peachy-pings","https://i.imgur.com/mPaWntS.png","https://botbroker.io/bids/new/peachy-pings").lifetime()

    channel = mainbot.get_channel(channel_id)
    if channel.id == channel_id:

        await channel.send(embed = peachy_post)

@mainbot.command(aliases=["Excluded"])
@commands.guild_only()
async def excluded(ctx):
    excluded_post = BotBroker("https://botbroker.io/groups/excluded","https://i.imgur.com/IC75BEx.png","https://botbroker.io/bids/new/excluded").no_lifetime()

    channel = mainbot.get_channel(channel_id)
    if channel.id == channel_id:

        await channel.send(embed = excluded_post)

@mainbot.command(aliases=["Guap"])
@commands.guild_only()
async def guap(ctx):
    guap_post = BotBroker("https://botbroker.io/groups/guap","https://i.imgur.com/FRNUvJu.png","https://botbroker.io/bids/new/guap").lifetime()

    channel = mainbot.get_channel(channel_id)
    if channel.id == channel_id:

        await channel.send(embed = guap_post)

@mainbot.command(aliases=["Bouncealerts","Bounce","bounce","BounceAlerts"])
@commands.guild_only()
async def bouncealerts(ctx):
    bouncealerts_post = BotBroker("https://botbroker.io/groups/bounce-alerts","https://i.imgur.com/oa2bwDx.png","https://botbroker.io/bids/new/bounce-alerts").lifetime()


    channel = mainbot.get_channel(channel_id)
    if channel.id == channel_id:

        await channel.send(embed = bouncealerts_post)

@mainbot.command(aliases=["Hidden","Society","Hiddensociety","ahiddensociety","AHiddensociety","Ahiddensociety","AHiddenSociety","aHiddenSociety"])
@commands.guild_only()
async def hiddensociety(ctx):
    hiddensociety_post = BotBroker("https://botbroker.io/groups/hidden-society","https://res.cloudinary.com/dcbenpm7u/image/twitter_name/w_600/ahiddensociety.jpg","https://botbroker.io/bids/new/hidden-society").no_lifetime()

    channel = mainbot.get_channel(channel_id)
    if channel.id == channel_id:

        await channel.send(embed = hiddensociety_post)


@mainbot.command(aliases=["Site","site","supply","Supply","Sitesupply","siteSupply","SiteSupply"])
@commands.guild_only()
async def sitesupply(ctx):
    sitesupply_post = BotBroker("https://botbroker.io/groups/site-supply","https://i.imgur.com/WlV0Y39.png","https://botbroker.io/bids/new/site-supply").lifetime()

    channel = mainbot.get_channel(channel_id)
    if channel.id == channel_id:

        await channel.send(embed = sitesupply_post)

@mainbot.command()
@commands.guild_only()
async def fakemonitor(ctx):
    fakemonitor_post = BotBroker("https://botbroker.io/groups/fake-monitor","https://i.imgur.com/dkBeWoj.png","https://botbroker.io/bids/new/fake-monitor").no_lifetime()

    channel = mainbot.get_channel(channel_id)
    if channel.id == channel_id:

        await channel.send(embed = fakemonitor_post)

@mainbot.command()
@commands.guild_only()
async def sabreio(ctx):
    sabreio_post = BotBroker("https://botbroker.io/groups/sabreio","https://res.cloudinary.com/dklrin11o/image/twitter_name/w_600/sabreio.jpg","https://botbroker.io/bids/new/sabreio").no_lifetime()

    channel = mainbot.get_channel(channel_id)
    if channel.id == channel_id:

        await channel.send(embed = sabreio_post)

token_RR = "NzA4MDAxODIwMTQ3OTc0MTk0.XvfcKA.ANFu-wYyHaNrRn57627-3JMuAyY"
token_test = "NzE0MDgzODU1MjU0MDI4MzA4.XvfNRg.aWHB5hzC2vd0gvsgJEhvHhzDWfY"


mainbot.run(token_RR)

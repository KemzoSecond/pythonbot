import discord
from discord.ext import commands
from bs4 import BeautifulSoup
import requests
import time
import re
mainbot = commands.Bot(command_prefix = "-")



channel_id = 717262662215532620
test_channel = 688447908613324867


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


############################
### >>>>>>  Bots  <<<<<< ###
############################

splashforce_post = BotBroker("https://botbroker.io/products/splashforce","https://i.imgur.com/br7M061.png","https://botbroker.io/bids/new/splashforce").no_lifetime()
polaris_post = BotBroker("https://botbroker.io/products/polaris","https://res.cloudinary.com/dcbenpm7u/image/twitter_name/w_600/polarisaio.jpg","https://botbroker.io/bids/new/polaris").no_lifetime()
balko_post = BotBroker("https://botbroker.io/products/balko","https://i.imgur.com/InY7MMU.png","https://botbroker.io/bids/new/balko").lifetime()
phantom_post = BotBroker("https://botbroker.io/products/phantom","https://i.imgur.com/8satPLU.png","https://botbroker.io/bids/new/phantom").lifetime()
dashe_post = BotBroker("https://botbroker.io/products/dashe","https://i.imgur.com/CV6MWXM.png","https://botbroker.io/bids/new/dashe").lifetime()
cyber_post = BotBroker("https://botbroker.io/products/cyber-aio","https://i.imgur.com/cvdVKqb.png","https://botbroker.io/bids/new/cyber-aio").lifetime()
pd_post = BotBroker("https://botbroker.io/products/project-destroyer","https://i.imgur.com/pF9aUGu.png","https://botbroker.io/bids/new/project-destroyer").lifetime()
wrath_post = BotBroker("https://botbroker.io/products/wrath","https://i.imgur.com/2vkT90s.png","https://botbroker.io/bids/new/wrath").lifetime()
prism_post = BotBroker("https://botbroker.io/products/prism","https://i.imgur.com/NxL1ajE.png","https://botbroker.io/bids/new/prism").no_lifetime()
mek_post = BotBroker("https://botbroker.io/products/mekpreme","https://i.imgur.com/fcFl3u7.png","https://botbroker.io/bids/new/mekpreme").lifetime()
adept_post = BotBroker("https://botbroker.io/products/adept-supreme","https://i.imgur.com/vFTqsqa.png","https://botbroker.io/bids/new/adept_supreme").lifetime()
velox_post = BotBroker("https://botbroker.io/products/velox","https://i.imgur.com/dmKhHKd.jpg","https://botbroker.io/bids/new/velox").lifetime()
scott_post = BotBroker("https://botbroker.io/products/scottbot","https://res.cloudinary.com/dklrin11o/image/twitter_name/w_600/scottbotv1.jpg","https://botbroker.io/bids/new/scottbot").no_lifetime()
tohru_post = BotBroker("https://botbroker.io/products/tohruaio","https://res.cloudinary.com/dcbenpm7u/image/twitter_name/w_600/tohruaio.jpg","https://botbroker.io/bids/new/tohruaio").no_lifetime()
swift_post = BotBroker("https://botbroker.io/products/swftaio","https://i.imgur.com/RQYnXeq.png","https://botbroker.io/bids/new/swiftaio").no_lifetime()

############################
### >>>>>  Groups  <<<<< ###
############################

excluded_post = BotBroker("https://botbroker.io/groups/excluded","https://i.imgur.com/IC75BEx.png","https://botbroker.io/bids/new/excluded").no_lifetime()
restockworld_post = BotBroker("https://botbroker.io/groups/restock-world","https://i.imgur.com/Ow5VHqq.jpg","https://botbroker.io/bids/new/restock-world").no_lifetime()
guap_post = BotBroker("https://botbroker.io/groups/guap","https://i.imgur.com/FRNUvJu.png","https://botbroker.io/bids/new/guap").lifetime()
sabreio_post = BotBroker("https://botbroker.io/groups/sabreio","https://res.cloudinary.com/dklrin11o/image/twitter_name/w_600/sabreio.jpg","https://botbroker.io/bids/new/sabreio").no_lifetime()
sitesupply_post = BotBroker("https://botbroker.io/groups/site-supply","https://i.imgur.com/WlV0Y39.png","https://botbroker.io/bids/new/site-supply").lifetime()
hiddensociety_post = BotBroker("https://botbroker.io/groups/hidden-society","https://res.cloudinary.com/dcbenpm7u/image/twitter_name/w_600/ahiddensociety.jpg","https://botbroker.io/bids/new/hidden-society").no_lifetime()
peachy_post = BotBroker("https://botbroker.io/groups/peachy-pings","https://i.imgur.com/mPaWntS.png","https://botbroker.io/bids/new/peachy-pings").lifetime()
fakemonitor_post = BotBroker("https://botbroker.io/groups/fake-monitor","https://i.imgur.com/dkBeWoj.png","https://botbroker.io/bids/new/fake-monitor").no_lifetime()
bouncealerts_post = BotBroker("https://botbroker.io/groups/bounce-alerts","https://i.imgur.com/oa2bwDx.png","https://botbroker.io/bids/new/bounce-alerts").lifetime()


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




@mainbot.command(aliases=["splash","force","Splashforce","SplashForce","splashForce"])
@commands.guild_only()
async def splashforce(ctx):
    channel = mainbot.get_channel(channel_id)
    if channel.id == channel_id:

        await channel.send(embed = splashforce_post)

@mainbot.command()
@commands.guild_only()
async def polaris(ctx):
    channel = mainbot.get_channel(channel_id)
    if channel.id == channel_id:

        await channel.send(embed = polaris_post)

@mainbot.command()
@commands.guild_only()
async def balko(ctx):
    channel = mainbot.get_channel(channel_id)
    if channel.id == channel_id:

        await channel.send(embed = balko_post)

@mainbot.command()
@commands.guild_only()
async def phantom(ctx):
    channel = mainbot.get_channel(channel_id)
    if channel.id == channel_id:

        await channel.send(embed = phantom_post)

@mainbot.command()
@commands.guild_only()
async def dashe(ctx):
    channel = mainbot.get_channel(channel_id)
    if channel.id == channel_id:

        await channel.send(embed = dashe_post)

@mainbot.command()
@commands.guild_only()
async def cyber(ctx):
    channel = mainbot.get_channel(channel_id)
    if channel.id == channel_id:

        await channel.send(embed = cyber_post)


@mainbot.command()
@commands.guild_only()
async def pd(ctx):
    channel = mainbot.get_channel(channel_id)
    if channel.id == channel_id:

        await channel.send(embed = pd_post)


@mainbot.command()
@commands.guild_only()
async def wrath(ctx):
    channel = mainbot.get_channel(channel_id)
    if channel.id == channel_id:

        await channel.send(embed = wrath_post)


@mainbot.command()
@commands.guild_only()
async def prism(ctx):
    channel = mainbot.get_channel(channel_id)
    if channel.id == channel_id:

        await channel.send(embed = prism_post)


@mainbot.command()
@commands.guild_only()
async def mek(ctx):
    channel = mainbot.get_channel(channel_id)
    if channel.id == channel_id:

        await channel.send(embed = mek_post)

@mainbot.command()
@commands.guild_only()
async def adept(ctx):
    channel = mainbot.get_channel(channel_id)
    if channel.id == channel_id:

        await channel.send(embed = adept_post)

@mainbot.command()
@commands.guild_only()
async def velox(ctx):
    channel = mainbot.get_channel(channel_id)
    if channel.id == channel_id:

        await channel.send(embed = velox_post)


@mainbot.command()
@commands.guild_only()
async def scott(ctx):
    channel = mainbot.get_channel(channel_id)
    if channel.id == channel_id:

        await channel.send(embed = scott_post)


@mainbot.command()
@commands.guild_only()
async def tohru(ctx):
    channel = mainbot.get_channel(channel_id)
    if channel.id == channel_id:

        await channel.send(embed = tohru_post)

@mainbot.command()
@commands.guild_only()
async def swift(ctx):
    channel = mainbot.get_channel(channel_id)
    if channel.id == channel_id:

        await channel.send(embed = swift_post)


@mainbot.command(aliases=["Restockworld","Restock","world"])
@commands.guild_only()
async def restockworld(ctx):

    channel = mainbot.get_channel(channel_id)
    if channel.id == channel_id:

        await channel.send(embed = restockworld_post)


@mainbot.command(aliases=["Peachypings","PeachyPings","peachy","Peachy"])
@commands.guild_only()
async def peachypings(ctx):

    channel = mainbot.get_channel(channel_id)
    if channel.id == channel_id:

        await channel.send(embed = peachy_post)

@mainbot.command(aliases=["Excluded"])
@commands.guild_only()
async def excluded(ctx):

    channel = mainbot.get_channel(channel_id)
    if channel.id == channel_id:

        await channel.send(embed = excluded_post)

@mainbot.command(aliases=["Guap"])
@commands.guild_only()
async def guap(ctx):

    channel = mainbot.get_channel(channel_id)
    if channel.id == channel_id:

        await channel.send(embed = guap_post)

@mainbot.command(aliases=["Bouncealerts","Bounce","bounce"])
@commands.guild_only()
async def bouncealerts(ctx):

    channel = mainbot.get_channel(channel_id)
    if channel.id == channel_id:

        await channel.send(embed = bouncealerts_post)

@mainbot.command(aliases=["Hidden","Society","Hiddensociety"])
@commands.guild_only()
async def hiddensociety(ctx):

    channel = mainbot.get_channel(channel_id)
    if channel.id == channel_id:

        await channel.send(embed = hiddensociety_post)


@mainbot.command(aliases=["Site","site","supply","Supply","Sitesupply","siteSupply","SiteSupply"])
@commands.guild_only()
async def sitesupply(ctx):

    channel = mainbot.get_channel(channel_id)
    if channel.id == channel_id:

        await channel.send(embed = sitesupply_post)

@mainbot.command()
@commands.guild_only()
async def fakemonitor(ctx):

    channel = mainbot.get_channel(channel_id)
    if channel.id == channel_id:

        await channel.send(embed = fakemonitor_post)

@mainbot.command()
@commands.guild_only()
async def sabreio(ctx):

    channel = mainbot.get_channel(channel_id)
    if channel.id == channel_id:

        await channel.send(embed = sabreio_post)

token_RR = "NzA4MDAxODIwMTQ3OTc0MTk0.XvfcKA.ANFu-wYyHaNrRn57627-3JMuAyY"
token_test = "NzE0MDgzODU1MjU0MDI4MzA4.XvfNRg.aWHB5hzC2vd0gvsgJEhvHhzDWfY"


mainbot.run(token_RR)
import os

from bs4 import BeautifulSoup
import requests
import discord
from discord.ext import commands
from prettytable import PrettyTable

DISCORD_TOKEN = os.environ.get("DISCORD_TOKEN")
intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix='!', intents=intents)

nsw_url = "https://www.nsw.gov.au/covid-19"
response = requests.get("https://www.nsw.gov.au/covid-19")
soup = BeautifulSoup(response.text, "html.parser")
message = ""
for stat in soup.findAll("h5", class_="statistics__item--heading"):
    heading = ' '.join(stat.text.split())
    message += f"{heading}\n"
    datano = stat.parent.div.text
    message += f"{datano}\n"

print(message)


@bot.event
async def on_ready():
    print('we have on as {0.user}'.format(bot))
    test_channel = bot.get_channel(515542525478436867)
    await test_channel.send(message)
    await bot.close()

bot.run(DISCORD_TOKEN)

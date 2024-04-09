


import discord
from discord.ext import commands
import csv
import sys

TOKEN = "token here"

intents = discord.Intents.all()
intents.messages = True

bot = commands.Bot(command_prefix='/', intents=intents)

def search_data(keywords):
    with open('breach.csv', 'r', encoding='utf-8') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            for field in row:
                if any(keyword.lower() in field.lower() for keyword in keywords):
                    return ', '.join(row)  
        return "Data not found."

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')

@bot.command()
async def search(ctx, *, query: str):
    keyword_list = [keyword.strip() for keyword in query.split(',')]
    result = search_data(keyword_list)
    await ctx.send(result if result != "Data not found." else "Not found!")         


bot.run(TOKEN)

import discord
from discord import app_commands
from discord.ext import commands
import random
import pathlib

TOKEN = "MTE3OTA5MDEwMDc4MTU4MDMzMQ.GrqYD-.6nGv36TG5JdVeuAlOEZuvUqoD75uRyvkYLuXfM"
PREFIX = ""
intents = discord.Intents.all()
bot = commands.Bot(command_prefix=PREFIX, intents=intents)

@bot.command()
async def привет(ctx):
    file1 = open("hello.txt", "r", encoding="utf-8")
    line_num = random.randrange(0, 6)
    phrases = file1.readlines()
    otv = phrases[line_num]
    file1.close


    channel = ctx.channel
    await channel.send(otv)



@bot.command()
async def выеби(ctx, *args):
    otv = "пашел нахуй, "+ str(args[0])
    channel = ctx.channel
    await channel.send(otv)


@bot.command()
async def мотивация(ctx):
    photo_num = random.randrange(0, 101)
    print(photo_num)
    photo = pathlib.PurePath('photos/', (str(photo_num)+".jpg"))
    channel = ctx.channel
    #channel = bot.get_channel(1179089379923341342)
    #channel = bot.get_channel(1179158538447228938)
    await channel.send(file=discord.File(photo))

    file1 = open("motivation.txt", "r", encoding="utf-8")
    line_num = random.randrange(0, 366)
    phrases = file1.readlines()
    await ctx.send(phrases[line_num])
    file1.close

@bot.command()
async def ddos(ctx, *args):
    for i in range(1,11):
        # otv = str(i) + " " + str(args[0])
        otv = "пашел нахуй," + " " + str(args[0])
        channel = ctx.channel
        await channel.send(otv)

bot.run(TOKEN)
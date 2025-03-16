import discord
from discord.ext import commands
from model import check_saha

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! I am a bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def check(ctx):
    if ctx.message.attachments:
        for file in ctx.message.attachments:
            file_name= file.filename
            await file.save(f"./images1/{file.filename}")
            await ctx.send(f"Fotoğraf başarıyla kaydedildi:{file.filename }")
            await ctx.send(check_saha(f"./images1/{file.filename}"))
    else:
        await ctx.send("Bir fotoğraf eklemelisiniz.")

bot.run("TOKEN")
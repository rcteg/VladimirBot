import discord
from discord.ext.commands import Bot
from discord.ext import commands
bot = Bot(command_prefix='~') # or whatever prefix you choose(!,%,?)

# insert the line below at the end of the file
# define <TOKEN> as your discord bot token
TOKEN = input("Provide Bot token ")

@bot.event
async def on_ready():
    await bot.change_presence(activity = discord.Game('League of Legends'))

@bot.event
async def on_message(message):
    await bot.process_commands(message)
    for i in badwords:
        if i in message.content:
            await message.delete()


@bot.event
async def on_message_delete(message):
    pass

@bot.command(name='build')
@commands.cooldown(1.0, 60.0, commands.BucketType.guild)
async def giveBuild(context):
    await context.channel.send("https://u.gg/lol/champions/vladimir/build")

@bot.command(name='addBannedWord')
async def giveBuild(context):
    await context.channel.send("Read OP.GG you fucking moron")


@bot.command(name='ban')
async def giveBuild(context):
    await context.channel.send("Read OP.GG you fucking moron")

@bot.command(name='kick')
async def giveBuild(context):
    await context.channel.send("Read OP.GG you fucking moron")

@bot.command(name='mute')
async def giveBuild(context, time):
    await context.channel.send("Read OP.GG you fucking moron")

@bot.command(name='addCommand')
async def addCommand(context):
    pass

@bot.command(name='editCommand')
async def editCommand(context):
    pass

@bot.command(name='delCommand')
async def delCommand(context):
    pass


bot.run(TOKEN)

# IMPORT DISCORD.PY. ALLOWS ACCESS TO DISCORD'S API.
import discord
from discord.ext import commands

intents = discord.Intents.all()
intents.members = True
client = commands.Bot(intents=intents, command_prefix="!")
# CHANGE CHANNEL ID FOR YOUR DISCORD AND UNCOMMENT LINE
#clashChannel = client.get_channel(123456789876542345)

# GRAB THE BOTS PRIVATE TOKEN
DISCORD_TOKEN = 'REDACTED'

# THIS IS DISGUSTING BUT WHO CARES
blacklistFile = open("nono_words.txt", "r")
unCutWords = blacklistFile.read()
cutWords = unCutWords.split(",")
blackListWords = cutWords

@client.event
async def on_ready():
    # CREATES A COUNTER TO KEEP TRACK OF HOW MANY GUILDS / SERVERS THE BOT IS CONNECTED TO.
    guild_count = 0

    # LOOPS THROUGH ALL THE GUILD / SERVERS THAT THE BOT IS ASSOCIATED WITH.
    for guild in client.guilds:
        # PRINT THE SERVER'S ID AND NAME.
        print(f"- {guild.id} (name: {guild.name})")

        # INCREMENTS THE GUILD COUNTER.
        guild_count = guild_count + 1

    # PRINTS HOW MANY GUILDS / SERVERS THE BOT IS IN.
    print("Johnny NoClashMessage is in " + str(guild_count) + " servers.")
    print(blackListWords)


# Handle any bums that send league of babies stuff to main channel during tourny
@client.event
async def on_message(message):
    # FIRST CHECK IF MESSAGE IS IN MAIN CHANNEL OR NOT
    # CHANGE CHANNEL ID FOR YOUR DISCORD AND UNCOMMENT LINE
    #if message.channel.id == 1234567834561326245:
        return
    # CHECKS IF THE MESSAGE SENT IS THE BOT'S JOIN MESSAGE
    if message.author.bot:
        return
    # CHECKS IF THE ANY PART OF THE MESSAGE SENT CONTAINS ANY BLACKLISTED WORDS
    if any(x in message.content for x in blackListWords):
        # SENDS BACK A MESSAGE TO THE CHANNEL.
        copiedMessage = message
        await message.delete()
        await message.channel.send('Wrong Channel', file=discord.File('HALT.PNG'), delete_after=5)


# Send a message to the general channel everytime somebody joins the voice chat
@client.event
async def on_voice_state_update(member, before, after):
    channel = before.channel or after.channel
    userGuild = member.guild

    if channel.id == 838768153529155658:  # Insert voice channel ID
        if before.channel is None and after.channel is not None:  # Member joins the defined channel
            await userGuild.system_channel.send(
             " Hello There " + member.name + ", don't send any L.o.L. shiite in this channel, send it in 'clash' ")  # Send a notification to the channel


# EXECUTES THE BOT WITH THE SPECIFIED TOKEN. TOKEN HAS BEEN REMOVED AND USED JUST AS AN EXAMPLE.
client.run(DISCORD_TOKEN)

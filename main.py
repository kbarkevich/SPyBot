import sys
import discord
import random
from discord import PCMAudio, Message
import asyncio
from threading import Thread
from discord.ext import commands
from quart import Quart, request, render_template, redirect

app = Quart(__name__,
            static_url_path='',
            static_folder='web',
            template_folder='web')
client = commands.Bot(command_prefix='~')

client_loop = None

################## DISCORD BOT ##################
@client.event
async def on_ready():
    print("Bot is ready!")


@client.command(
    name="nick_roulette",
    description="Play a game of Nickname Roulette! Randomly shuffle names around with your fellow voice chat-goers.",
    pass_context=True,
)
async def nickRoulette(context: commands.Context):
    sender = context.message.author
    voice = sender.voice
    if voice is None:
        await context.channel.send("You aren't in a VC!")
    else:
        await context.channel.send("Spin the wheel, around it goes....")
        await play_nick_roulette(sender.voice.channel)


@client.command(
    name="voice_roulette",
    description="Play a game of Voice Chat Roulette! Randomly shuffle everybody in VC around" +
                " a specified number of chats, defaulting to all of the available ones.",
    pass_context=True,
)
async def voiceRoulette(context: commands.Context, arg="0"):
    try:
        channelcount = int(arg)
        if channelcount < 0:
            channelcount = 0
    except ValueError as e:
        print("Invalid number, defaaulting to 0")
        channelcount = 0
    print(channelcount)
    usablechannels = await get_guild_voice_channels(context.guild, count=channelcount)
    voicemembers = await get_guild_voice_members(context.guild)
    if len(usablechannels) == 0:
        context.channel.send("No usable voice channels!")
    else:
        print("Indexes for random edges are 0 and " + str(len(usablechannels)))
        print("list of channels is " + str(usablechannels))
        for member in voicemembers:
            channelindex = random.randint(0, len(usablechannels)-1)
            print("Current channel index: " + str(channelindex))
            channel = usablechannels[channelindex]
            print("Moving " + member.display_name + " to voice channel " + channel.name)
            await member.edit(voice_channel=channel)
        await context.channel.send("Spin the wheel, around it goes....")


@client.command()
async def bitch(ctx):
    await ctx.send("you smell like farts you fucking bitch")


@client.command(
    name="ha",
    description="*snort snort*",
    pass_context=True,
)
async def ha(context):
    user = context.message.author
    voice = user.voice
    if voice is not None:
        await play_audio(user.voice.channel, "sounds/ha.mp3")
    else:
        await context.channel.send("You aren't in a VC!")


@client.command(
    name="e",
    description="E",
    pass_context=True,
)
async def E(context):
    user = context.message.author
    voice = user.voice
    if voice is not None:
        await play_audio(user.voice.channel, "sounds/e.mp3", volume=4.0)
    else:
        await context.channel.send("You aren't in a VC!")


@client.command(
    name="e9",
    description="EEEEEEEEE",
    pass_context=True,
)
async def E9(context):
    user = context.message.author
    voice = user.voice
    if voice is not None:
        await play_audio(user.voice.channel, "sounds/e9.mp3", volume=6.0)
    else:
        await context.channel.send("You aren't in a VC!")


@client.command(
    name="bige",
    description="EEEeee...",
    pass_context=True,
)
async def bigE(context):
    user = context.message.author
    voice = user.voice
    if voice is not None:
        await play_audio(user.voice.channel, "sounds/bige.mp3", volume=4.0)
    else:
        await context.channel.send("You aren't in a VC!")


@client.command(
    name="somebode",
    description="e E e e, e e?",
    pass_context=True,
)
async def bigE(context):
    user = context.message.author
    voice = user.voice
    if voice is not None:
        await play_audio(user.voice.channel, "sounds/somebodE.mp3", volume=4.0)
    else:
        await context.channel.send("You aren't in a VC!")


@client.command(
    name="a",
    description="A",
    pass_context=True,
)
async def A(context):
    user = context.message.author
    voice = user.voice
    if voice is not None:
        await play_audio(user.voice.channel, "sounds/a.mp3", volume=6.0)
    else:
        await context.channel.send("You aren't in a VC!")


@client.command(
    name="biga",
    description="AAAaaa...",
    pass_context=True,
)
async def bigA(context):
    user = context.message.author
    voice = user.voice
    if voice is not None:
        await play_audio(user.voice.channel, "sounds/biga.mp3", volume=4.0)
    else:
        await context.channel.send("You aren't in a VC!")


@client.command(
    name="sports",
    description="SPORTS",
    pass_context=True,
)
async def sports(context):
    user = context.message.author
    voice = user.voice
    if voice is not None:
        await play_audio(user.voice.channel, "sounds/sports.mp3", volume=6.0)
    else:
        await context.channel.send("You aren't in a VC!")


@client.command(
    name="bigsports",
    description="SPOOOorrtss...",
    pass_context=True,
)
async def bigSports(context):
    user = context.message.author
    voice = user.voice
    if voice is not None:
        await play_audio(user.voice.channel, "sounds/bigsports.mp3", volume=6.0)
    else:
        await context.channel.send("You aren't in a VC!")


@client.command(
    name="2sports",
    description="2SPOOOorrtss...",
    pass_context=True,
)
async def bigSports(context):
    user = context.message.author
    voice = user.voice
    if voice is not None:
        await play_audio(user.voice.channel, "sounds/2sports.mp3", volume=4.0)
    else:
        await context.channel.send("You aren't in a VC!")


@client.command(
    name="2sportsx",
    description="2SPOOOorrtss... X!",
    pass_context=True,
)
async def twoSportsX(context: discord.ext.commands.context.Context):
    user = context.message.author
    voice = user.voice
    if voice is not None:
        await play_audio(user.voice.channel, "sounds/2sportsx.mp3", volume=2.5)
    else:
        await context.channel.send("You aren't in a VC!")


@client.command(
    name="game",
    description="SINAGAME",
    pass_context=True,
)
async def game(context):
    user = context.message.author
    voice = user.voice
    if voice is not None:
        await play_audio(user.voice.channel, "sounds/game.mp3", volume=6.0)
    else:
        await context.channel.send("You aren't in a VC!")


@client.command(
    name="trucks",
    description="Two of them.",
    pass_context=True,
)
async def trucks(context):
    user = context.message.author
    voice = user.voice
    if voice is not None:
        await play_audio(user.voice.channel, "sounds/trucks.mp3")
    else:
        await context.channel.send("You aren't in a VC!")

@client.command(
    name="trains",
    description="Chugga chugga, whoo whoo!",
    pass_context=True,
)
async def trains(context):
    user = context.message.author
    voice = user.voice
    if voice is not None:
        await play_audio(user.voice.channel, "sounds/trains.mp3", volume=0.5)
    else:
        await context.channel.send("You aren't in a VC!")


def send_message_to_channel(message, channel):
    print("getting channel")
    channel = client.get_channel(int(channel))
    print("sending to channel")
    client.loop.create_task(channel.send(message))
    print("done")
    return "done"


async def play_audio(voice_channel, filename, volume=1.0):
    vc = await voice_channel.connect()
    player = vc.play(discord.PCMVolumeTransformer(discord.FFmpegPCMAudio(filename), volume), after=lambda e: print('done playing ', e))
    while vc.is_playing():
        await asyncio.sleep(1)
    vc.stop()
    await vc.disconnect()


async def play_nick_roulette(channel: discord.VoiceChannel):
    members = channel.members
    names = list()
    for member in members:
        print(member.display_name)
        names.append(member.display_name)
    random.shuffle(names)
    for i in range(0, len(members)):
        print("Changing " + members[i].display_name + "'s nickname to", names[i])
        try:
            await members[i].edit(nick=names[i])
        except discord.errors.Forbidden as e:
            print("Permission was denied.")


async def get_guild_voice_channels(guild: discord.Guild, count:int = 0, includeafk=False):
    channels = guild.voice_channels
    afk = guild.afk_channel
    if not includeafk and afk is not None:
        print("theres an afk channel")
        for channel in channels:
            if channel.id == afk.id:
                print("Removing afk channel " + channel.name)
                channels.remove(channel)
                break
    if len(channels) == 0:
        return []
    elif count == 0 or len(channels) <= count:
        return channels
    else:
        return channels[0:count]


async def get_guild_voice_members(guild: discord.Guild):
    channels = guild.voice_channels
    members = list()
    for channel in channels:
        for member in channel.members:
            members.append(member)
    return members


################## FLASK SERVER ##################
@app.route('/')
async def indexDefault():
    return await render_template('index.html')


@app.route('/channel/message/<channelid>')
async def indexChannel(channelid):
    try:
        channel = client.get_channel(int(channelid))
        if channel is None:
            print('channel is none')
            return redirect('/')
        return await render_template('channel/channel.html', channel=int(channelid), name=channel.name)
    except Exception as e:
        print('excepted out: ' + str(e))
        return redirect('/')


async def stop():
    await asyncio.sleep(3)


@app.route('/sendmsg', methods=['POST'])
async def sendmsg():
    data = await request.form
    print(data['message'])
    send_message_to_channel(data['message'], data['channel'])
    return "OK"


def start_discord_client():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    global client_loop
    client_loop = loop
    client.run(open(".tok", "r").readline())


def main():
    print("Hello, World!")
    p1 = Thread(target=start_discord_client)
    p1.start()
    app.debug = True
    app.run(host='0.0.0.0', port=5000)


if __name__ == '__main__':
    main()

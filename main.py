import sys
import discord
from discord import PCMAudio
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

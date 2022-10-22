import os
import discord
import responses
#from decouple import config


async def send_messages(message, user_message, is_private):
    try:
        response = responses.handle_response(user_message, message)
        await message.author.send(response) if is_private else await message.channel.send(response)
    except Exception as e:
        print(e)


def run_discord_bot():
    BOT_KEY = ('MTAzMTk3NzEzNTg4OTQ2NTQxNA.GyDoV4.ijJHjIDJ122y5C1ObI55z8z_cHoMc078pRS2Q0')
    print(BOT_KEY)
    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print(f'{client.user} is now running')

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return

        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)

        print(f"{username} said: '{user_message}'({channel})")

        if user_message[0] == '?':
            user_message = user_message[1:]
            await send_messages(message, user_message, is_private=True)
        else:
            await send_messages(message, user_message, is_private=False)

    client.run(BOT_KEY)
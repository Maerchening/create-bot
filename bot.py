import requests
from bs4 import BeautifulSoup
import discord
import asyncio
from json import loads

client_id = "4tn3n6xydw7yqfg5imjga6p445xc98"
client_secret = "ngxtv8p34es4btueh30ee6f7n1zzok"
discord_Token = ""

discord_ID = "992003515163623446"
discord_state = "기다리는중~"

Twitch_ID = 'bggul'
ment = "시간 나면 한번 들러줘"

client = discord.Client()

@client.event

async def on_ready():

    print(client.user.id)
    print("ready")
    game = discord.Game(discord_state)
    await client.change_presence(status=discord.Status.online, activity=game)
    channel = client.get_channel(discord_ID)
    oauth_key = requests.post("https://id.twitch.tv/oauth2/token?client_id=" + client_id + "&client_secret=" + client_secret + "&grant_type=client_credentials")
    access_token = loads(oauth_key.text)["access_token"]
    token_type = 'Bearer '
    authorization = token_type + access_token
    print(authorization)
    check = False

    while True:
        print("ready on Notification")
        headers = {'client-id': client_id, 'Authorization': authorization}
        response_channel = requests.get('https://api.twitch.tv/helix/streams?user_login=' + Twitch_ID, headers=headers)
        print(response_channel.text)
        try:
            if loads(response_channel.text)['data'][0]['type'] == 'live':
                print('good')
                await channel.send('ment + \n https://www.twitch.tv/ + Twitch_ID')
                print("Online")
                check = True
        except:
            print("Offline")
            check = False
        await asyncio.sleep(30)

client.run(discord_Token)
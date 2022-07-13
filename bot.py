import requests
import discord
import asyncio
from json import loads

client_id = ""
client_secret = ""
discord_Token = ""

discord_state = "대기"

Twitch_ID = ''
ment = "방송켰다~ 당장 달려와~"

client = discord.Client()

@client.event
async def on_ready():
    game = discord.Game(discord_state)
    await client.change_presence(status=discord.Status.online, activity=game)
    channel = client.get_channel()
    oauth_key = requests.post("https://id.twitch.tv/oauth2/token?client_id=" + client_id + "&client_secret=" + client_secret + "&grant_type=client_credentials")
    access_token = loads(oauth_key.text)["access_token"]
    token_type = 'Bearer '
    authorization = token_type + access_token
    check = False

    while True:
        headers = {'client-id': client_id, 'Authorization': authorization}
        response_channel = requests.get('https://api.twitch.tv/helix/streams?user_login=' + Twitch_ID, headers=headers)
        #print(response_channel.text)
        try:
            if loads(response_channel.text)['data'][0]['type'] == 'live' and check==False:
                await channel.send(ment + '\nhttps://www.twitch.tv/' + Twitch_ID)
                check = True
        except:
            check = False
        await asyncio.sleep(10)

client.run(discord_Token)
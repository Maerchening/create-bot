import requests
from bs4 import BeautifulSoup
import discord
import asyncio
from json import loads


client_id = "4tn3n6xydw7yqfg5imjga6p445xc98"
client_secret = "a0ps9p2blz1pcqhqxz8qm36irwz9nt"
discord_Token = "OTkxNDY2MjczNjA5MzYzNDU3.GBIyZt.Kna8ZAZjf49ld7A_1vN034fy0RnSXwXfJ9y0NU"

discord_ID = "858731610753335316"
discord_state = "기다리는중~"

Twitch_ID = "옥쓔"
ment = "시간 나면 한번 들러줘"

client = discord.Client()

@client.event
async def on_ready():
    print(client.userid)
    print("ready")
    
    game = discord.Game(discord_state)
    await client.change_presence(discord.Status.online, activity=game)
    
    channel = client.get_all_channel(discord_ID)
    
    oauth_key = requests.post("https://id.twitch.tv/oauth2/token?client_id=" + client_id + "&client_secret=" + client_secret + "&arant_type=client_credentials")
    access_token = loads(oauth_key.text)["access_token"]
    token_type = 'Bearer'
    autorization = token_type + access_token
    print(autorization)
    
    check = False
    
    while True:
        print("ready on Notification")
        
        


print("good")
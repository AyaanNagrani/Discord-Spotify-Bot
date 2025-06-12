import discord
from discord.ext import commands
import logging
import os
from requests import post
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from dotenv import load_dotenv


load_dotenv()

token = os.getenv('DISCORD_BOT_TOKEN')
spot_clientID = os.getenv('SPOTIFY_CLIENT_ID')
spot_apiKey = os.getenv('SPOTIFY_CLIENT_SECRET')


bot = commands.Bot(command_prefix="/", intents=discord.Intents.all())

 

spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(
    client_id=spot_clientID,
    client_secret=spot_apiKey
))





@bot.command()
async def mood(ctx, *, mood):
    mood = mood + ' playlist'
    result = spotify.search(q=mood, type='playlist', limit=10)
    await ctx.send(f"Hey, {ctx.author}! Here are some {mood}!")
    lst = []
    for playlist in result['playlists']['items']:
        try:
            lst.append(f"-{playlist['name']} by {playlist['owner']['display_name']}")
        except TypeError:
            continue
    await ctx.send("\n".join(lst))

    
    



   

    

bot.run(token)

# takes user input of mood "happy sad" > finds playlist on spotify with name happy sad'


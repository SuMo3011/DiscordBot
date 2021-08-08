import discord
import os
import reddit

client = discord.Client()

@client.event
async def on_ready():
  print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  msg = message.content

  if msg.startswith('!hello'):
    await message.channel.send(f'Hey {message.author}!')


  if msg.startswith('!joke'):
    post = reddit.get_post(reddit_client, 'Jokes', 'hot', False)
    await message.channel.send(f'{post.title}\n\n{post.selftext}')
  
  if msg.startswith('!meme'):
    subred = msg.split('!meme', 1)
    if len(subred)>1:
      subred = subred[1]
    else:
      subred = 'Memes'

    post = reddit.get_post(reddit_client, subred, 'top', False)
    embed = discord.Embed(title=post.title, color=discord.Color.purple())
    embed.set_image(url=post.url)
    await message.channel.send(embed=embed)


reddit_client = reddit.create_reddit_object()
discord_token = os.environ['discord_token']
client.run(discord_token)
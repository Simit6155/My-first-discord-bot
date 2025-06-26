import discord
import os
from dotenv import load_dotenv
import requests
from keep_alive import keep_alive

load_dotenv()

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print("We have logged in as {0.user}".format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith("$hello"):
        await message.channel.send("Sybau")
    if message.content.startswith("$help"):
        await message.channel.send("SYBAAUUU")
    if message.content.startswith("$yo"):
        await message.channel.send("whats up")
    if message.content.startswith("$pmo"):
        await message.channel.send("ts pmo ngl icl sybau stfu atp lil br gng")
    if message.content.startswith("$yogurt"):
        await message.channel.send("""
Gurt: yo
o: what do you mean y?
you: i didnt say anything
didnt: yes i did say something
something: u didnt call my name???
name: im not yours!!
absolute cinema
https://tenor.com/view/me-atrapaste-es-cine-its-cinema-cinema-esto-es-cine-gif-17729711691959966457
        """)

    if message.content.startswith("$Hack"):
        await message.channel.send("Enter the user to hack: ")

        def check(m):
            return m.author == message.author and m.channel == message.channel

        reply = await client.wait_for("message", check=check, timeout=30.0)
        usertohack = reply.content
        await message.channel.send("Hacked User: " + usertohack + """
Full Name = Ben Jerremy 
Age = 19
House = New yorker street 12
phone number = +55 345 556 234
Email = maymun@gmail.com
ip adress = 198.129.586.15
mac adress = 00:14:22:01:23:45
        """)


keep_alive()
client.run(os.getenv('TOKEN'))

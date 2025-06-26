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
        await message.channel.send("Hello , how are you? ")

    if message.content.startswith("$help"):
        await message.channel.send("Check the repository https://github.com/Simit6155/My-first-discord-bot if you need any help.")

    if message.content.startswith("$yo"):
        await message.channel.send("Whats up")

    if message.content.startswith("$code"):
        await message.channel.send("""
What type of code do you need?
[1] Geolocator
[2] Port scanner
[3] Spambot 
""")
        def check_(m):
            return m.author == message.author and m.channel == message.channel

        command_ = await client.wait_for("message", check=check_, timeout=30.0)
        command__ = command_.content
        if command__ == "1":
            await message.channel.send("""
```python
ip = input(Fore.GREEN + "Enter IP Address: ")

url = f"https://ipapi.co/{ip}/json/"
response = requests.get(url, timeout=5)
data = response.json()

network = data.get("network", "Unknown")
version = data.get("version", "Unknown")
city = data.get("city", "Unknown")
country = data.get("country", "Unknown")
country_name = data.get("country_name", "Unknown")
country_code = data.get("country_code", "Unknown")
postal = data.get("postal", "Unknown")
timezone = data.get("timezone", "Unknown")
asn = data.get("asn", "Unknown")
languages = data.get("languages", "Unknown")
country_capital = data.get("country_capital", "Unknown")
country_area = data.get("country_area", "Unknown")

longitude = data.get("longitude", "Unknown")
latitude = data.get("latitude", "Unknown")

print(Fore.GREEN + "Network: " + network)
print(Fore.GREEN + "Version: " + version)
print(Fore.GREEN + "City: " + city)
print(Fore.GREEN + "Country: " + country)
print(Fore.GREEN + "Country_name: " + country_name)
print(Fore.GREEN + "Country_code: " + country_code)
print(Fore.GREEN + "Country_capital: " + country_capital)
print(Fore.GREEN + "Postal Code: " + postal)
print(Fore.GREEN + "Timezone: " + timezone)
print(Fore.GREEN + "ASN: " + asn)
print(Fore.GREEN + "Languages: " + languages)
print(Fore.GREEN + "Country_area: " + str(country_area))

print(Fore.GREEN + "Longitude: " + str(longitude))
print(Fore.GREEN + "Latitude: " + str(latitude))
print(Fore.GREEN + f"https://www.google.com/maps?q={latitude},{longitude}")
```
""")

        elif command__ == "2":
            await message.channel.send("""
```python
choice = input(Fore.RED + "[1] Single Port scanner [2] Multi Port scanner"

if choice == "1":
    ip = input(Fore.GREEN + "IP to scan: ")
    port = int(input(Fore.GREEN + "Input the following port: "))
    time.sleep(1)
    print(Fore.LIGHTGREEN_EX + "Connecting...")
    time.sleep(2)

    try:
        socket.create_connection((ip, port), timeout=4)  # you can change the timeout if you want cuz its kinda long
        print(Fore.GREEN + "port is open")
    except socket.error:
        print(Fore.GREEN + "port is closed")

elif choice == "2":
    ip = input(Fore.GREEN + "Enter IP to scan: ")
    ports = [4444, 445, 443, 8080,
             20, 21, 22, 23, 25, 53,
             68, 80, 110, 123, 135, 67,
             137, 138, 139, 143, 161,
             162, 389, 443, 445, 465,
             514, 587, 636, 993, 995,
             1080, 1433, 1521, 1723,
             2049, 2121, 3306, 3389,
             5432, 5900, 6000, 8080,
             8443, 8888, 10000, 20000,
             32768, 49152, 65535]

    for port in ports:
        try:
            socket.create_connection((ip, port),
                                     timeout=1)  # I recommend changing the timeout to 2 or 3 if you want to be sure
            print(Fore.RED + f"Port {port} open ")
        except socket.error:
            print(Fore.LIGHTBLACK_EX + f"Port {port} closed ")
``` 
""")
        elif command__ == "3":
            await message.channel.send("""
```python
print(Fore.GREEN + "             Author: @Redsimit")
limit = input(Fore.RED + "Input the number of messages to send: ")
speed = input(Fore.RED + "Input the waiting time between messages: ")
word = input(Fore.RED + "Input your message: ")
print(Fore.GREEN + "Put your mouse on the place to spamm the messages!")
time.sleep(3)
print("SENDING MESSAGES... ")
a = 1
while a <= int(limit):
    pyautogui.typewrite(word)
    pyautogui.press("enter")
    a = a + 1
    time.sleep(float(speed))
```
""")
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

    if message.content.startswith("$hack"):
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

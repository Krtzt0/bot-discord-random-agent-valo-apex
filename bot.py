import discord
import random
import os
from dotenv import load_dotenv
from discord.ext import commands

# โหลด environment variables
load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

# ตั้งค่า intents
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

# รายชื่อตัวละครและรูปภาพสำหรับ Apex Legends
apex_legends = {
    "Alter": "https://static.wikia.nocookie.net/apexlegends_gamepedia_en/images/f/f8/Alter.jpg/revision/latest?cb=20240510002053",
    "Ash": "https://apexlegends.wiki.gg/images/thumb/7/70/Ash.jpg/300px-Ash.jpg",
    "Ballistic": "https://static.wikia.nocookie.net/apexlegends_gamepedia_en/images/4/4a/Ballistic.jpg/revision/latest?cb=20230425012245",
    "Bangalore": "https://apexlegends.wiki.gg/images/thumb/f/f7/Bangalore.jpg/300px-Bangalore.jpg",
    "Catalyst": "https://apexlegends.wiki.gg/images/thumb/9/9d/Catalyst.jpg/300px-Catalyst.jpg",
    "Caustic": "https://apexlegends.wiki.gg/images/thumb/e/e7/Caustic.jpg/300px-Caustic.jpg",
    "Conduit": "https://static.wikia.nocookie.net/apexlegends_gamepedia_en/images/8/8f/Conduit.jpg/revision/latest?cb=20231026232222",
    "Crypto": "https://apexlegends.wiki.gg/images/thumb/1/1f/Crypto.jpg/300px-Crypto.jpg",
    "Fuse": "https://apexlegends.wiki.gg/images/thumb/2/25/Fuse.jpg/300px-Fuse.jpg",
    "Gibraltar": "https://apexlegends.wiki.gg/images/thumb/8/8b/Gibraltar.jpg/300px-Gibraltar.jpg",
    "Horizon": "https://static.wikia.nocookie.net/apexlegends_gamepedia_en/images/7/7d/Horizon.jpg/revision/latest/scale-to-width-down/314?cb=20201102162249",
    "Lifeline": "https://static.wikia.nocookie.net/apexlegends_gamepedia_en/images/4/4f/Lifeline.jpg/revision/latest?cb=20200916154942",
    "Loba": "https://apexlegends.wiki.gg/images/thumb/7/7d/Loba.jpg/300px-Loba.jpg",
    "Mad Maggie": "https://static.wikia.nocookie.net/apexlegends_gamepedia_en/images/5/5f/Mad_Maggie.jpg/revision/latest/scale-to-width-down/314?cb=20220131161644",
    "Mirage": "https://apexlegends.wiki.gg/images/thumb/a/a6/Mirage.jpg/300px-Mirage.jpg",
    "Newcastle": "https://static.wikia.nocookie.net/apexlegends_gamepedia_en/images/b/b9/Newcastle.jpg/revision/latest/scale-to-width-down/314?cb=20220506022224",
    "Octane": "https://static.wikia.nocookie.net/apexlegends_gamepedia_en/images/d/d6/Octane.jpg/revision/latest/scale-to-width-down/314?cb=20200916155547",
    "Pathfinder": "https://apexlegends.wiki.gg/images/thumb/5/53/Pathfinder.jpg/300px-Pathfinder.jpg",
    "Rampart": "https://static.wikia.nocookie.net/apexlegends_gamepedia_en/images/5/51/Rampart.jpg/revision/latest?cb=20200816182752",
    "Revenant": "https://static.wikia.nocookie.net/apexlegends_gamepedia_en/images/e/ed/Old_Revenant.jpg/revision/latest?cb=20200916155949",
    "Seer": "https://static.wikia.nocookie.net/apexlegends_gamepedia_en/images/4/4b/Seer.jpg/revision/latest/scale-to-width-down/314?cb=20210729151504",
    "Valkyrie": "https://static.wikia.nocookie.net/apexlegends_gamepedia_en/images/5/5f/Valkyrie.jpg/revision/latest?cb=20210430145805",
    "Vantage": "https://static.wikia.nocookie.net/apexlegends_gamepedia_en/images/5/5a/Vantage.jpg/revision/latest/scale-to-width-down/314?cb=20220801155109",
    "Wattson": "https://static.wikia.nocookie.net/apexlegends_gamepedia_en/images/8/82/Wattson.jpg/revision/latest/scale-to-width-down/314?cb=20200916155642",
    "Wraith": "https://apexlegends.wiki.gg/images/thumb/a/a4/Wraith.jpg/300px-Wraith.jpg",
}

# รายชื่อตัวละครและรูปภาพสำหรับ Valorant
valorant_agents = {
    "Brimstone": "https://valorantinfo.gg/wp-content/uploads/2021/09/agent-brimstone.png",
    "Phoenix": "https://static.wikia.nocookie.net/valorant/images/9/90/Phoenix_Artwork_Full.png/revision/latest/scale-to-width/360?cb=20220810202811",
    "Breach": "https://static.wikia.nocookie.net/valorant/images/c/c7/Breach_%28Full%29.png/revision/latest/scale-to-width-down/250?cb=20230412090641",
    "Cypher": "https://static.wikia.nocookie.net/valorant/images/5/55/Cypher_Artwork_Full.png/revision/latest/scale-to-width-down/1200?cb=20220810202731",
    "Jett": "https://static.wikia.nocookie.net/valorant/images/7/79/Jett_artwork.png/revision/latest?cb=20210821140212&path-prefix=id",
    "Omen": "https://static.wikia.nocookie.net/valorant-lore/images/d/dc/Omen_-_Full_body.png/revision/latest?cb=20241030123240",
    "Raze": "https://static.wikia.nocookie.net/valorant-lore/images/b/bb/Raze_-_Full_body.png/revision/latest/scale-to-width-down/1200?cb=20241030124138",
    "Sage": "https://static.wikia.nocookie.net/valorant/images/1/1e/Sage_artwork.png/revision/latest?cb=20210821140215&path-prefix=id",
    "Sova": "https://static.wikia.nocookie.net/valorant/images/c/c5/Sova_Artwork_Full.png/revision/latest?cb=20220810202832",
    "Viper": "https://static.wikia.nocookie.net/valorant/images/8/85/Viper_Artwork_Full.png/revision/latest?cb=20220810202837",
    "Reyna": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT6-v7bFGxW6VQBWdCQcFXCAaVkM0FUkgjpog&s",
    "Killjoy": "https://static.wikia.nocookie.net/valorant-lore/images/9/99/Killjoy_-_Full_body.png/revision/latest?cb=20241030123334",
    "Skye": "https://static.wikia.nocookie.net/valorant-lore/images/0/06/Skye_-_Full_body.png/revision/latest?cb=20241030124332",
    "Yoru": "https://static.wikia.nocookie.net/valorant-lore/images/2/27/Yoru_-_Full_body.png/revision/latest?cb=20241030124430",
    "Astra": "https://static.wikia.nocookie.net/valorant/images/4/45/Astra_Plein-pied.png/revision/latest?cb=20240703111655&path-prefix=fr",
    "KAY/O": "https://static.wikia.nocookie.net/valorant-lore/images/b/bb/KAY_O_-_Full_body.png/revision/latest?cb=20241030124554",
    "Chamber": "https://static.wikia.nocookie.net/valorant-lore/images/d/d6/Chamber_-_Full_body.png/revision/latest?cb=20241030124644",
    "Neon": "https://static.wikia.nocookie.net/valorant-lore/images/0/0f/Neon_-_Full_body.png/revision/latest?cb=20241030124751",
    "Harbor": "https://static.wikia.nocookie.net/valorant/images/5/5c/Harbor_Artwork_Full.png/revision/latest/scale-to-width/360?cb=20221018133900",
    "Gekko": "https://static.wikia.nocookie.net/valorant/images/a/a4/Gekko_Artwork_Full.png/revision/latest/scale-to-width-down/1200?cb=20230304203025",
    "Deadlock": "https://static.wikia.nocookie.net/valorant/images/a/aa/Deadlock_Artwork_Full.png/revision/latest?cb=20230627132700",
    "Iso": "https://static.wikia.nocookie.net/valorant/images/5/5f/Iso_Artwork_Full.png/revision/latest?cb=20231031131018",
    "Waylay": "https://static.wikia.nocookie.net/valorant/images/4/4f/Waylay_Artwork_Full.png/revision/latest/scale-to-width/360?cb=20250304181227",
    "Tejo": "https://static.wikia.nocookie.net/valorant-lore/images/f/f5/Tejo_-_Full_body.png/revision/latest?cb=20250107233316",
}

@bot.event
async def on_ready():
    activity = discord.CustomActivity(name="สุ่มApex => !ranapex | สุ่มValorant => !ranvalo")
    await bot.change_presence(activity=activity)
    print(f"✅ Logged in as {bot.user}")

@bot.command()
async def ranapex(ctx):
    name, image_url = random.choice(list(apex_legends.items()))
    embed = discord.Embed(title=f"🎲 {name}", description="ตัวละครที่คุณสุ่มได้จาก **Apex Legends**", color=discord.Color.blue())
    embed.set_image(url=image_url)
    await ctx.send(embed=embed)

@bot.command()
async def ranvalo(ctx):
    name, image_url = random.choice(list(valorant_agents.items()))
    embed = discord.Embed(title=f"🎲 {name}", description="เอเจนต์ที่คุณสุ่มได้จาก **Valorant**", color=discord.Color.red())
    embed.set_image(url=image_url)
    await ctx.send(embed=embed)

# ตรวจสอบว่ามี Token หรือไม่ก่อนรัน
if TOKEN:
    bot.run(TOKEN)
else:
    print("❌ ERROR: DISCORD_TOKEN not found. Please check your .env file.")

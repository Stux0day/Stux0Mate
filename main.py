import discord
import os
import dotenv
dotenv.load_dotenv()

print("Lancement du bot ...")

client = discord.Client(intents=discord.Intents.all())
client.run(os.getenv('DISCORD_TOKEN'))
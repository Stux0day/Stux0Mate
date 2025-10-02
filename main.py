import discord
import os
import dotenv
dotenv.load_dotenv()

print("Lancement du bot ...")

client = discord.Client(intents=discord.Intents.all())
try: 
    client.run(os.getenv('DISCORD_TOKEN'))
except discord.errors.LoginFailure:
    (print("❌ Attention: Le token Discord est invalide ou manquant dans le .env"))
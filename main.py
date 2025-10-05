import discord, os, dotenv
import message_data
dotenv.load_dotenv()

print("Lancement de Stux0Mate ...")
client = discord.Client(intents=discord.Intents.all())

@client.event
async def on_ready():
    print(f"Connecté en tant que {client.user}")

try: 
    client.run(os.getenv('DISCORD_TOKEN'))
except discord.errors.LoginFailure:
    (print("❌ Attention: Le token Discord est invalide ou manquant dans le .env"))
import discord, os, platform, time, yaml
from discord.ext import commands
from dotenv import load_dotenv
from colorama import Fore, Style

load_dotenv()
token = os.getenv("discordToken")

with open('config.yml', 'r') as file:
    config = yaml.safe_load(file)

intents = discord.Intents.default()
intents.message_content = True
intents.all()

class PersistentButtons(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix=commands.when_mentioned_or('$'), intents=intents)
        
    async def setup_hook(self) -> None:
        None

client = PersistentButtons()

@client.event
async def on_ready():
    print(f"{client.user} is connected.")

    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            try:
                await client.load_extension(f"cogs.{filename[:-3]}")
                print(f"{Fore.GREEN}Loaded: {Style.RESET_ALL}{filename}!")
            except Exception as e:
                print(f"{Fore.RED}Failed to load: {Style.RESET_ALL}{filename}! {Fore.RED}[ERROR]: {Style.RESET_ALL}{e}")
    print("All cogs loaded!")

    await client.tree.sync()
    print("Commands synced!")
    print(f"{Fore.GREEN}Application has started up{Style.RESET_ALL}")
    
    try:
        pfp = client.user.avatar.url
    except:
        print("No profile picture found! Skipping...")
        pfp = None
    seconds = time.time()
    local_time = time.ctime(seconds)
    device_name = platform.node()
    logging_channel = config['MAIN']['loggingChannel']
    lchannel = client.get_channel(int(logging_channel))
        
    emb = discord.Embed(title=f"{client.user.name} is Online!", colour=discord.Colour.teal())
    if pfp:
        emb.set_thumbnail(url=pfp)
    emb.add_field(name="Time logged on:", value=f"{local_time} UTC", inline=False)
    emb.add_field(name="Host name:", value=device_name, inline=False)
    await lchannel.send(embed=emb)
    await client.change_presence(activity=discord.Game(name="DM waytooicyy for issues!"))

client.run(token)

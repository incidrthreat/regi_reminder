import asyncio, discord, os
from datetime import datetime
from dotenv import load_dotenv

intents = discord.Intents.default()

client = discord.Client(intents=intents)

# The load_dotenv() function reads the .env file and adds the key-value pairs in the file to the environment, 
# so that they can be accessed by your script using the os.environ object.
load_dotenv()
# Environment variables
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
DISCORD_CHANNEL = int(os.getenv("DISCORD_CHANNEL"))

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')
    f = read_file('./images/regi_icon.png')
    await client.user.edit(avatar=f.read())
    f.close
    asyncio.get_event_loop().create_task(regi())

@client.event
async def on_message(message):
    # Ensures the bot does not respond to itself.
    if message.author == client.user:
        return

async def regi():
    while True:
        # datetime.datetime.today().weekday() will give an integer value from 0-6, representing the day of the week. 
        # Monday is 0, Tuesday is 1, and so on, Sunday is 6.
        today = datetime.today().weekday()
        
        # Check if today is Tuesday
        if today == 1:
            # Get the current week of the year
            week = datetime.today().isocalendar()[1]
        # Check if it is an even week
            if week % 2 == 0:
                # Get the specific channel by its ID
                channel = client.get_channel(DISCORD_CHANNEL)
                # Open the image file
                f = read_file('./images/reginald.jpg')
                await channel.send(file=discord.File(f))
                f.close()
            # else:
            #     print("It's Tuesday, but not the right week for Reginald.")
        # else:
        #     print("It's not Tuesday.")
        
        await asyncio.sleep(86400)

# Reusable funtcion to open image files
def read_file(file_path):
    return open(file_path, "rb")

if __name__ == "__main__":
    client.run(DISCORD_TOKEN)
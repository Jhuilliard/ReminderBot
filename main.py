import os
import discord
import asyncio
import datetime
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
DISCORD_BOT_TOKEN = os.getenv('DISCORD_BOT_TOKEN')
USER_ID = os.getenv('USER_ID')

x=''
intents = discord.Intents.all()
client = commands.Bot(command_prefix=',', intents=intents)


async def send_message(user, message):
  await user.send(message)


async def schedule_daily_message(): 
  while True:
    user = await client.fetch_user(USER_ID)
    now = datetime.datetime.now()
    if now.year == 2025 and now.month == 5 and now.day == 11:
      x = "M-Day"
    if now.year == 2025 and now.month == 6 and now.day == 16:
      x = "D-Day"
    if now.year == 2024 and now.month == 12 and now.day == 18:
      x = "XMAS - 1 week"
    if now.year == 2024 and now.month == 12 and now.day == 25:
      x = "XMAS" 

    target_time = now.replace(hour=4, minute=0, second=0, microsecond=0)

    if now.date() == target_time.date() and now > target_time:
      target_time += datetime.timedelta(days=1)
  
    seconds_until_message = (target_time - now).total_seconds()
    await asyncio.sleep(seconds_until_message)

    
    await send_message(user, "Good morning!")
    if x == "M-Day":
      await send_message(user, "IT'S MOTHER'S DAY! TELL MOM YOU LOVE HER!!!")
    if x == "M-Day":
      await send_message(user, "IT'S FATHER'S DAY! TELL DAD YOU LOVE HER!!!")
    if x == "XMAS - 1 week":
      await send_message(user, "CHRISTMAS IS COMING UP! ITS 1 WEEK LEFT!!!")
    if x == "XMAS":
      await send_message(user, "IT'S CHRISTMAS!!! MERRY CHRISTMAS!!!")


@client.event
async def on_ready():
  print(f'We have logged in as {client.user}')
  asyncio.create_task(schedule_daily_message())
  
client.run(DISCORD_BOT_TOKEN)

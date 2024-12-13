'''Flightpulse
    Copyright (C) 2024  Billy Evans

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.'''

print("""FlightPulse Copyright (C) 2024  Billy Evans
    This program comes with ABSOLUTELY NO WARRANTY.
    This is free software, and you are welcome to redistribute it
    under certain conditions""")

import os
from dotenv import dotenv_values
from discord.ext import commands, tasks
from discord import app_commands
from typing import Literal, Optional
import discord
import asyncio
import time
from utils.trainlogger.main import *

# ENV READING
config = dotenv_values(".env")

BOT_TOKEN = config['BOT_TOKEN']
STARTUP_CHANNEL_ID = int(config['STARTUP_CHANNEL_ID']) # channel id to send the startup message
RARE_SERVICE_CHANNEL_ID = int(config['RARE_SERVICE_CHANNEL_ID'])
COMMAND_PREFIX = config['COMMAND_PREFIX']
USER_ID = config['USER_ID']

bot = commands.Bot(command_prefix=COMMAND_PREFIX, intents=discord.Intents.all())
log_channel = bot.get_channel(STARTUP_CHANNEL_ID)

# command categorys
# Group commands
class CommandGroups(app_commands.Group):
    ...
trainlogs = CommandGroups(name='log')

# start bot
@bot.event
async def on_ready():
    # download the trainset data     
    
    print("Bot started")
    channel = bot.get_channel(STARTUP_CHANNEL_ID)
    bot.tree.add_command(trainlogs)
    

#log train
@trainlogs.command(name="flight", description="Log a flight you have been on")
@app_commands.describe(registration = "Aircraft registration", date = "Date in DD/MM/YYYY format", airline = 'Airline', start='Departure Airport ICAO', end = 'Arrival Airport ICAO', type='Type of aircraft')
# @app_commands.autocomplete(start=station_autocompletion)
# @app_commands.autocomplete(end=station_autocompletion)
# @app_commands.autocomplete(line=line_autocompletion)

# Train logger
async def logtrain(ctx,  registration:str,  start:str, end:str, airline:str, type:str, date:str='today', notes:str=None):
    channel = ctx.channel
    await ctx.response.defer()
    print(date)
    async def log():
        print("logging the thing")

        savedate = date.split('/')
        if date.lower() == 'today':
            current_time = time.localtime()
            savedate = time.strftime("%Y-%m-%d", current_time)
        else:
            try:
                savedate = time.strptime(date, "%d/%m/%Y")
                savedate = time.strftime("%Y-%m-%d", savedate)
            except ValueError:
                await ctx.edit_original_response(content=f'Invalid date: `{date}`\nMake sure to use a possible date.')
                return
            except TypeError:
                await ctx.edit_original_response(content=f'Invalid date: `{date}`\nUse the form `dd/mm/yyyy`')
                return

        # checking if train number is valid
        '''if number != 'Unknown':
            set = setNumber(number.upper())
            if set == None:
                await ctx.edit_original_response(content=f'Invalid train number: `{number.upper()}`')
                return
            type = trainType(number.upper())
        else:
            set = 'Unknown'
            type = 'Unknown'
            if traintype == 'auto':
                type = 'Unknown'
            else: type = traintype
        if traintype == "Tait":
            set = '381M-208T-230D-317M' '''
            
        # Add train to the list
        id = addTrain(ctx.user.name, registration, type, savedate, airline, start.upper(), end.upper(), notes)
        # await ctx.response.send_message(f"Added {set} ({type}) on the {line} line on {savedate} from {start.title()} to {end.title()} to your file. (Log ID `#{id}`)")
        
        embed = discord.Embed(title="Flight Logged")
        
        embed.add_field(name="Aircraft", value=f'{registration} ({type})')
        embed.add_field(name="Airine", value=airline)
        embed.add_field(name="Date", value=savedate)
        embed.add_field(name="Trip", value=f'{start.upper()} to {end.upper()}')
        if notes:
            embed.add_field(name="Notes", value=notes)
        
        await ctx.edit_original_response(embed=embed)
                        
    # Run in a separate task
    asyncio.create_task(log())



# HERE ARE THE INTERNAL USE COMMANDS
@bot.command()
@commands.guild_only()
async def sync(ctx: commands.Context, guilds: commands.Greedy[discord.Object], spec: Optional[Literal["~", "*", "^"]] = None) -> None:
    if ctx.author.id in [707866373602148363,780303451980038165]:
        if not guilds:
            if spec == "~":
                synced = await ctx.bot.tree.sync(guild=ctx.guild)
            elif spec == "*":
                ctx.bot.tree.copy_global_to(guild=ctx.guild)
                synced = await ctx.bot.tree.sync(guild=ctx.guild)
            elif spec == "^":
                ctx.bot.tree.clear_commands(guild=ctx.guild)
                await ctx.bot.tree.sync(guild=ctx.guild)
                synced = []
            else:
                synced = await ctx.bot.tree.sync()

            await ctx.send(
                f"Synced {len(synced)} commands {'globally' if spec is None else 'to the current guild.'}"
            )
            return

        ret = 0
        for guild in guilds:
            try:
                await ctx.bot.tree.sync(guild=guild)
            except discord.HTTPException as e:
                print(f'Error: {e}')
            else:
                ret += 1

        await ctx.send(f"Synced the tree to {ret}/{len(guilds)}.")
        
@bot.command()
async def ping(ctx):
    latency = round(bot.latency * 1000)  # Convert latency to ms
    await ctx.send(f"Pong! Latency: {latency} ms")
    
@bot.command()
async def syncdb(ctx, url='https://railway-photos.xm9g.net/trainsets.csv'):
    if str(ctx.author.id) == USER_ID:
        csv_url = url
        save_location = "utils/trainsets.csv"
        await ctx.send(f"Downloading trainset data from {csv_url} to {save_location}")
        print(f"Downloading trainset data from {csv_url} to `{save_location}`")
        try:
            download_csv(csv_url, save_location)
            ctx.send(f"Sucsess!")
        except Exception as e:
            ctx.send(f"Error: `{e}`")
    else:
        print(f'{USER_ID} tried to synd the database.')
        await ctx.send("You are not authorized to use this command.")
    
# imptrant
bot.run(BOT_TOKEN)
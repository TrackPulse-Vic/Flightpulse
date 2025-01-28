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
from utils.trainlogger.stats import *
from utils.trainlogger.graph import *


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
    

#log plane
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
    
#log car
@trainlogs.command(name="drive", description="Log a drive")
@app_commands.describe(registration = "Car registration", date = "Date in DD/MM/YYYY format", start_time='Start time in 24h HH:MM format', end_time ='End time in 24h HH:MM format',start_odometer='Start odometer reading', end_odometer='End odometer reading', notes='Any notes you want to add')

# Train logger
async def logcar(ctx, registration:str, start_time:str, end_time:str, start_odometer:int, end_odometer:int, paking:bool, light_traffic:bool, moderate_traffic:bool, heavy_taffic:bool, dry_weather:bool, wet_weather:bool, local_street:bool, main_rd:bool, inner_city:bool, freeway:bool, rural_highway:bool, rural_other:bool, gravel:bool, day:bool, dawn_dusk:bool, night:bool, driver:str, date:str='today', notes:str=None):
    channel = ctx.channel
    await ctx.response.defer()
    print(date)
    async def log():
        print("logging the drive")

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
            
        # Add car to the list
        id = addCar(ctx.user.name, savedate, registration, start_time, end_time, start_odometer, end_odometer, paking, light_traffic, moderate_traffic, heavy_taffic, dry_weather, wet_weather, local_street, main_rd, inner_city, freeway, rural_highway, rural_other, gravel, day, dawn_dusk, night, driver, notes)
        # await ctx.response.send_message(f"Added {set} ({type}) on the {line} line on {savedate} from {start.title()} to {end.title()} to your file. (Log ID `#{id}`)")
        embed = discord.Embed(title="Drive Logged")
        
        embed.add_field(name="Car", value=f'{registration}')
        embed.add_field(name="Time", value=f'{savedate} {start_time} to {end_time}')
        embed.add_field(name="Odometer", value=f'{start_odometer} to {end_odometer}')
        
        if paking:
            embed.add_field(name="Parking", value=str(paking))
        if light_traffic:
            embed.add_field(name="Light Traffic", value=str(light_traffic))
        if moderate_traffic:
            embed.add_field(name="Moderate Traffic", value=str(moderate_traffic))
        if heavy_taffic:
            embed.add_field(name="Heavy Traffic", value=str(heavy_taffic))
        if dry_weather:
            embed.add_field(name="Dry Weather", value=str(dry_weather))
        if wet_weather:
            embed.add_field(name="Wet Weather", value=str(wet_weather))
        if local_street:
            embed.add_field(name="Local Street", value=str(local_street))
        if main_rd:
            embed.add_field(name="Main Road", value=str(main_rd))
        if inner_city:
            embed.add_field(name="Inner City", value=str(inner_city))
        if freeway:
            embed.add_field(name="Freeway", value=str(freeway))
        if rural_highway:
            embed.add_field(name="Rural Highway", value=str(rural_highway))
        if rural_other:
            embed.add_field(name="Rural Other", value=str(rural_other))
        if gravel:
            embed.add_field(name="Gravel", value=str(gravel))
        if day:
            embed.add_field(name="Day", value=str(day))
        if dawn_dusk:
            embed.add_field(name="Dawn/Dusk", value=str(dawn_dusk))
        if night:
            embed.add_field(name="Night", value=str(night))
        
        embed.add_field(name="Driver", value=driver)
        
        if notes:
            embed.add_field(name="Notes", value=notes)
        
        await ctx.edit_original_response(embed=embed)
        # embed = discord.Embed(title="Drive Logged")
        
        # embed.add_field(name="Car", value=f'{registration}')
        # embed.add_field(name="Time", value=f'{savedate} {start_time} to {end_time}')
        # if notes:
        #     embed.add_field(name="Notes", value=notes)
        
        # await ctx.edit_original_response(embed=embed)
                        
    # Run in a separate task
    asyncio.create_task(log())
    
@trainlogs.command(name="total_drive_time", description="Show the total driving time from a user's logs")
@app_commands.describe(user="The user whose total driving time you want to see")

async def total_drive_time(ctx: discord.Interaction, user: discord.User = None):
    async def calculate_total_drive_time():
        userid = user if user else ctx.user
        file_path = f'utils/drivelogger/userdata/{userid.name}.csv'
        
        try:
            with open(file_path, mode='r', newline='') as file:
                csv_reader = csv.reader(file)
                total_minutes = 0
                for row in csv_reader:
                    start_time = datetime.strptime(row[4], "%H:%M")
                    end_time = datetime.strptime(row[5], "%H:%M")
                    duration = (end_time - start_time).total_seconds() / 60  # duration in minutes
                    total_minutes += duration
                
                total_hours = total_minutes // 60
                total_minutes = total_minutes % 60
                await ctx.response.send_message(f'Total driving time for {userid.name}: {int(total_hours)} hours and {int(total_minutes)} minutes')
        except FileNotFoundError:
            await ctx.response.send_message(f'{userid.name} has no driving logs!', ephemeral=True)
        except Exception as e:
            await ctx.response.send_message(f'An error occurred: {e}', ephemeral=True)
    
    asyncio.create_task(calculate_total_drive_time())


# train logger reader - log view
@trainlogs.command(name="view", description="View logged flights for a user")
@app_commands.describe(user = "Who do you want to see the data of?", id="The ID of the log you want to view, leave blank to see all logs")

async def userLogs(ctx, user: discord.User=None, id:str=None):
    async def sendLogs():
        if user == None:
                userid = ctx.user
        else:
            userid = user
            
        if id != None:
            file_path = f'utils/trainlogger/userdata/{userid.name}.csv'
                
            
            
            with open(file_path, mode='r', newline='') as file:
                
                if not id.startswith('#'):
                    cleaned_id = '#' + id
                else:
                    cleaned_id = id
                csv_reader = csv.reader(file)
                for row in csv_reader:
                    if row[0] == cleaned_id.upper():
                                        
                            # Make the embed
                        embed = discord.Embed(title=f'Log `{id}`')
                        embed.add_field(name=f'Aircraft', value="{} ({})".format(row[1], row[2]))
                        embed.add_field(name=f'Airline', value="{}".format(row[4]))
                        embed.add_field(name=f'Date', value="{}".format(row[3]))
                        embed.add_field(name=f'Departure', value="{}".format(row[5]))
                        embed.add_field(name=f'Arrival', value="{}".format(row[6]))
                        if row[7]:
                            embed.add_field(name='Notes:', value=row[7])
                        try:
                            embed.set_thumbnail(url=image)
                        except:
                            print('no image')
                        await ctx.response.send_message(embed=embed)
                await ctx.response.send_message(f'Cannot find log `{id}`')
                
        else:            
            if user == None:
                userid = ctx.user
            else:
                userid = user
            
            try:
                file = discord.File(f'utils/trainlogger/userdata/{userid.name}.csv')
            except FileNotFoundError:
                if userid == ctx.user:
                    await ctx.response.send_message("You have no flights logged!",ephemeral=True)
                else:
                    await ctx.response.send_message("This user has no flights logged!",ephemeral=True)
                return
            print(userid.name)
            data = readLogs(userid.name)
            if data == 'no data':
                if userid == ctx.user:
                    await ctx.response.send_message("You have no flights logged!",ephemeral=True)
                else:
                    await ctx.response.send_message("This user has no flights logged!",ephemeral=True)
                return
        
            # create thread
            try:
                logsthread = await ctx.channel.create_thread(
                    name=f'{userid.name}\'s Flight Logs',
                    auto_archive_duration=60,
                    type=discord.ChannelType.public_thread
                )
            except Exception as e:
                await ctx.response.send_message(f"Cannot create thread! Ensure the bot has permission to create threads and that you aren't running this in another thread or DM.\n Error: `{e}`")
                
            # send reponse message
            pfp = userid.avatar.url
            embed=discord.Embed(title='Flight Logs', colour=0x7e3e98)
            embed.set_author(name=userid.name, url='https://xm9g.net', icon_url=pfp)
            embed.add_field(name='Click here to view your logs:', value=f'<#{logsthread.id}>')
            await ctx.response.send_message(embed=embed)
            await logsthread.send(f'# {userid.name}\'s CSV file', file=file)
            await logsthread.send(f'# {userid.name}\'s Flight Logs')
            formatted_data = ""
            for sublist in data:
                if len(sublist) >= 7:  # Ensure the sublist has enough items
                    image = None
                    
                                    
                    #send in thread to reduce spam!
                        # Make the embed
                    embed = discord.Embed(title=f"Log {sublist[0]}")
                    embed.add_field(name=f'Aircraft', value="{} ({})".format(sublist[1], sublist[2]))
                    embed.add_field(name=f'Airline', value="{}".format(sublist[4]))
                    embed.add_field(name=f'Date', value="{}".format(sublist[3]))
                    embed.add_field(name=f'Departure', value="{}".format(sublist[5]))
                    embed.add_field(name=f'Arrival', value="{}".format(sublist[6]))
                    try:
                        embed.set_thumbnail(url=image)
                    except:
                        print('no image')
                    
                    await logsthread.send(embed=embed)
                    # if count == 6:
                    #     await ctx.channel.send('Max of 5 logs can be sent at a time. Use the csv option to see all logs')
                    #     return
            
    asyncio.create_task(sendLogs())



# train logger stats
@trainlogs.command(name="stats", description="View stats for a logged user's flights.")
@app_commands.describe(stat='Type of stats to view', user='Who do you want to see the data of?', format='Diffrent ways and graphs for showing the data.')
@app_commands.choices(stat=[
    app_commands.Choice(name="Airlines", value="airlines"),
    app_commands.Choice(name="Airports", value="airports"),
    app_commands.Choice(name="Trips", value="pairs"),
    # app_commands.Choice(name="Trip Length (VIC train only)", value="length"),
    app_commands.Choice(name="Aircraft", value="aircraft"),
    app_commands.Choice(name="Dates", value="dates"),
    app_commands.Choice(name="Types", value="types"),
    # app_commands.Choice(name="Operators", value="operators"),
])
@app_commands.choices(format=[
    app_commands.Choice(name="List and Bar chart", value="l&g"),
    app_commands.Choice(name="Pie chart", value="pie"),
    app_commands.Choice(name="CSV file", value="csv"),
    app_commands.Choice(name="Daily Chart", value="daily"),
])

async def statTop(ctx: discord.Interaction, stat: str, format: str='l&g', global_stats:bool=False, user: discord.User = None):
    async def sendLogs():
        statSearch = stat
        userid = user if user else ctx.user
        
        if userid.name == 'comeng_17':
            name = 'comeng17'
        else:
            name = userid
            
        if global_stats:
            data = globalTopStats(statSearch)
        else:
            try:
                data = allTopStats(userid.name, statSearch) 
            except:
                await ctx.response.send_message('You have no logged trips!')
        count = 1
        message = ''
        
        # top operators thing:
        if stat == 'operators':
            try:
                pieChart(data, f'Top Operators in Victoria ― {name}', ctx.user.name)
                await ctx.response.send_message(message, file=discord.File(f'temp/Graph{ctx.user.name}.png'))
            except:
                await ctx.response.send_message('User has no logs!')  
        if stat == 'length':
            try:
                lines = data.splitlines()
                chunks = []
                current_chunk = ""
                await ctx.response.send_message('Here are your longest trips in Victoria:')

                for line in lines:
                    # Check if adding this line would exceed the max_length
                    if len(current_chunk) + len(line) + 1 > 1500:  # +1 for the newline character
                        chunks.append(current_chunk)
                        current_chunk = line
                    else:
                        if current_chunk:
                            current_chunk += "\n" + line
                        else:
                            current_chunk = line

                # Add the last chunk
                if current_chunk:
                    chunks.append(current_chunk)
                    
                for i, chunk in enumerate(chunks):
                    await ctx.channel.send(chunk)
                
            except Exception as e:
                await ctx.response.send_message(f"Error: `{e}`")
                
        # make temp csv
        csv_filename = f'temp/top{stat.title()}.{userid}-t{time.time()}.csv'
        with open(csv_filename, mode='w', newline='') as csv_file:
            writer = csv.writer(csv_file)  # Use csv.writer on csv_file, not csvs
            for item in data:
                station, times = item.split(': ')
                writer.writerow([station, times.split()[0]])
        
        if format == 'csv':
            try:
                await ctx.response.send_message("Here is your file:", file=discord.File(csv_filename))
            except:
                ctx.response.send_message('You have no logs!')
            
        elif format == 'l&g':
            await ctx.response.send_message('Here are your stats:')
            for item in data:
                station, times = item.split(': ')
                message += f'{count}. **{station}:** `{times}`\n'
                count += 1
                if len(message) > 1900:
                    await ctx.channel.send(message)
                    message = ''
            try:
                if global_stats:
                    barChart(csv_filename, stat.title(), f'Top {stat.title()} ― Global', ctx.user.name)
                else:
                    barChart(csv_filename, stat.title(), f'Top {stat.title()} ― {name}', ctx.user.name)
                await ctx.channel.send(message, file=discord.File(f'temp/Graph{ctx.user.name}.png'))
            except:
                await ctx.channel.send('User has no logs!')
        elif format == 'pie':
            try:
                if global_stats:
                    pieChart(csv_filename, f'Top {stat.title()} ― {name}', ctx.user.name)
                else:
                    pieChart(csv_filename, f'Top {stat.title()} ― Global', ctx.user.name)

                await ctx.response.send_message(file=discord.File(f'temp/Graph{ctx.user.name}.png'))
            except:
                await ctx.response.send_message('You have no logs!')
        elif format == 'daily':
            if stat != 'dates':
                await ctx.response.send_message('Daily chart can only be used with the stat set to Top Dates')
            try:
                dayChart(csv_filename, ctx.user.name)
                await ctx.response.send_message(file=discord.File(f'temp/Graph{ctx.user.name}.png'))
            except:
                ctx.response.send_message('User has no logs!')
    await sendLogs()


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
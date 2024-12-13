from utils.trainImage import *
from utils.trainlogger.stationDistance import *
import discord

lines_dictionary = {
    'Alamein': [['Richmond', 'East Richmond', 'Burnley', 'Hawthorn', 'Glenferrie', 'Auburn', 'Camberwell', 'Riversdale', 'Willison', 'Hartwell', 'Burwood', 'Ashburton', 'Alamein'],0x01518a],
    'Belgrave': [['Richmond', 'East Richmond', 'Burnley', 'Hawthorn', 'Glenferrie', 'Auburn', 'Camberwell', 'East Camberwell', 'Canterbury', 'Chatham', 'Union', 'Box Hill', 'Laburnum', 'Blackburn', 'Nunawading', 'Mitcham', 'Heatherdale', 'Ringwood', 'Heathmont', 'Bayswater', 'Boronia', 'Ferntree Gully', 'Upper Ferntree Gully', 'Upwey', 'Tecoma', 'Belgrave'],0x01518a],
    'Craigieburn': [['North Melbourne', 'Kensington', 'Newmarket', 'Ascot Vale', 'Moonee Ponds', 'Essendon', 'Glenbervie', 'Strathmore', 'Pascoe Vale', 'Oak Park', 'Glenroy', 'Jacana', 'Broadmeadows', 'Coolaroo', 'Roxburgh Park', 'Craigieburn'],0xfcb818],
    'Cranbourne': [['Richmond', 'South Yarra', 'Malvern', 'Caulfield', 'Carnegie', 'Murrumbeena', 'Hughesdale', 'Oakleigh', 'Huntingdale', 'Clayton', 'Westall', 'Springvale', 'Sandown Park', 'Noble Park', 'Yarraman', 'Dandenong', 'Lynbrook', 'Merinda Park', 'Cranbourne'],0x00a8e4],
    'Flemington Racecourse': [['Flemington Racecourse', 'Showgrounds', 'North Melbourne', 'Southern Cross', 'Flinders Street'],0x8a8c8f],
    'Frankston': [['Flinders Street', 'Richmond', 'South Yarra', 'Hawksburn', 'Toorak', 'Armadale', 'Malvern', 'Caulfield', 'Glen Huntly', 'Ormond', 'McKinnon', 'Bentleigh', 'Patterson', 'Moorabbin', 'Highett', 'Southland', 'Cheltenham', 'Mentone', 'Parkdale', 'Mordialloc', 'Aspendale', 'Edithvale', 'Chelsea', 'Bonbeach', 'Carrum', 'Seaford', 'Kananook', 'Frankston'],0x009645],
    'Glen Waverley': [['Richmond', 'East Richmond', 'Burnley', 'Heyington', 'Kooyong', 'Tooronga', 'Gardiner', 'Glen Iris', 'Darling', 'East Malvern', 'Holmesglen', 'Jordanville', 'Mount Waverley', 'Syndal', 'Glen Waverley'],0x01518a],
    'Hurstbridge': [['Jolimont', 'West Richmond', 'North Richmond', 'Collingwood', 'Victoria Park', 'Clifton Hill', 'Westgarth', 'Dennis', 'Fairfield', 'Alphington', 'Darebin', 'Ivanhoe', 'Eaglemont', 'Heidelberg', 'Rosanna', 'Macleod', 'Watsonia', 'Greensborough', 'Montmorency', 'Eltham', 'Diamond Creek', 'Wattle Glen', 'Hurstbridge'],0xd0202e],
    'Lilydale': [['Richmond', 'East Richmond', 'Burnley', 'Hawthorn', 'Glenferrie', 'Auburn', 'Camberwell', 'East Camberwell', 'Canterbury', 'Chatham', 'Union', 'Box Hill', 'Laburnum', 'Blackburn', 'Nunawading', 'Mitcham', 'Heatherdale', 'Ringwood', 'Ringwood East', 'Croydon', 'Mooroolbark', 'Lilydale'],0x01518a],
    'Mernda': [['Jolimont', 'West Richmond', 'North Richmond', 'Collingwood', 'Victoria Park', 'Clifton Hill', 'Rushall', 'Merri', 'Northcote', 'Croxton', 'Thornbury', 'Bell', 'Preston', 'Regent', 'Reservoir', 'Ruthven', 'Keon Park', 'Thomastown', 'Lalor', 'Epping', 'South Morang', 'Middle Gorge', 'Hawkstowe', 'Mernda'],0xd0202e],
    'Pakenham': [['Richmond', 'South Yarra', 'Malvern', 'Caulfield', 'Carnegie', 'Murrumbeena', 'Hughesdale', 'Oakleigh', 'Huntingdale', 'Clayton', 'Westall', 'Springvale', 'Sandown Park', 'Noble Park', 'Yarraman', 'Dandenong', 'Hallam', 'Narre Warren', 'Berwick', 'Beaconsfield', 'Officer', 'Cardinia Road', 'Pakenham'],0x00a8e4],
    'Sandringham': [['Flinders Street', 'Richmond', 'South Yarra', 'Prahran', 'Windsor', 'Balaclava', 'Ripponlea', 'Elsternwick', 'Gardenvale', 'North Brighton', 'Middle Brighton', 'Brighton Beach', 'Hampton', 'Sandringham'],0xf17fb1],
    'Stony Point': [['Stony Point', 'Crib Point', 'Morradoo', 'Bittern', 'Hastings', 'Tyabb', 'Somerville', 'Baxter', 'Leawarra', 'Frankston'],0x009645],
    'Sunbury': [['North Melbourne', 'Footscray', 'Middle Footscray', 'West Footscray', 'Tottenham', 'Sunshine', 'Albion', 'Ginifer', 'St Albans', 'Keilor Plains', 'Watergardens', 'Diggers Rest', 'Sunbury'],0xfcb818],
    'Upfield': [['North Melbourne', 'Macaulay', 'Flemington Bridge', 'Royal Park', 'Jewell', 'Brunswick', 'Anstey', 'Moreland', 'Coburg', 'Batman', 'Merlynston', 'Fawkner', 'Gowrie', 'Upfield'],0xfcb818],
    'Werribee': [['Flinders Street', 'Southern Cross', 'North Melbourne', 'South Kensington', 'Footscray', 'Seddon', 'Yarraville', 'Spotswood', 'Newport', 'Seaholme', 'Altona', 'Westona', 'Laverton', 'Aircraft', 'Williams Landing', 'Hoppers Crossing', 'Werribee'],0x009645],
    'Williamstown': [['Flinders Street', 'Southern Cross', 'North Melbourne', 'South Kensington', 'Footscray', 'Seddon', 'Yarraville', 'Spotswood', 'Newport', 'North Williamstown', 'Williamstown Beach', 'Williamstown'],0x009645],
    'Unknown/Other':[[None], 0x000000],
}


def logEmbed(row):
    # thing to find image:
    if row[2] == 'Tait':
        image = 'https://railway-photos.xm9g.net/photos/317M-6.webp'
    
    if not '-' in row[1]:
        image = getImage(row[1])

    else:
        hyphen_index = row[1].find("-")
        if hyphen_index != -1:
            first_car = row[1][:hyphen_index]
            print(f'First car: {first_car}')
            image = getImage(first_car)
            if image == None:
                last_hyphen = row[1].rfind("-")
                if last_hyphen != -1:
                    last_car = row[1][last_hyphen + 1 :]  # Use last_hyphen instead of hyphen_index
                    print(f'Last car: {last_car}')
                    image = getImage(last_car)
                    if image == None:
                        image = getImage(row[2])
                        print(f'the loco number is: {row[1]}')
                    
        # Make the embed
    if row[4] in vLineLines:
        embed = discord.Embed(title=f"Log {row[0]}",colour=0x7e3e98)
    elif row[4] == 'Unknown':
            embed = discord.Embed(title=f"Log {row[0]}")
    else:
        try:
            embed = discord.Embed(title=f"Log `{row[0]}`",colour=lines_dictionary[row[4]][1])
        except:
            embed = discord.Embed(title=f'Log `{id}`')
    embed.add_field(name=f'Set', value="{} ({})".format(row[1], row[2]))
    embed.add_field(name=f'Line', value="{}".format(row[4]))
    embed.add_field(name=f'Date', value="{}".format(row[3]))
    embed.add_field(name=f'Trip', value=f"{row[5]} to {row[6]}")
    if row[5] != 'N/A' and row[6] != 'N/A':
        embed.add_field(name='Distance:', value=f'{round(getStationDistance(load_station_data("utils/trainlogger/stationDistances.csv"), row[5], row[6]))}km')
    try:
        embed.set_thumbnail(url=image)
    except:
        print('no image')
        
    return embed
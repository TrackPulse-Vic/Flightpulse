import csv
import os
import discord

def hextodec(hexnum):
    decnum = int(str(hexnum), 16) 
    return decnum

def dectohex(decnum):
    hexnum = hex(decnum)
    return hexnum[2:].upper()

def is_hexadecimal(s):
   for char in s:
      if not char.isalnum(): # Check if the character is a valid hexadecimal digit
         return False
   return True

def addTrain(username, date, train_number, train_type, line, start, end, note):

    # Create a CSV file named after the username
    filename = f"utils/trainlogger/userdata/{username}.csv"
    
    if not os.path.exists(filename):
        # Create the file if it does not exist
        with open(filename, 'w') as file:
            file.write('')  # Write an empty string to create the file
        print(f"File created: {filename}")
    else:
        print(f"File already exists: {filename}")
    
    if date.endswith('-'):
        date = date[:-1]

    id = None

    # Write the data to the CSV file
    try:
        os.listdir('utils\\trainlogger\\userdata')
    except FileNotFoundError:
        os.mkdir('utils/trainlogger/userdata')
        id = 0

    with open(filename, 'r+', newline='') as file:
        data = file.readlines()
        if data == []:
            id = 0
        else:
            id = data[-1].split(',')[0][1:]
    
    id = dectohex(hextodec(id)+1)
    
    with open(filename, 'a', newline='') as file:
        writer = csv.writer(file)
        # file.write('\n')
        writer.writerow([f'#{id}',date, train_number,train_type, line, start, end, note])


    print(f"Data saved to {filename}")
    return id

# Tram version:
def addTram(username, date, train_number, train_type, line, start, end):

    # Create a CSV file named after the username
    filename = f"utils/trainlogger/userdata/tram/{username}.csv"
    
    if not os.path.exists(filename):
        # Create the file if it does not exist
        with open(filename, 'w') as file:
            file.write('')  # Write an empty string to create the file
        print(f"File created: {filename}")
    else:
        print(f"File already exists: {filename}")
    
    if date.endswith('-'):
        date = date[:-1]

    id = None

    # Write the data to the CSV file
    try:
        os.listdir('utils\\trainlogger\\userdata\\tram')
    except FileNotFoundError:
        os.mkdir('utils/trainlogger/userdata/tram')
        id = 0

    with open(filename, 'r+', newline='') as file:
        data = file.readlines()
        if data == []:
            id = 0
        else:
            id = data[-1].split(',')[0][1:]
    
    id = dectohex(hextodec(id)+1)
    
    with open(filename, 'a', newline='') as file:
        writer = csv.writer(file)
        # file.write('\n')
        writer.writerow([f'#{id}',date, train_number,train_type, line, start, end])


    print(f"Data saved to {filename}")
    return id

def addSydneyTrain(username, date, train_number, train_type, line, start, end):

    # Create a CSV file named after the username
    filename = f"utils/trainlogger/userdata/sydney-trains/{username}.csv"
    
    if not os.path.exists(filename):
        # Create the file if it does not exist
        with open(filename, 'w') as file:
            file.write('')  # Write an empty string to create the file
        print(f"File created: {filename}")
    else:
        print(f"File already exists: {filename}")
    
    if date.endswith('-'):
        date = date[:-1]

    id = None

    # Write the data to the CSV file
    try:
        os.listdir('utils\\trainlogger\\userdata\\sydney-trains')
    except FileNotFoundError:
        os.mkdir('utils/trainlogger/userdata/sydney-trains')
        id = 0

    with open(filename, 'r+', newline='') as file:
        data = file.readlines()
        if data == []:
            id = 0
        else:
            id = data[-1].split(',')[0][1:]
    
    id = dectohex(hextodec(id)+1)
    
    with open(filename, 'a', newline='') as file:
        writer = csv.writer(file)
        # file.write('\n')
        writer.writerow([f'#{id}',date, train_number,train_type, line, start, end])


    print(f"Data saved to {filename}")
    return id

def addBus(username, date, train_number, train_type, line, start, end, operator):

    # Create a CSV file named after the username
    filename = f"utils/trainlogger/userdata/bus/{username}.csv"
    
    if not os.path.exists(filename):
        # Create the file if it does not exist
        with open(filename, 'w') as file:
            file.write('')  # Write an empty string to create the file
        print(f"File created: {filename}")
    else:
        print(f"File already exists: {filename}")
    
    if date.endswith('-'):
        date = date[:-1]

    id = None

    # Write the data to the CSV file
    try:
        os.listdir('utils\\trainlogger\\userdata\\bus')
    except FileNotFoundError:
        os.mkdir('utils/trainlogger/userdata/bus')
        id = 0

    with open(filename, 'r+', newline='') as file:
        data = file.readlines()
        if data == []:
            id = 0
        else:
            id = data[-1].split(',')[0][1:]
    
    id = dectohex(hextodec(id)+1)
    
    with open(filename, 'a', newline='') as file:
        writer = csv.writer(file)
        # file.write('\n')
        writer.writerow([f'#{id}',date, train_number,train_type, line, start, end, operator])


    print(f"Data saved to {filename}")
    return id
# B
def addFlight(username, date, train_number, train_type, line, start, end, operator):

    # Create a CSV file named after the username
    filename = f"utils/trainlogger/userdata/flights/{username}.csv"
    
    if not os.path.exists(filename):
        # Create the file if it does not exist
        with open(filename, 'w') as file:
            file.write('')  # Write an empty string to create the file
        print(f"File created: {filename}")
    else:
        print(f"File already exists: {filename}")
    
    if date.endswith('-'):
        date = date[:-1]

    id = None

    # Write the data to the CSV file
    try:
        os.listdir('utils\\trainlogger\\userdata\\flights')
    except FileNotFoundError:
        os.mkdir('utils/trainlogger/userdata/flights')
        id = 0

    with open(filename, 'r+', newline='') as file:
        data = file.readlines()
        if data == []:
            id = 0
        else:
            id = data[-1].split(',')[0][1:]
    
    id = dectohex(hextodec(id)+1)
    
    with open(filename, 'a', newline='') as file:
        writer = csv.writer(file)
        # file.write('\n')
        writer.writerow([f'#{id}',date, train_number,train_type, line, start, end, operator])


    print(f"Data saved to {filename}")
    return id


def addSydneyTram(username, date, train_number, train_type, line, start, end):

    # Create a CSV file named after the username
    filename = f"utils/trainlogger/userdata/sydney-trams/{username}.csv"
    
    if not os.path.exists(filename):
        # Create the file if it does not exist
        with open(filename, 'w') as file:
            file.write('')  # Write an empty string to create the file
        print(f"File created: {filename}")
    else:
        print(f"File already exists: {filename}")
    
    if date.endswith('-'):
        date = date[:-1]

    id = None

    # Write the data to the CSV file
    try:
        os.listdir('utils\\trainlogger\\userdata\\sydney-trams')
    except FileNotFoundError:
        os.mkdir('utils/trainlogger/userdata/sydney-trams')
        id = 0

    with open(filename, 'r+', newline='') as file:
        data = file.readlines()
        if data == []:
            id = 0
        else:
            id = data[-1].split(',')[0][1:]
    
    id = dectohex(hextodec(id)+1)
    
    with open(filename, 'a', newline='') as file:
        writer = csv.writer(file)
        # file.write('\n')
        writer.writerow([f'#{id}',date, train_number,train_type, line, start, end])


    print(f"Data saved to {filename}")
    return id

def addAdelaideTrain(username, date, train_number, train_type, line, start, end):

    # Create a CSV file named after the username
    filename = f"utils/trainlogger/userdata/adelaide-trains/{username}.csv"
    
    if not os.path.exists(filename):
        # Create the file if it does not exist
        with open(filename, 'w') as file:
            file.write('')  # Write an empty string to create the file
        print(f"File created: {filename}")
    else:
        print(f"File already exists: {filename}")
    
    if date.endswith('-'):
        date = date[:-1]

    id = None

    # Write the data to the CSV file
    try:
        os.listdir('utils\\trainlogger\\userdata\\adelaide-trains')
    except FileNotFoundError:
        os.mkdir('utils/trainlogger/userdata/adelaide-trains')
        id = 0

    with open(filename, 'r+', newline='') as file:
        data = file.readlines()
        if data == []:
            id = 0
        else:
            id = data[-1].split(',')[0][1:]
    
    id = dectohex(hextodec(id)+1)
    
    with open(filename, 'a', newline='') as file:
        writer = csv.writer(file)
        # file.write('\n')
        writer.writerow([f'#{id}',date, train_number,train_type, line, start, end])


    print(f"Data saved to {filename}")
    return id

def readLogs(username):

    # Create the filename based on the username
    filename = f"utils/trainlogger/userdata/{username}.csv"
    user_data = []

    try:
        # Open the CSV file and read the data
        with open(filename, 'r', newline='') as file:
            reader = csv.reader(file)
            user_data = list(reader)
            # data = file.readlines()
            # print(data)
            if user_data == []:
                return 'no data'
        
        # Return the data instead of printing it
        if len(user_data) > 0:
            return user_data[::-1] 
        else:
            return []
    except FileNotFoundError:
        print(f"File {filename} not found.")
        return []
 
def readTramLogs(username):
    # Create the filename based on the username
    filename = f"utils/trainlogger/userdata/tram/{username}.csv"
    user_data = []

    try:
        # Open the CSV file and read the data
        with open(filename, 'r', newline='') as file:
            reader = csv.reader(file)
            user_data = list(reader)
            # data = file.readlines()
            # print(data)
            if user_data == []:
                return 'no data'
        
        # Return the data instead of printing it
        if len(user_data) > 0:
            return user_data[::-1]
        else:
            return []
    except FileNotFoundError:
        print(f"File {filename} not found.")
        return []

def readSydneyTrainLogs(username):
    # Create the filename based on the username
    filename = f"utils/trainlogger/userdata/sydney-trains/{username}.csv"
    user_data = []

    try:
        # Open the CSV file and read the data
        with open(filename, 'r', newline='') as file:
            reader = csv.reader(file)
            user_data = list(reader)
            # data = file.readlines()
            # print(data)
            if user_data == []:
                return 'no data'
        
        # Return the data instead of printing it
        if len(user_data) > 0:
            return user_data[::-1]
        else:
            return []
    except FileNotFoundError:
        print(f"File {filename} not found.")
        return []
    
def readSydneyLightRailLogs(username):
    # Create the filename based on the username
    filename = f"utils/trainlogger/userdata/sydney-trams/{username}.csv"
    user_data = []

    try:
        # Open the CSV file and read the data
        with open(filename, 'r', newline='') as file:
            reader = csv.reader(file)
            user_data = list(reader)
            # data = file.readlines()
            # print(data)
            if user_data == []:
                return 'no data'
        
        # Return the data instead of printing it
        if len(user_data) > 0:
            return user_data[::-1]
        else:
            return []
    except FileNotFoundError:
        print(f"File {filename} not found.")
        return []

def readBusLogs(username):
    # Create the filename based on the username
    filename = f"utils/trainlogger/userdata/bus/{username}.csv"
    user_data = []

    try:
        # Open the CSV file and read the data
        with open(filename, 'r', newline='') as file:
            reader = csv.reader(file)
            user_data = list(reader)
            # data = file.readlines()
            # print(data)
            if user_data == []:
                return 'no data'
        
        # Return the data instead of printing it
        if len(user_data) > 0:
            return user_data[::-1]
        else:
            return []
    except FileNotFoundError:
        print(f"File {filename} not found.")
        return []

def readAdelaideLogs(username):
    # Create the filename based on the username
    filename = f"utils/trainlogger/userdata/adelaide-trains/{username}.csv"
    user_data = []

    try:
        # Open the CSV file and read the data
        with open(filename, 'r', newline='') as file:
            reader = csv.reader(file)
            user_data = list(reader)
            # data = file.readlines()
            # print(data)
            if user_data == []:
                return 'no data'
        
        # Return the data instead of printing it
        if len(user_data) > 0:
            return user_data[::-1]
        else:
            return []
    except FileNotFoundError:
        print(f"File {filename} not found.")
        return []

# same as one above but only reads the row you put in   
def readRow(username, logid):
    try:
        os.listdir('utils\\trainlogger\\userdata')
    except FileNotFoundError:
        return 'no data at all'
    
    # Create the filename based on the username
    filename = f"utils/trainlogger/userdata/{username}.csv"

    # Open the CSV file and read the data
    with open(filename, 'r', newline='') as file:
        data = file.readlines()

        if data == []:
            return 'no data for user'
        else:
            if logid == 'LAST':
                id = data[-1].split(',')[0][1:]
            else:
                id = logid
            row = None
            for r in data:
                if r.split(',')[0] == f'#{id}':
                    row = r
                    break
            if row == None:
                return 'invalid id did not show up'
            else:
                return row

# same as the other but it works for all modes
def universalReadRow(username, logid, mode):
    try:
        os.listdir('utils\\trainlogger\\userdata')
    except FileNotFoundError:
        return 'no data at all'
    
    # Create the filename based on the username
    if mode == 'train':
        filename = f"utils/trainlogger/userdata/{username}.csv"
    else:
        filename = f"utils/trainlogger/userdata/{mode}/{username}.csv"

    # Open the CSV file and read the data
    with open(filename, 'r', newline='') as file:
        data = file.readlines()

        if data == []:
            return 'no data for user'
        else:
            if logid == 'LAST':
                id = data[-1].split(',')[0][1:]
            else:
                id = logid
            row = None
            for r in data:
                if r.split(',')[0] == f'#{id}':
                    row = r
                    break
            if row == None:
                return 'invalid id did not show up'
            else:
                return row
        
def deleteRow(username, logid, mode):
    # Create the filename based on the username
    if mode == 'train':
        filename = f"utils/trainlogger/userdata/{username}.csv"
    else:
        filename = f"utils/trainlogger/userdata/{mode}/{username}.csv"
        
    # Open the CSV file and read the data
    with open(filename, 'r+', newline='') as file:
        data = file.readlines()

        if logid == 'LAST':
            id = data[-1].split(',')[0][1:]
        else:
            id = logid
        
        file.truncate(0)
        file.seek(0)
        
        for r in data:
            if r.split(',')[0] != f'#{id}':
                file.write(r)
                
        return id
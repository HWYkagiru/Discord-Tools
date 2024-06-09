import requests
from colorama import Fore, Style
from datetime import datetime
import os
"""
Copyright 2024 Developed by Kagiru.
This Tool is freely available on my GitHub: https://github.com/HWYkagiru/Discord-Tools.
If you modify and distribute this tool, giving credits would be greatly appreciated.
"""

def friendsprint(friend):
    username = friend.get('user', {}).get('username', 'Unknown')
    global_name = friend.get('user', {}).get('global_name', 'Unknown')
    friend_id = friend.get('id', 'Unknown')
    since = friend.get('since', 'Unknown')
    
    if since != 'Unknown':
        since_date = datetime.strptime(since, "%Y-%m-%dT%H:%M:%S.%f%z")
        sincef = since_date.strftime("%Y-%m-%d")
    else:
        sincef = 'Unknown'
        
    print(f"{Fore.GREEN}{username} {Fore.WHITE}|{Fore.CYAN} {global_name} {Fore.WHITE}|{Fore.CYAN} {friend_id} {Fore.WHITE}|{Fore.CYAN} Friends Since: {sincef}")

def guildinfoprint(guild):
    guild_name = guild.get('name', 'Unknown')
    guild_id = guild.get('id', 'Unknown')
    print(f"{Fore.GREEN}{guild_name} {Fore.WHITE}|{Fore.CYAN} {guild_id}")

def printdata(data, data_type):
    if isinstance(data, dict):
        for key, value in data.items():
            if isinstance(value, dict) or isinstance(value, list):
                printdata(value, data_type)
            else:
                print(f"{Fore.GREEN}{key}: {Fore.CYAN}{value}{Style.RESET_ALL}")
    elif isinstance(data, list):
        if data_type == "friends":
            for friend in data:
                friendsprint(friend)
        elif data_type == "guilds":
            for guild in data:
                guildinfoprint(guild)

def getguilds(token):
    headers = {
        'Authorization': token
    }
    response = requests.get('https://discord.com/api/v9/users/@me/guilds', headers=headers)
    if response.status_code == 200:
        guildsdata = response.json()
        return guildsdata
    else:
        return None

def maininfo(token):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:124.0) Gecko/20100101 Firefox/124.0',
        'Accept': '*/*',
        'Authorization': token,
    }

    userurl = "https://discord.com/api/v9/users/@me"

    try:
        res = requests.get(userurl, headers=headers)
        if res.status_code == 200:
            data = res.json()
            print(Fore.GREEN + Style.BRIGHT + "Main-Info:\n" + Style.RESET_ALL)
            printdata(data, "main")
        else:
            print(f"{Fore.CYAN}{Style.BRIGHT}[-] {Fore.RED}Invalid Token{Style.RESET_ALL}")
    except Exception:
        print(f"MainInfoError")

def friendinfo(token):
    headers = {
        'Authorization': token
    }
    response = requests.get('https://discord.com/api/v9/users/@me/relationships', headers=headers)
    if response.status_code == 200:
        friendsdata = response.json()
        friendsamount = len(friendsdata)
        print(Fore.GREEN + Style.BRIGHT + f"\nFriendsInfo: {Fore.BLUE}{friendsamount}\n" + Style.RESET_ALL)
        printdata(friendsdata, "friends")
    else:
        return None

def guildinfo(token):
    headers = {
        'Authorization': token
    }
    response = requests.get('https://discord.com/api/v9/users/@me/guilds', headers=headers)
    if response.status_code == 200:
        guildsdata = response.json()
        print(Fore.GREEN + Style.BRIGHT + "\nGuildsInfo:\n" + Style.RESET_ALL)
        printdata(guildsdata, "guilds")
    else:
        return None
    
if __name__ == "__main__":
    os.system("cls" if os.name == "nt" else "clear")
    token = input(f"{Fore.CYAN}Discord Token: ")
    maininfo(token)
    friendinfo(token)
    guildinfo(token)
    input(f"\n{Fore.BLUE}Press Enter to Exit...{Fore.RESET}")
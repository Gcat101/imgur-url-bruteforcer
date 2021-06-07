import urllib.request 
import json
import random 

url = input('Input link (the last part): ')
url = url.lower()
mode = input('Url contains /a/ or /gallery/ (input "a" or "gallery"): ')
correcturl = False
truelink = ''

while (correcturl == False):
    urltry = list(url)
    for i in urltry:
        if (random.randint(0, 1) == 1):
            urltry[urltry.index(i)] = urltry[urltry.index(i)].upper()
    urltry = ''.join(urltry)

    if (mode == 'gallery'):
        try:
            with urllib.request.urlopen("https://api.imgur.com/post/v1/posts/" + urltry + "?client_id=546c25a59c58ad7&include=media%2Ctags%2Caccount%2Cadconfig%2Cpromoted") as link:
                data = json.loads(url.read().decode())
        except urllib.error.HTTPError:
            print(f'{urltry} - Failed')
        except AttributeError:
            print(f'{urltry} - Success!')
            truelink = f'\n https://imgur.com/gallery/{urltry} is the right url!'
            break

    if (mode == 'a'):
        try:
            with urllib.request.urlopen("https://api.imgur.com/post/v1/albums/" + urltry + "?client_id=546c25a59c58ad7&include=media%2Cadconfig%2Caccount") as link:
                data = json.loads(url.read().decode())
        except urllib.error.HTTPError:
            print(f'{urltry} - Failed')
        except AttributeError:
            print(f'{urltry} - Success!')
            truelink = f'\n https://imgur.com/a/{urltry} is the right url!'
            break

print(truelink)

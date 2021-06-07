import urllib.request 
import json
import random 

url = input('Input link (the last part): ')
url = url.lower()
mode = input('Url contains /a/, /gallery/, none or any if you dont know (input "a"/"gallery"/"none"/"any"): ')
mode = mode.lower()
if (mode == "any"): print('Warning! "Any" mode is pretty slow. Try spesific mode if you want to go faster.')
printfail = input('Do you want to print failed attempts (y/n)? ')
printfail = printfail.lower()
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
            if (printfail == 'y'):
                print(f'{urltry} - Failed')
        except AttributeError:
            print(f'{urltry} - Success!')
            truelink = f'\n https://imgur.com/gallery/{urltry} is the right url!'
            break

    elif (mode == 'a'):
        try:
            with urllib.request.urlopen("https://api.imgur.com/post/v1/albums/" + urltry + "?client_id=546c25a59c58ad7&include=media%2Cadconfig%2Caccount") as link:
                data = json.loads(url.read().decode())
        except urllib.error.HTTPError:
            if (printfail == 'y'):
                print(f'{urltry} - Failed')
        except AttributeError:
            print(f'{urltry} - Success!')
            truelink = f'\n https://imgur.com/a/{urltry} is the right url!'
            break

    elif (mode == 'none'):
        try:
            with urllib.request.urlopen("https://api.imgur.com/post/v1/media/" + urltry + "?client_id=546c25a59c58ad7&include=media%2Cadconfig%2Caccount") as link:
                data = json.loads(url.read().decode())
        except urllib.error.HTTPError:
            if (printfail == 'y'):
                print(f'{urltry} - Failed')
        except AttributeError:
            print(f'{urltry} - Success!')
            truelink = f'\n https://imgur.com/{urltry} is the right url!'
            break

    elif (mode == 'any'):
        try:
            with urllib.request.urlopen("https://api.imgur.com/post/v1/posts/" + urltry + "?client_id=546c25a59c58ad7&include=media%2Ctags%2Caccount%2Cadconfig%2Cpromoted") as link:
                data = json.loads(url.read().decode())
        except urllib.error.HTTPError:
            if (printfail == 'y'):
                print(f'gallery/{urltry} - Failed')
        except AttributeError:
            print(f'gallery/{urltry} - Success!')
            truelink = f'\n https://imgur.com/gallery/{urltry} is the right url!'
            break

        try:
            with urllib.request.urlopen("https://api.imgur.com/post/v1/albums/" + urltry + "?client_id=546c25a59c58ad7&include=media%2Cadconfig%2Caccount") as link:
                data = json.loads(url.read().decode())
        except urllib.error.HTTPError:
            if (printfail == 'y'):
                print(f'a/{urltry} - Failed')
        except AttributeError:
            print(f'a/{urltry} - Success!')
            truelink = f'\n https://imgur.com/a/{urltry} is the right url!'
            break

        try:
            with urllib.request.urlopen("https://api.imgur.com/post/v1/media/" + urltry + "?client_id=546c25a59c58ad7&include=media%2Cadconfig%2Caccount") as link:
                data = json.loads(url.read().decode())
        except urllib.error.HTTPError:
            if (printfail == 'y'):
                print(f'/{urltry} - Failed')
        except AttributeError:
            print(f'/{urltry} - Success!')
            truelink = f'\n https://imgur.com/{urltry} is the right url!'
            break

print(truelink)
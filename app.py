import requests

url = input('Input link (the last part): ')
url = url.lower()
mode = input('Url contains /a/, /gallery/, none or any if you dont know (input "a"/"gallery"/"none"/"any"): ')
mode = mode.lower()
if (mode == "any"): print('\nWarning! "Any" mode is pretty slow. Try spesific mode if you want to go faster.\n')
printfail = input('Do you want to print failed attempts (y/n)? ')
printfail = printfail.lower()
correcturl = False
truelink = ''

def permute(inp):
    possble = []
    n = len(inp)
  
    mx = 1 << n
  
    inp = inp.lower()
     
    for i in range(mx):
        combination = [k for k in inp]
        for j in range(n):
            if (((i >> j) & 1) == 1):
                combination[j] = inp[j].upper()
  
        temp = ""
        for i in combination:
            temp += i
        possble.append(temp)
    return possble

posurls = (permute(url))

for urltry in posurls:

    if (mode == 'gallery'):
        page = requests.get("https://api.imgur.com/post/v1/posts/" + urltry + "?client_id=546c25a59c58ad7&include=media%2Ctags%2Caccount%2Cadconfig%2Cpromoted")
        if (page.status_code == 404):
            if (printfail == 'y'):
                print(f'{urltry} - Failed')
        else:
            print(f'{urltry} - Success!')
            truelink = f'\n https://imgur.com/gallery/{urltry} is the right url!'
            correcturl = True
            break

    elif (mode == 'a'):
        page("https://api.imgur.com/post/v1/albums/" + urltry + "?client_id=546c25a59c58ad7&include=media%2Cadconfig%2Caccount")
        if (page.status_code == 404):
            if (printfail == 'y'):
                print(f'{urltry} - Failed')
        else:
            print(f'{urltry} - Success!')
            truelink = f'\n https://imgur.com/a/{urltry} is the right url!'
            correcturl = True
            break

    elif (mode == 'none'):
        page = requests.get("https://api.imgur.com/post/v1/media/" + urltry + "?client_id=546c25a59c58ad7&include=media%2Cadconfig%2Caccount")
        if (page.status_code == 404):
            if (printfail == 'y'):
                print(f'{urltry} - Failed')
        else:
            print(f'{urltry} - Success!')
            truelink = f'\n https://imgur.com/{urltry} is the right url!'
            correcturl = True
            break

    elif (mode == 'any'):
        page = requests.get("https://api.imgur.com/post/v1/posts/" + urltry + "?client_id=546c25a59c58ad7&include=media%2Ctags%2Caccount%2Cadconfig%2Cpromoted")
        if (page.status_code == 404):
            if (printfail == 'y'):
                print(f'gallery/{urltry} - Failed')
        else:
            print(f'gallery/{urltry} - Success!')
            truelink = f'\n https://imgur.com/gallery/{urltry} is the right url!'
            correcturl = True
            break

        page("https://api.imgur.com/post/v1/albums/" + urltry + "?client_id=546c25a59c58ad7&include=media%2Cadconfig%2Caccount")
        if (page.status_code == 404):
            if (printfail == 'y'):
                print(f'a/{urltry} - Failed')
        else:
            print(f'a/{urltry} - Success!')
            truelink = f'\n https://imgur.com/a/{urltry} is the right url!'
            correcturl = True
            break

        page = requests.get("https://api.imgur.com/post/v1/media/" + urltry + "?client_id=546c25a59c58ad7&include=media%2Cadconfig%2Caccount")
        if (page.status_code == 404):
            if (printfail == 'y'):
                print(f'/{urltry} - Failed')
        else:
            print(f'/{urltry} - Success!')
            truelink = f'\n https://imgur.com/{urltry} is the right url!'
            correcturl = True
            break

    else:
        print("You've chosen an invalid mode, try again")
        correcturl = True
        break

if (correcturl == False):
    print("Hmmmm.... This doesn't seem like an imgur link... Check the link that you've inputed and the mode you've chosen.")
else:
    print(truelink)
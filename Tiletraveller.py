# Þetta virkar í Mímir :) kv. Daníel
n = '(N)orth'
s = '(S)outh'
w = '(W)est'
e = '(E)ast'
o = ' or '
d = '.'
tile1 = 1
tile2 = 1
travel = ''
bla = True

while bla:
    if travel == 'n' or travel == 'N':
        tile2 += 1

    elif travel == 's' or travel == 'S':
        tile2 += -1   

    elif travel == 'e' or travel == 'E':
        tile1 += 1
    
    elif travel == 'w' or travel == 'W':
        tile1 += -1
        
    if (tile1,tile2) == (1,1):
        print("You can travel: "+n + d)
        travel = input("Direction: ")
        if travel != 'n' and travel != 'N':
            print('Not a valid direction!')
            travel = ""
            direction = ''
        else:
            direction = ''
            
    if (tile1,tile2) == (1,2):
        print("You can travel: "+n + o + e + o + s + d)
        travel = input("Direction: ")
        if travel != 'n' and travel != 'N' and travel != 'e' and travel != 'E' and travel != 's' and travel != 'S':
            print('Not a valid direction!')
            travel = ""
            direction = ''
        else:
            direction = ''
            
    if (tile1,tile2) == (1,3):
        print("You can travel: "+e + o + s + d)
        travel = input("Direction: ")
        if travel != 'e' and travel != 'E' and travel != 's' and travel != 'S':
            print('Not a valid direction!')
            travel = ""
            direction = ""
        else:
            direction = ''
            
    if (tile1,tile2) == (2,1):
        print("You can travel: "+n + d)
        travel = input("Direction: ")
        if travel != 'n' and travel != 'N':
            print('Not a valid direction!')
            travel = ""
            direction = ''
        else:
            direction = ''
            
    if (tile1,tile2) == (2,2):
        print("You can travel: "+s + o + w + d)
        travel = input("Direction: ")
        if travel != 'w' and travel != 'W' and travel != 's' and travel != 'S':
            print('Not a valid direction!')
            travel = ""
            direction = ''
        else:
            direction = ''
            
    if (tile1,tile2) == (2,3):
        print("You can travel: "+e + o + w + d)
        travel = input("Direction: ")
        if travel != 'w' and travel != 'W' and travel != 'e' and travel != 'E':
            print('Not a valid direction!')
            travel = ""
            direction = ''
        else:
            direction = ''
            
    if (tile1,tile2) == (3,1):
        print('Victory!')
        bla = not bla
        break
    
    if (tile1,tile2) == (3,3):
        print("You can travel: "+s + o + w + d)
        travel = input("Direction: ")
        if travel != 'w' and travel != 'W' and travel != 's' and travel != 'S':
            print('Not a valid direction!')
            travel = ""
            direction = ''
        else:
            direction = ''
    
    if (tile1,tile2) == (3,2):
        print("You can travel: "+n + o + s + d)
        travel = input("Direction: ")
        if travel != 'n' and travel != 'N' and travel != 's' and travel != 'S':
            print('Not a valid direction!')
            travel = ""
            direction = ''
        else:
            direction = ''

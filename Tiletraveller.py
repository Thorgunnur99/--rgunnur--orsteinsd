tile1 = 1
tile2 = 1

travel = input('You can travel: (N)orth.')

while tile1 != 3 and tile2 !=1:
if travel == 'n' or travel == 'N' and tile1 != 3 and (tile1,tile2) != (2,2):
    tile1 += 1

elif travel == 's' or travel == 'S' and tile1 != 1 and (tile1,tile2) != (2,3):
    tile1 -= 1   

elif travel == 'e' or travel == 'E' and tile2 != 3 and (tile1,tile2) != (2,2) and (tile1,tile2) != (2,1):
    tile2 += 1
    
elif travel == 'w' or travel == 'W' and tile2 != 1 and (tile1,tile2) != (2,1) and (tile1,tile2) != (3,2):
    tile2 -= 1
n = '(N)orth'
s = '(S)outh'
w = '(W)est'
e = '(E)ast'
o = ' or '
d = '.'

if (tile1,tile2) == (1,1) or (tile1,tile2) == (2,1):
    direction = n + d
    travel = input('You can travel: {}'.format(direction))
    direction = ''
    if travel != 'n' travel != 'N':
        print('Not a valid direction!')
        travel = input('You can travel: {}'.format(direction))
        direction = ''

if (tile1,tile2) == (1,2):
    direction = n + o + e + o + s + d
    travel = input('You can travel: {}'.format(direction))
    direction = ''
    if travel == 'W' or travel == 'w':
        print('Not a valid direction!')
        travel = input('You can travel: {}'.format(direction))
        direction = ''

if (tile1,tile2) == (1,3):
    direction = e + o + s + d
    travel = input('You can travel: {}'.format(direction))
    direction = ''
    if travel != 'n' or travel != 'N' or travel == 'w' or travel == 'W'
        print('Not a valid direction!')
        travel = input('You can travel: {}'.format(direction))
        direction = ''
        
if (tile1,tile2) == (2,1):
    direction = n + d
    travel = input('You can travel: {}'.format(direction))
    direction = ''
    if travel != 'n' travel != 'N'
        print('Not a valid direction!')
        travel = input('You can travel: {}'.format(direction))
        direction = ''

if (tile1,tile2) == (2,2):
    direction = w + o + s + d
    travel = input('You can travel: {}'.format(direction))
    direction = ''
    if travel != 'w' or travel != 'W' or travel != 's' or travel != 'S'
        print('Not a valid direction!')
        travel = input('You can travel: {}'.format(direction))
        direction = ''

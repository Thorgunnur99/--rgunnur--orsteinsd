"""

In this assignment, you work in groups of 2-3 students each and apply pair programing. Moreover, you need to use git during the development of your solution.

The assignment is to develop a computer game in which the player is located in a certain tile in a grid.  At each iteration, the program displays the directions for which there are adjacent tiles that the player can travel to.  

The program only displays text, so you don’t actually draw the tile grid, but the program should behave as if the player is in a 3x3 grid with open and closed walls as seen in the following image:

The player starts in tile (1,1). At the beginning, and after each move selected by the player, the program should print the player’s travel options. If there is an open wall in a direction, write that direction as a possible travel direction.

At each iteration, the player enters the first letter of the direction he/she wishes to travel, after which the player should be located in another tile and the options for the new tile are then printed out.

The player enters:

n/N for north (up)
e/E for east (right)
s/S for south (down)
w/W for west (left)
If the player enters an invalid direction, the program prints “Not a valid direction!” and allows the player to enter the direction again.

For example, in tile (1,1) it’s only possible to move north. In tile (1,2), the possible moves are north, east and south, and in tile (3,3) the valid moves are south and west.

Tile (3,1) is the victory location.  When the player enters this tile, the program should notify him/her of their victory and quit running.

Example run:
"""

n = '(N)orth'
s = '(S)outh'
w = '(W)est'
e = '(E)ast'
o = ' or '
d = '.'
tile1 = 1
tile2 = 1
travel = ''

while tile1 != 3 and tile2 !=1:
    if travel == 'n' or travel == 'N':
        tile1 += 1

    elif travel == 's' or travel == 'S':
        tile1 += -1   

    elif travel == 'e' or travel == 'E':
        tile2 += 1
    
    elif travel == 'w' or travel == 'W':
        tile2 += -1
        
    if (tile1,tile2) == (1,1) or (tile1,tile2) == (2,1):
        direction = n + d
        travel = input('You can travel:',direction)
        if travel != 'n' and travel != 'N':
            print('Not a valid direction!')
            travel = input('You can travel: {}'.format(direction))
            direction = ''
        else:
            direction = ''
            
    if (tile1,tile2) == (1,2):
        direction = n + o + e + o + s + d
        travel = input('You can travel: {}'.format(direction))
        if travel == 'W' or travel == 'w':
            print('Not a valid direction!')
            travel = input('You can travel: {}'.format(direction))
            direction = ''
        else:
            direction = ''
            
    if (tile1,tile2) == (1,3):
        direction = e + o + s + d
        travel = input('You can travel: {}'.format(direction))
        if travel == 'n' or travel == 'N' or travel == 'w' or travel == 'W':
            print('Not a valid direction!')
            travel = input('You can travel: {}'.format(direction))
            direction = ''
        else:
            direction = ''
            
    if (tile1,tile2) == (2,1):
        direction = n + d
        travel = input('You can travel: {}'.format(direction))
        if travel != 'n' and travel != 'N':
            print('Not a valid direction!')
            travel = input('You can travel: {}'.format(direction))
            direction = ''
        else:
            direction = ''
            
    if (tile1,tile2) == (2,2):
        direction = w + o + s + d
        travel = input('You can travel: {}'.format(direction))
        if travel == 'e' or travel == 'E' or travel == 'n' or travel == 'N':
            print('Not a valid direction!')
            travel = input('You can travel: {}'.format(direction))
            direction = ''
        else:
            direction = ''
            
    if (tile1,tile2) == (2,3):
        direction = w + o + e + d
        travel = input('You can travel: {}'.format(direction))
        if travel == 's' or travel == 'S' or travel == 'n' or travel == 'N':
            print('Not a valid direction!')
            travel = input('You can travel: {}'.format(direction))
            direction = ''
        else:
            direction = ''
            
    if (tile1,tile2) == (3,1):
        print('Victory!')
        break
    
    if (tile1,tile2) == (3,3):
        direction = w + o + s + d
        travel = input('You can travel: {}'.format(direction))
        if travel == 'n' or travel == 'N' or travel == 'e' or travel == 'E':
            print('Not a valid direction!')
            travel = input('You can travel: {}'.format(direction))
            direction = ''
        else:
            direction = ''
    
    if (tile1,tile2) == (3,2):
        direction = n + o + s + d
        travel = input('You can travel: {}'.format(direction))
        if travel == 'n' or travel == 'N' or travel == 'e' or travel == 'E':
            print('Not a valid direction!')
            travel = input('You can travel: {}'.format(direction))
            direction = ''
        else:
            direction = ''
"""
You can travel: (N)orth.
Direction: s
Not a valid direction!
You can travel: (N)orth.
Direction: n
You can travel: (N)orth or (E)ast or (S)outh.
Direction: N
You can travel: (E)ast or (S)outh.
Direction: w
Not a valid direction!
You can travel: (E)ast or (S)outh.
Direction: E
You can travel: (E)ast or (W)est.
Direction: e
You can travel: (S)outh or (W)est.
Direction: s
You can travel: (N)orth or (S)outh.
Direction: S
Victory!
"""

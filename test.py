from visual import *
import random
import time

spheren = []

count = 0


# Setup random position, scale, color, opacity....
def getrand(randType):
    if randType == 'pos':
        return(random.randint(-128, 128))
    if randType == 'radius':
        return(random.randint(1, 5))
    if randType == 'color':
        return(random.random())
    if randType == 'opacity':
        return(random.random())
    else:
        print('Fail, not a valid randType, you passed in: ' + randType)
        return 0


def grid():
    # Negitive
    text(text=(str(count * -1)), align=('center'), pos=(count * -1, 0, 0))
    text(text=(str(count * -1)), align=('center'), pos=(0, count * -1, 0))
    text(text=(str(count * -1)), align=('center'), pos=(0, 0, count * -1))
    # Positive
    text(text=(str(count)), align=('center'), pos=(count, 0, 0))
    text(text=(str(count)), align=('center'), pos=(0, count, 0))
    text(text=(str(count)), align=('center'), pos=(0, 0, count))


def lighting():
    lamp = local_light(pos=(count, 0, 0), color=(color.green))
    return(lamp)

# Draw outside box
box(size=(256, 256, 256), color=(getrand('color'),getrand('color'),getrand('color')), opacity=(getrand('opacity')))
# TODO: Add text here with instructions

cube = frame()  # Tying shit together into a single object, sort of

# Build in a min max amount. Can make this a setable number and have it turn off and on the visability of different spheren
while true:

    # Get randoms for x,y,z for position placement
    x = getrand('pos')
    y = getrand('pos')
    z = getrand('pos')

    # Get randoms for r,g,b color assignment
    r = getrand('color')
    g = getrand('color')
    b = getrand('color')

    # Setup opacity, add some mother fluff'n rings biatch! Add tiny planets that orbit each 'star'.
    spheren.append(sphere(frame=cube, pos=(x, y, z),
    radius=(getrand('radius')),
    color=(r, g, b),
    material=materials.wood, opacity=getrand('opacity')))

    if count % 3:
        #spheren[count].visible = False
        spheren[0].visible = False
        spheren.pop(0)
        #lighting()
        time.sleep(0.1)
    count = count + 1
    cube.pos = (-1, 0, 0)
    #grid()

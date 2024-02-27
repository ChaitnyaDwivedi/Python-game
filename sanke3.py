# import keyboard as keys
import os
import random
import time
from pynput import keyboard as keys

gameover = False
height = 20
width = 20
x, y = width // 2, height // 2
fX, fY, score = random.randint(0, width-1), random.randint(0, height-1), 0
tX, tY = [0] * 100, [0] * 100
ntail = 0
dir = 0

def setup():
    global gameover, dir, x, y, fX, fY, score
    gameover = False
    dir = 0
    x, y = width // 2, height // 2
    fX, fY = random.randint(0, width-1), random.randint(0, height-1)

def draw():
    os.system('clear')
    for i in range(width):
        print("#", end="")
    print()
    for i in range(height):
        for j in range(width):
            if j == 0 or j == width - 1:
                print("#", end="")
            elif i == y and j == x:
                print("O", end="")
            elif i == fY and j == fX:
                print("F", end="")
            else:
                print_char = False
                for k in range(ntail):
                    if i == tY[k] and j == tX[k]:
                        print("o", end="")
                        print_char = True
                if not print_char:
                    print(" ", end="")
        print()
    for i in range(width):
        print("#", end="")
    print("\n")
    print("Score is:", score)



# ...

def input():
    global dir, gameover
    with keys.Listener(on_press=on_press) as listener:
        listener.join()

def on_press(key):
    global dir, gameover
    try:
        key = key.char
        if key == 'a':
            dir = 3
        elif key == 's':
            dir = 2
        elif key == 'd':
            dir = 4
        elif key == 'w':
            dir = 1
        elif key == 'x':
            gameover = True
    except AttributeError:
        pass

# ...


def logic():
    global x, y, ntail, gameover, score
    prevX, prevY = tX[0], tY[0]
    tX[0], tY[0] = x, y
    for i in range(1, ntail):
        prev2X, prev2Y = tX[i], tY[i]
        tX[i], tY[i] = prevX, prevY
        prevX, prevY = prev2X, prev2Y
    if dir == 1:
        y -= 1
    elif dir == 2:
        y += 1
    elif dir == 3:
        x -= 1
    elif dir == 4:
        x += 1
    if x >= width:
        x = 0
    elif x < 0:
        x = width - 1
    if y >= height:
        y = 0
    elif y < 0:
        y = height - 1
    for i in range(ntail):
        if x == tX[i] and y == tY[i]:
            gameover = True
    if x == fX and y == fY:
        score += 10
        fX, fY = random.randint(0, width-1), random.randint(0, height-1)
        ntail += 1

setup()
while not gameover:
    draw()
    input()
    logic()
    time.sleep(0.05)

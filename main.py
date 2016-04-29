import datetime
import math
import random
import tkinter
import threading

screenWidth = 800
screenHeight = 600
rectWidth = 50
rectHeight = 50
rectCount = 0
heroSpeed = 300  # pixels per sec
fps = 60
drawDelay = round(1000 / fps)

timerGambi = 0
timerGambiTot = 0

colors = ('Moccasin', 'Lavender', 'blue', 'green', 'red', 'purple', 'yellow', 'orange', 'firebrick2', 'tan4',
          'dark olive green', 'grey', 'pink', 'Moccasin', 'Royal Blue', 'Medium Turquoise', 'Dark Khaki', 'Gold',
          'Dark Salmon', 'Deep Pink', 'Light Steel Blue'
          )


# w.create_line(0, 0, 200, 100)
# w.create_line(0, 100, 200, 0, fill="red", dash=(4, 4))


def draw_rect(pos, color):
    # global rectCount

    # tagOld = 'rect' + str(rectCount)
    # rectCount = rectCount + 1
    # tagNew = 'rect' + str(rectCount)

    rect_tag = 'rectMain'

    # print(rectCount, color, pos)

    w.create_rectangle(pos['left'], pos['top'], pos['left'] + rectWidth, pos['top'] + rectHeight, fill=color, width=0,
                       tags=(rect_tag))
    # w.create_text((pos['left'] + rectWidth / 2), (pos['top'] + rectHeight / 2), text=rectCount, tags=(tagNew))
    # w.delete(tagOld)


def drawRandRect():
    color = random.choice(colors)
    posRand = {
        'top': random.randint(0, screenHeight - 1),
        'left': random.randint(0, screenWidth - 1)
    }
    draw_rect(posRand, color)


def drawRandRectInLoop():
    drawRandRect()
    w.after(drawDelay, drawRandRectInLoop)


def canvasClick(event):

    move_x = abs(event.x - w.coords('rectMain')[0])
    move_y = abs(event.y - w.coords('rectMain')[1])

    dist = math.sqrt(move_x * move_x + move_y * move_y)

    print('X - Clicado:', event.x, 'atual:', w.coords('rectMain')[0], 'dif: ', move_x)
    print('Y - Clicado:', event.y, 'atual:', w.coords('rectMain')[1], 'dif: ', move_y)
    print('Dist=', dist)

    startMove()
    moveTo(event.x, event.y)


def startMove():
    global timerGambi, timerGambiTot

    timerGambi = datetime.datetime.now()
    timerGambiTot = datetime.datetime.now()



def endMove():
    global timerGambiTot

    print('End: ', datetime.datetime.now() - timerGambiTot)


def moveTo(x, y):
    global timerGambi

    # print('I: ', drawDelay, datetime.datetime.now() - timerGambi)

    moveMaxX = x - w.coords('rectMain')[0]
    moveMaxY = y - w.coords('rectMain')[1]

    if x < w.coords('rectMain')[0]:
        sideX = -1  # tem que mover para a esquerda, ou seja x negativo
    else:
        sideX = 1

    if y < w.coords('rectMain')[1]:
        sideY = -1  # tem que mover para a cima, ou seja y negativo
    else:
        sideY = 1

    move = heroSpeed * drawDelay * 0.001

    if move > abs(moveMaxX):
        moveX = moveMaxX
    else:
        moveX = move * sideX

    if move > abs(moveMaxY):
        moveY = moveMaxY
    else:
        moveY = move * sideY

    # print ('moveX: ', moveX, 'moveY:', moveY, 'maxX: ', moveMaxX, 'maxY: ', moveMaxY)

    w.move('rectMain', moveX, moveY)

    # print ('x do rect:', w.coords('rectMain')[0], math.ceil(w.coords('rectMain')[0]), 'mover para: ', x)
    # print ('y do rect:', w.coords('rectMain')[1], math.ceil(w.coords('rectMain')[1]), 'mover para: ', y)

    # print('F: ', drawDelay, datetime.datetime.now() - timerGambi, moveX, moveY)
    timerGambi = datetime.datetime.now()
    if x != w.coords('rectMain')[0] or y != w.coords('rectMain')[1]:
        w.after(drawDelay, moveTo, x, y)
    else:
        endMove()


parent = tkinter.Tk()

w = tkinter.Canvas(parent, width=screenWidth, height=screenHeight)
w.bind("<Button-1>", canvasClick)

w.pack()

# drawRandRectInLoop()
drawRandRect()
tkinter.mainloop()

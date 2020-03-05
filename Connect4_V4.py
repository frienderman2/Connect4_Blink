import graphics
from graphics import *
from time import *
#Callaghan Donnelly
#2017 - 2018
#Python Mr.Blair


# drawing the board image
win = GraphWin("Connect 4", 1400, 950)
win.setBackground("blue")
board = Rectangle(Point(200, 75), Point(1200, 725))
board.setFill("Yellow")
board.draw(win)
title = Text(Point(660, 30), "Connect 4")
title.setSize(35)
title.setFace("times roman")
title.setTextColor("Red")
title.draw(win)
lblwinner = Text(Point(650, 850), "")
lblwinner.setTextColor("gold")
lblwinner.setSize(20)
lblwinner.draw(win)

# arrays for each column and counter
boardArray = [["grey", "grey", "grey", "grey", "grey", "grey"],
            ["grey", "grey", "grey", "grey", "grey", "grey"],
            ["grey", "grey", "grey", "grey", "grey", "grey"],
            ["grey", "grey", "grey", "grey", "grey", "grey"],
            ["grey", "grey", "grey", "grey", "grey", "grey"],
            ["grey", "grey", "grey", "grey", "grey", "grey"],
            ["grey", "grey", "grey", "grey", "grey", "grey"]]


# counters for making sure column stops when full
c0 = 0
c1 = 0
c2 = 0
c3 = 0
c4 = 0
c5 = 0
c6 = 0


turn = "Red"
check = False
columns = 0
rows = 0
pxlcol = 0
pxlrow = 0
direction = "none"


button_col = 200
txtX = 250
txtY = 775
increaseX = 132


# draws buttons and labels with loop
for d in range(7):
    button = Rectangle(Point(button_col, 750), Point(button_col + 95, 800))
    button_col = button_col + 144
    button.setFill("Red")
    button.draw(win)
    btntxt = Text(Point(txtX, txtY), d + 1)
    btntxt.draw(win)
    increaseX = increaseX + 3
    txtX = txtX + increaseX


# draws circles with loop
for i in range (7):
    for o in range(6):
        x = 140 * i
        y = 110 * o

        Circle(Point(x + 260, y + 120), 40).draw(win).setFill('grey')


def main():
    global turn, c0, c1, c2, c3, c4, c5, c6, columns, rows, pxlcol, pxlrow
    # loops as long as game could go then 1 more click
    while check == False:
        a = 5
        # find where the user clicked
        touch = win.getMouse()
        touch_X = touch.getX()
        touch_Y = touch.getY()

        # find column based on where the user clicks
        if touch_X >= 200 and touch_X <= 300:
            columns = 0

        elif touch_X >= 350 and touch_X <= 450:
            columns = 1

        elif touch_X >= 488 and touch_X <= 588:
            columns = 2

        elif touch_X >= 625 and touch_X <= 725:
            columns = 3

        elif touch_X >= 775 and touch_X <= 875:
            columns = 4

        elif touch_X >= 925 and touch_X <= 1025:
            columns = 5

        elif touch_X >= 1050 and touch_X <= 1145:
            columns = 6


        while boardArray[columns][a] != "grey":
            a = a - 1
        rows = a

        boardArray[columns][rows] = turn


        # Finds the pixel locatins of where to put piece based on the found row and column
        if rows == 0:
            pxlrow = 120

        elif rows == 1:
            pxlrow = 230

        elif rows == 2:
            pxlrow = 340

        elif rows == 3:
            pxlrow = 450

        elif rows == 4:
            pxlrow = 560

        elif rows == 5:
            pxlrow = 670


        if columns == 0:
            pxlcol = 260

        elif columns == 1:
            pxlcol = 400

        elif columns == 2:
            pxlcol = 540

        elif columns == 3:
            pxlcol = 680

        elif columns == 4:
            pxlcol = 820

        elif columns == 5:
            pxlcol = 960

        elif columns == 6:
            pxlcol = 1100

        # draws the desired piece
        Circle(Point(pxlcol, pxlrow), 40).draw(win).setFill(turn)
        check_diag1()
        check_diag2()
        check_horz(rows)
        check_vert()


def end_Game(rows, columns):
    global pxlcol, pxlrow
    # display winner and then exits progamme after next click
    lblwinner.setText(turn + " Wins!")
    blink(rows, columns)
    win.getMouse()
    exit()


def check_vert():
    # Check vertical columns for a winner of 4 peices
    global check, turn, direction
    check = False

    for columns in range(7):
        for rows in range(3):
            if boardArray[columns][rows] == turn and boardArray[columns][rows + 1] == turn and boardArray[columns][rows + 2] == turn and boardArray[columns][rows + 3] == turn:
                # if each column index has a color value equal to the turn then there is a winner
                check = True
                direction = "vertical"
                end_Game(rows, columns)

    if check == False:
        if turn == "Red":
            turn = "Black"
        elif turn == "Black":
            turn = "Red"


def check_horz(rows):
    # checks the horizontal rows for 4 peices of a consecutive color
    global check, turn, direction
    for columns in range(4):
        if boardArray[columns][rows] == turn and boardArray[columns + 1][rows] == turn and boardArray[columns + 2][rows] == turn and boardArray[columns + 3][rows] == turn:
            check = True
            direction = "horizontal"
            end_Game(rows, columns)


def check_diag1():
    global check, turn, direction
    for columns in (range(4)):
        for rows in (range(3)):
            # checks for a winner from NE to SW
            if boardArray[columns][rows] == turn and boardArray[columns + 1][rows + 1] == turn and boardArray[columns + 2][rows + 2] == turn and boardArray[columns + 3][rows + 3] == turn:
                check = True
                direction = "NE"
                end_Game(rows, columns)


def check_diag2():
    global check, turn, direction
    for columns in range(4):
        for rows in reversed(range(6)):
            # checks for a winner from SE to NW
            if boardArray[columns][rows] == turn and boardArray[columns + 1][rows - 1] == turn and boardArray[columns + 2][rows - 2] == turn and boardArray[columns + 3][rows - 3] == turn:
                check = True
                direction = "NW"
                end_Game(rows, columns)


def blink(rows, columns):
    newcol = ((columns + 1) * 100)
    newrow = ((rows) * 100)

    if direction == "vertical" and columns == 0:
        zer1 = Circle(Point(newcol + 160, newrow + 140), 40)
        zer2 = Circle(Point(newcol + 160, newrow + 250), 40)
        zer3 = Circle(Point(newcol + 160, newrow + 360), 40)
        zer4 = Circle(Point(newcol + 160, newrow + 470), 40)

    elif direction == "vertical" and columns != 0:
        zer1 = Circle(Point(newcol + 320, newrow + 140), 40)
        zer2 = Circle(Point(newcol + 320, newrow + 250), 40)
        zer3 = Circle(Point(newcol + 320, newrow + 360), 40)
        zer4 = Circle(Point(newcol + 320, newrow + 470), 40)

    if direction == "horizontal":
        zer1 = Circle(Point(newcol + 160, newrow + 70), 40)
        zer2 = Circle(Point(newcol + 300, newrow + 70), 40)
        zer3 = Circle(Point(newcol + 440, newrow + 70), 40)
        zer4 = Circle(Point(newcol + 580, newrow + 70), 40)

    if direction == "NE":
        zer1 = Circle(Point(newcol, newrow + 197), 40)
        zer2 = Circle(Point(newcol + 140, newrow + 307), 40)
        zer3 = Circle(Point(newcol + 280, newrow + 417), 40)
        zer4 = Circle(Point(newcol + 420, newrow + 527), 40)

    if direction == "NW":
        zer1 = Circle(Point(newcol, newrow), 40)
        zer2 = Circle(Point(newcol - 5, newrow + 307), 40)
        zer3 = Circle(Point(newcol - 25, newrow + 417), 40)
        zer4 = Circle(Point(newcol - 50, newrow + 527), 40)

    zer1.draw(win)
    zer2.draw(win)
    zer3.draw(win)
    zer4.draw(win)
    zer1.setFill('yellow')
    zer2.setFill('yellow')
    zer3.setFill('yellow')
    zer4.setFill('yellow')
    for bl in range(4):
        sleep(1)
        zer1.setFill('yellow')
        zer2.setFill('yellow')
        zer3.setFill('yellow')
        zer4.setFill('yellow')
        sleep(1)
        zer1.setFill(turn)
        zer2.setFill(turn)
        zer3.setFill(turn)
        zer4.setFill(turn)



main()

def hide():
    if direction == "horizontal":
        zer1 = Circle(Point(newcol - 1, newrow + 524), 40)
        zer2 = Circle(Point(newcol + 139, newrow + 524), 40)
        zer3 = Circle(Point(newcol + 279, newrow + 524), 40)
        zer4 = Circle(Point(newcol + 419, newrow + 524), 40)
from copy import deepcopy as DP
import os
import time
import random

def getGird(H, W):
    Tg = []
    Gird = []
    for a in range(W): Tg += [0]
    for a in range(H): Gird += [DP(Tg)]
    return Gird

def getScore(Gird, H, W):
    OO = 0
    XX = 0
    KK = 0
    for Y in range(H):
        for X in range(W):    
            if Gird[Y][X] == 2:
                OO += 1
            elif Gird[Y][X] == 1:
                XX += 1
            else:
                KK += 1
    return [OO, XX, KK]

def Draw(Gird, H, W):
    print("\x1b[0;0H")
    OO = 0
    XX = 0
    KK = 0
    print("    0   1   2   3   4   5   6   7")
    print("  " + "  " * (W * 2))
    for Y in range(H):
        Line = "{} ".format(Y)
        for X in range(W):    
            if Gird[Y][X] == 2:
                Line += "  O "  # White chess
                OO += 1
            elif Gird[Y][X] == 1:
                Line += "  X "  # Black chess
                XX += 1
            else:
                Line += "  . "
                KK += 1
        Line += "|"
        print(Line)
        print("  " + "  " * (W * 2))
    print("O: {}   ".format(OO))
    print("X: {}   ".format(XX))
    return [OO, XX, KK]

def getNew(Board, Point, Chess):
    Y = Point[0]
    X = Point[1]
    Board[Y][X] = Chess
    Points =[]
    Pp = []
    for LXY in range(1, 9): # /
        Ax = X - LXY
        Ay = Y + LXY
        if Ax <0 or Ay <0 or Ax > (W - 1) or Ay > (H - 1):
            Pp = []
            break
        elif Board[Ay][Ax] == Chess:
            break
        elif Board[Ay][Ax] != Chess and Board[Ay][Ax] != 0:
            Pp += [[Ay, Ax]]
        elif Board[Ay][Ax] == 0:
            Pp = []
            break
    if Pp != []: Points += Pp
    Pp = []
    for LXY in range(1, 9): # /
        Ax = X + LXY
        Ay = Y - LXY
        if Ax <0 or Ay <0 or Ax > (W - 1) or Ay > (H - 1):
            Pp = []
            break
        elif Board[Ay][Ax] == Chess:
            break
        elif Board[Ay][Ax] != Chess and Board[Ay][Ax] != 0:
            Pp += [[Ay, Ax]]
        elif Board[Ay][Ax] == 0:
            Pp = []
            break
    if Pp != []: Points += Pp
    Pp = []
    for LXY in range(1, 9): # \
        Ax = X - LXY
        Ay = Y - LXY
        if Ax <0 or Ay <0 or Ax > (W - 1) or Ay > (H - 1):
            Pp = []
            break
        elif Board[Ay][Ax] == Chess:
            break
        elif Board[Ay][Ax] != Chess and Board[Ay][Ax] != 0:
            Pp += [[Ay, Ax]]
        elif Board[Ay][Ax] == 0:
            Pp = []
            break
    if Pp != []: Points += Pp
    Pp = []
    for LXY in range(1, 9): # \
        Ax = X + LXY
        Ay = Y + LXY
        if Ax <0 or Ay <0 or Ax > (W - 1) or Ay > (H - 1):
            Pp = []
            break
        elif Board[Ay][Ax] == Chess:
            break
        elif Board[Ay][Ax] != Chess and Board[Ay][Ax] != 0:
            Pp += [[Ay, Ax]]
        elif Board[Ay][Ax] == 0:
            Pp = []
            break
    if Pp != []: Points += Pp
    Pp = []
    for LXY in range(1, 9): # -
        Ax = X - LXY
        Ay = Y
        if Ax <0 or Ay <0 or Ax > (W - 1) or Ay > (H - 1):
            Pp = []
            break
        elif Board[Ay][Ax] == Chess:
            break
        elif Board[Ay][Ax] != Chess and Board[Ay][Ax] != 0:
            Pp += [[Ay, Ax]]
        elif Board[Ay][Ax] == 0:
            Pp = []
            break
    if Pp != []: Points += Pp
    Pp = []
    for LXY in range(1, 9): # -
        Ax = X + LXY
        Ay = Y
        if Ax <0 or Ay <0 or Ax > (W - 1) or Ay > (H - 1):
            Pp = []
            break
        elif Board[Ay][Ax] == Chess:
            break
        elif Board[Ay][Ax] != Chess and Board[Ay][Ax] != 0:
            Pp += [[Ay, Ax]]
        elif Board[Ay][Ax] == 0:
            Pp = []
            break
    if Pp != []: Points += Pp
    Pp = []
    for LXY in range(1, 9): # |
        Ax = X
        Ay = Y - LXY
        if Ax <0 or Ay <0 or Ax > (W - 1) or Ay > (H - 1):
            Pp = []
            break
        elif Board[Ay][Ax] == Chess:
            break
        elif Board[Ay][Ax] != Chess and Board[Ay][Ax] != 0:
            Pp += [[Ay, Ax]]
        elif Board[Ay][Ax] == 0:
            Pp = []
            break
    if Pp != []: Points += Pp
    Pp = []
    for LXY in range(1, 9): # |
        Ax = X
        Ay = Y + LXY
        if Ax <0 or Ay <0 or Ax > (W - 1) or Ay > (H - 1):
            Pp = []
            break
        elif Board[Ay][Ax] == Chess:
            break
        elif Board[Ay][Ax] != Chess and Board[Ay][Ax] != 0:
            Pp += [[Ay, Ax]]
        elif Board[Ay][Ax] == 0:
            Pp = []
            break
    if Pp != []: Points += Pp
    #print(Points)
    for l in Points:
        Y, X = l[0], l[1]
        Board[Y][X] = Chess
    return DP(Board)

        
def TheAI(Board, PlayerChess, AIChess, H, W):
    ValueMap = getGird(H, W)
    BestScore = 0
    BestPoint = []
    for Y in range(H):
        for X in range(W):
            Value = 0
            if Board[Y][X] == 0:
                Pp = 0
                for LXY in range(1, 9): # /
                    Ax = X - LXY
                    Ay = Y + LXY
                    if Ax <0 or Ay <0 or Ax > (W - 1) or Ay > (H - 1):
                        Value -= Pp
                        break
                    elif Board[Ay][Ax] == AIChess:
                        break
                    elif Board[Ay][Ax] == PlayerChess:
                        Value += 1
                        Pp += 1
                    elif Board[Ay][Ax] == 0:
                        Value -= Pp
                        break
                Pp = 0
                for LXY in range(1, 9): # /
                    Ax = X + LXY
                    Ay = Y - LXY
                    if Ax <0 or Ay <0 or Ax > (W - 1) or Ay > (H - 1):
                        Value -= Pp
                        break
                    elif Board[Ay][Ax] == AIChess:
                        break
                    elif Board[Ay][Ax] == PlayerChess:
                        Value += 1
                        Pp += 1
                    elif Board[Ay][Ax] == 0:
                        Value -= Pp
                        break
                Pp = 0
                for LXY in range(1, 9): # \
                    Ax = X - LXY
                    Ay = Y - LXY
                    if Ax <0 or Ay <0 or Ax > (W - 1) or Ay > (H - 1):
                        Value -= Pp
                        break
                    elif Board[Ay][Ax] == AIChess:
                        break
                    elif Board[Ay][Ax] == PlayerChess:
                        Value += 1
                        Pp += 1
                    elif Board[Ay][Ax] == 0:
                        Value -= Pp
                        break
                Pp = 0
                for LXY in range(1, 9): # \
                    Ax = X + LXY
                    Ay = Y + LXY
                    if Ax <0 or Ay <0 or Ax > (W - 1) or Ay > (H - 1):
                        Value -= Pp
                        break
                    elif Board[Ay][Ax] == AIChess:
                        break
                    elif Board[Ay][Ax] == PlayerChess:
                        Value += 1
                        Pp += 1
                    elif Board[Ay][Ax] == 0:
                        Value -= Pp
                        break
                Pp = 0
                for LXY in range(1, 9): # -
                    Ax = X - LXY
                    Ay = Y
                    if Ax <0 or Ay <0 or Ax > (W - 1) or Ay > (H - 1):
                        Value -= Pp
                        break
                    elif Board[Ay][Ax] == AIChess:
                        break
                    elif Board[Ay][Ax] == PlayerChess:
                        Value += 1
                        Pp += 1
                    elif Board[Ay][Ax] == 0:
                        Value -= Pp
                        break
                Pp = 0
                for LXY in range(1, 9): # -
                    Ax = X + LXY
                    Ay = Y
                    if Ax <0 or Ay <0 or Ax > (W - 1) or Ay > (H - 1):
                        Value -= Pp
                        break
                    elif Board[Ay][Ax] == AIChess:
                        break
                    elif Board[Ay][Ax] == PlayerChess:
                        Value += 1
                        Pp += 1
                    elif Board[Ay][Ax] == 0:
                        Value -= Pp
                        break
                Pp = 0
                for LXY in range(1, 9): # |
                    Ax = X
                    Ay = Y - LXY
                    if Ax <0 or Ay <0 or Ax > (W - 1) or Ay > (H - 1):
                        Value -= Pp
                        break
                    elif Board[Ay][Ax] == AIChess:
                        break
                    elif Board[Ay][Ax] == PlayerChess:
                        Value += 1
                        Pp += 1
                    elif Board[Ay][Ax] == 0:
                        Value -= Pp
                        break
                Pp = 0
                for LXY in range(1, 9): # |
                    Ax = X
                    Ay = Y + LXY
                    if Ax <0 or Ay <0 or Ax > (W - 1) or Ay > (H - 1):
                        Value -= Pp
                        break
                    elif Board[Ay][Ax] == AIChess:
                        break
                    elif Board[Ay][Ax] == PlayerChess:
                        Value += 1
                        Pp += 1
                    elif Board[Ay][Ax] == 0:
                        Value -= Pp
                        break
            ValueMap[Y][X] = Value
            if Value > BestScore:
                BestScore = Value
                BestPoint = [Y, X]
            elif Value == BestScore:
                if random.random() < 0.5:
                    BestPoint = [Y, X]
    BestY = BestPoint[0]
    BestX = BestPoint[1]
    return [BestY, BestX]
    #print(ValueMap)
                    
os.system("clear")
H = 8
W = 8

Player = 2
AI = 1

Chess = ["X", "O"]

ChessBoard = [
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 2, 1, 0, 0, 0],
    [0, 0, 0, 1, 2, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
]
POINT = 0
while 1:
    os.system("clear")
    [OO, XX, KK] = Draw(ChessBoard, H, W)
    if KK == 0:
        if OO > XX:
            print("O win!    ")
        elif XX > OO:
            print("X win!    ")
        else:
            print("Both!    ")
        break
    elif XX == 0:
        print("X lose!    ")
        break
    elif OO == 0:
        print("O lose!    ")
        break
#    print("You are: {}".format(Chess[Player-1]))
#    print("AI are: {}".format(Chess[AI-1]))
#    POINT = input("Input your point:\nE.g. : 3,2  Y,X\n")
    if POINT != "Reset":
#        POINT = POINT.split(",")
        
        POINT = TheAI(ChessBoard, AI, Player, H, W)
        Y = int(POINT[0])
        X = int(POINT[1])
        POINT = [Y, X]
        if ChessBoard[Y][X] == 0:
            #print(POINT)
            time.sleep(0.5)
            ChessBoard = getNew(ChessBoard, POINT, Player)
            [OO, XX, KK] = Draw(ChessBoard, H, W)
            if KK == 0:
                if OO > XX:
                    print("O win!    ")
                elif XX > OO:
                    print("X win!    ")
                else:
                    print("Both!    ")
                break
            elif XX == 0:
                print("X lose!    ")
                break
            elif OO == 0:
                print("O lose!    ")
                break
            time.sleep(0.5)
            POINT = TheAI(ChessBoard, Player, AI, H, W)
            if ChessBoard[POINT[0]][POINT[1]] == 0:
                #print(POINT)
                ChessBoard = getNew(ChessBoard, POINT, AI)
            else:
                print("There was a Chess!")
        else:
            print("There was a Chess!")
    else:
        ChessBoard = [
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 2, 1, 0, 0, 0],
            [0, 0, 0, 1, 2, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
        ]

print("Game over!")

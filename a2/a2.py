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

def Draw(Gird, H, W, Mode = 1):
    OO = 0
    XX = 0
    KK = 0
    if Mode:
        print("\x1b[0;0H")
        print("\033[1;93;44m    0   1   2   3   4   5   6   7  ")
        print("\033[0m" + "  " * (W * 2 + 1))
        for Y in range(H):
            Line = "\033[1;93;44m{} ".format(Y)
            for X in range(W):    
                if Gird[Y][X] == 2:
                    Line += "  \033[1;32;40mO "  # White chess
                    OO += 1
                elif Gird[Y][X] == 1:
                    Line += "  \033[1;31;40mX "  # Black chess
                    XX += 1
                else:
                    if Mode: Line += "  \033[0;0;40m. "
                    KK += 1
            Line += "\033[1;93;44m|"
            print(Line)
            print("\033[0m" + "  " * (W * 2 + 1))
        print("\033[1;32;40mO: {}   ".format(OO))
        print("\033[1;31;40mX: {}   ".format(XX))
        print("\033[0m")
    else:
        for Y in range(H):
            for X in range(W):    
                if Gird[Y][X] == 2:
                    OO += 1
                elif Gird[Y][X] == 1:
                    XX += 1
                else:
                    KK += 1
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

def getValue(Board, X, Y, Value, AIChess, PlayerChess):
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
    for LXY in range(1, 9): # `
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
    for LXY in range(1, 9): # `
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
    return Value

def SearcMoveAble(Board, AIChess, PlayerChess):
    ValueMap = getGird(H, W)
    Scores = []
    MoveAble = []
    for Y in range(H): # Search AI's best location.
        for X in range(W):
            Value = 0
            if not(Board[Y][X]):
                Value = getValue(Board, X, Y, Value, AIChess, PlayerChess)
            ValueMap[Y][X] = Value
    for Y in range(H):
        for X in range(W):
            V = ValueMap[Y][X]
            if V > 0:
                Scores += [V]
                MoveAble += [[Y, X]]
    return [Scores, MoveAble]
def firstSearch(Board, MA, AIChess, PlayerChess, Times = 1):
    TempPST = 0
    NB = DP(getNew(DP(Board), MA, AIChess))
    TempMoveAble = 0
    TempP = 0
    TempMA = 0
    for Y in range(H): # Search Player's all moveable location.
        for X in range(W):
            if NB[Y][X] == 0:
                Value = getValue(NB, X, Y, 0, PlayerChess, AIChess)
                #ValueMap[Y][X] = Value
                if Value > 0:
                    #print("\x1b[%s;%sH" % (Y * 2 + 3, X * 2 + 3))
                    #print("\033[1;0;45m.")
                    #print("\033[0m")
                    SNB = DP(getNew(DP(NB), [Y, X], PlayerChess))
                    if Times <= 3:

                        a = firstSearch(SNB, [Y, X], PlayerChess, AIChess, Times + 1)
                        TempP += a[0] * 0.5
                        if a[1] == 0:
                            TempMA += 100
                        else:
                            TempMA += a[1] * 0.7
                    [OO, XX, KK] = Draw(SNB, H, W, 0)
                    #time.sleep(0.5)
                    if XX == 0:
                        TempPST += 128
                    elif OO == 0:
                        TempPST -= 64
                    else:
                        TempPST += OO + TempP * 0.5
                    TempMoveAble += 1 + TempMA * 0.5
    return [TempPST, TempMoveAble]

def TheAI(Board, PlayerChess, AIChess, H, W):

    [Scores, MoveAble] = SearcMoveAble(Board, AIChess, PlayerChess)
    
    MAs = []
    PST = []
    for MA in MoveAble:
        [TempPST, TempMoveAble] = firstSearch(Board, MA, AIChess, PlayerChess)
        if TempMoveAble == 0:
            return MA
        PST += [TempPST / TempMoveAble]
        MAs += [TempMoveAble]

    Score = []
    for k in range(len(MoveAble)):
        Score += [Scores[k]*4 - MAs[k]*8 - PST[k]]

    try:
        bestS = max(Score)
    except:
        return "PASS"
    TMP = []
    for k in range(len(Score)):
        if Score[k] == bestS:
            TMP += [MoveAble[k]]
    print(TMP)
    #exit()
    if len(TMP) >= 2:
        BestPoint = random.choice(TMP)
    else:
        BestPoint = TMP[0]
    print(BestPoint)
    #exit()
    if BestPoint != []:
        BestY = BestPoint[0]
        BestX = BestPoint[1]
        return [BestY, BestX]
    else:
        return "PASS"
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
    [0, 0, 0, 1, 2, 0, 0, 0],
    [0, 0, 0, 2, 1, 0, 0, 0],
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
    print("AI got point: {}".format(POINT))
    print("You are: {}".format(Chess[Player-1]))
    print("AI are: {}".format(Chess[AI-1]))
#    POINT = input("Input your point:\nE.g. : 3,2  Y,X\n")
    time.sleep(0.5)
    POINT = TheAI(ChessBoard, AI, Player, H, W)
    if POINT != "PASS":
#        POINT = POINT.split(",")
        
#        POINT = TheAI(ChessBoard, AI, Player, H, W)
        Y = int(POINT[0])
        X = int(POINT[1])
        POINT = [Y, X]
        if ChessBoard[Y][X] == 0:
            #print(POINT)
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
            #time.sleep(0.5)
        else:
            print("There was a Chess!")
    elif POINT == "RESET":
        ChessBoard = [
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 1, 2, 0, 0, 0],
            [0, 0, 0, 2, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
        ]
    else:
        pass
    time.sleep(0.5)
    POINT = TheAI(ChessBoard, Player, AI, H, W)
    #print(ChessBoard)
    #exit()
    if POINT != "PASS":
        if ChessBoard[POINT[0]][POINT[1]] == 0:
            #print(POINT)
            ChessBoard = getNew(ChessBoard, POINT, AI)
        else:
            print("There was a Chess!")
    else:
        pass

print("Game over!")

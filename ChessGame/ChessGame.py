import os


w, h = 8,8;
winner = False


ChessField = [['T', 'H', 'B', 'Q', 'K', 'B', 'H', 'T'], 
              ['F', 'F', 'F', 'F', 'F', 'F', 'F', 'F'], 
              ['_', '_', '_', '_', '_', '_', '_', '_'], 
              ['_', '_', '_', '_', '_', '_', '_', '_'], 
              ['_', '_', '_', '_', '_', '_', '_', '_'], 
              ['_', '_', '_', '_', '_', '_', '_', '_'], 
              ['F', 'F', 'F', 'F', 'F', 'F', 'F', 'F'], 
              ['T', 'H', 'B', 'K', 'Q', 'B', 'H', 'T']]

def Chesfield():
    print("a b c d e f g h ")
    counter = 0
    for line in ChessField:
        counter = counter + 1
        for letter in line:
            print(letter, end=' ')
        print(counter, end=' ')
        print("")

def convlettonumb(letter):
    if letter == 'a':
        return 0
    if letter == 'b':
        return 1
    if letter == 'c':
        return 2
    if letter == 'd':
        return 3
    if letter == 'e':
        return 4
    if letter == 'f':
        return 5
    if letter == 'g':
        return 6
    if letter == 'h':
        return 7

def checkSelection(figure):
    if len(figure) == 2:
        print(figure[0])
        sy = int(convlettonumb(figure[0]))
        print(figure[1])
        sx = int(figure[1])-1
    if sx < 8 and sy >= 0 :
        print(ChessField[sx][sy])
        print(" " + str(sx)  + "-" + str(sy) )
    if ChessField[sx][sy] == '_':
        print("Keine Figur gewaehlt")
    return ChessField[sx][sy]

def checkTarget(target):
    if len(target) == 2:
        print(target[0])
        sy = int(convlettonumb(target[0]))
        print(target[1])
        sx = int(target[1])-1
    if sx < 8 and sy >= 0 :
        print(ChessField[sx][sy])
        print(" " + str(sx)  + "-" + str(sy) )
    return ChessField[sx][sy]

def farmer(p,t):
    moveint = abs(int(p[1]) - int(t[1]))
    if moveint > 0 and moveint < 3:
        ChessField[int(p[1])-1][int(convlettonumb(p[0]))] = '_'
        ChessField[int(t[1])-1][int(convlettonumb(t[0]))] = 'F'

def tower(p,t):
    if p[1] == t[1]:
        print(abc(int(p[1]) - int(t[1])))

    if p[0] == t[0]:
        print(abs(int(convlettonumb(p[0])) - int(convlettonumb(t[0]))))

    ChessField[int(p[1])-1][int(convlettonumb(p[0]))] = '_'
    ChessField[int(t[1])-1][int(convlettonumb(t[0]))] = 'T'

def horse(p,t):
    ChessField[int(p[0])][int(p[1])] = '_'
    ChessField[int(t[0])][int(t[1])] = 'H'

def bishop(p,t):
    ChessField[int(p[0])][int(p[1])] = '_'
    ChessField[int(t[0])][int(t[1])] = 'B'

def queen(p,t):
    ChessField[int(p[0])][int(p[1])] = '_'
    ChessField[int(t[0])][int(t[1])] = 'Q'

def king(p,t):
    ChessField[int(p[0])][int(p[1])] = '_'
    ChessField[int(t[0])][int(t[1])] = 'K'

def checkFigure(token, Sfigure, target):
    if token == 'F':
        farmer(Sfigure,target)
    if token == 'T':
        tower(Sfigure,target)
    if token == 'H':
        horse(Sfigure,target)
    if token == 'B':
        bishop(Sfigure,target)
    if token == 'Q':
        queen(Sfigure,target)
    if token == 'K':
        king(Sfigure,target)

while winner == False:
    Chesfield() 
    playerf = input('Waehle Figur Koordinate: ') 
    Sfigure = checkSelection(playerf) 
    target = input('Waehle  Zielkoordinate: ') 
    Starget = checkTarget(target) 
    checkFigure(Sfigure, playerf, target) 
    #os.system('cls') 
    Chesfield() 
    winner = True
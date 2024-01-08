import pygame
import time
width =700
height =700
blue=(0,0,40)
red=(200,0,0)
yellow=(200,200,0)
x=0
y=0
# drop=0
circleRadius=45

pieceSwitch=2

runOnce=0

pieceEnd=0

clock = pygame.time.Clock()
board = [
    [0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0],
    [3,3,3,3,3,3,3]#This one is the base that "holds" the pieces above
    ]
boardCoords = [
    [(0,0)  ,(100,0)  ,(200,0)  ,(300,0)  ,(400,0)  ,(500,0)  ,(600,0)  ],#Top(starting), before the board itself
    [(0,100),(100,100),(200,100),(300,100),(400,100),(500,100),(600,100)],
    [(0,200),(100,200),(200,200),(300,200),(400,200),(500,200),(600,200)],
    [(0,300),(100,300),(200,300),(300,300),(400,300),(500,300),(600,300)],
    [(0,400),(100,400),(200,400),(300,400),(400,400),(500,400),(600,400)],
    [(0,500),(100,500),(200,500),(300,500),(400,500),(500,500),(600,500)],
    [(0,600),(100,600),(200,600),(300,600),(400,600),(500,600),(600,600)],
]
def layout():
    for row in board:
        print(row)
    print("------------------")
 
b=0
switch=1
bottom=height-100

window = pygame.display.set_mode((width,height))
pygame.display.set_caption('Connect Four Attempt')

circle2 = pygame.image.load('assets/Circle.png')
BoardLayout = pygame.image.load('assets/BoardLayout.png')
circle = pygame.transform.scale(circle2, (100,100))

def circleColour(switch):
    if switch==1:
        circle2 = pygame.image.load('assets/RedCircle.png')
    else:
        circle2 = pygame.image.load('assets/YellowCircle.png')
    return pygame.transform.scale(circle2, (100,100))
    
def circleAppearance(x,y):
    window.fill(blue)
    displayUpdate()
    window.blit(circle,(x,y))
    window.blit(BoardLayout,(0,100))
    pygame.display.update()
    
def drop(x,y,pieceSwitch):
    num=int(y/100)-1
    num2=int(x/100)
    if y%100==0:
        if board[num][num2]!=0 and board[6][num2]!=0:
            board[num-1][num2]=pieceSwitch
            return 1
    return 0

def redWin():
    redBanner = pygame.image.load('assets/RedWins.jpg')
    window.blit(redBanner,(0,0))
def yellowWin():
    yellowBanner = pygame.image.load('assets/YellowWins.jpg')
    window.blit(yellowBanner,(0,0))
def checkWin():
    for x in range(6):
        for y in range(3):
            if board[x][y]==1 and board[x][y+1]==1 and board[x][y+2]==1 and board[x][y+3]==1:
                # print("WIN for RED - HORIZONTAL")
                redWin()
    for x in range(6):
        for y in range(3):
            if board[x][y]==2 and board[x][y+1]==2 and board[x][y+2]==2 and board[x][y+3]==2:
                # print("WIN for YELLOW - HORIZONTAL")
                yellowWin()
    for x in range(6):
        for y in range(3):
            if board[x][y]==1 and board[x+1][y]==1 and board[x+2][y]==1 and board[x+3][y]==1:
                # print("WIN for RED - VERTICAL")
                redWin()
    for x in range(6):
        for y in range(3):
            if board[x][y]==2 and board[x+1][y]==2 and board[x+2][y]==2 and board[x+3][y]==2:
                # print("WIN for YELLOW - VERTICAL")
                yellowWin()
    for x in range(3):
        for y in range(4):
            if board[x][y]==1 and board[x+1][y+1]==1 and board[x+2][y+2]==1 and board[x+3][y+3]==1:
                # print("WIN for RED - \DIAGONAL\ ")
                redWin()
    for x in range(3):
        for y in range(4):
            if board[x][y]==2 and board[x+1][y+1]==2 and board[x+2][y+2]==2 and board[x+3][y+3]==2:
                # print("WIN for YELLOW - \DIAGONAL\ ")
                yellowWin()
    for x in range(5,3,-1):
        for y in range(4):
            if board[x][y]==1 and board[x-1][y+1]==1 and board[x-2][y+2]==1 and board[x-3][y+3]==1:
                # print("WIN for RED - /DIAGONAL/ ")
                redWin()
    for x in range(5,3,-1):
        for y in range(4):
            if board[x][y]==2 and board[x-1][y+1]==2 and board[x-2][y+2]==2 and board[x-3][y+3]==2:
                # print("WIN for RED - /DIAGONAL/ ")
                yellowWin()

def newCircle():
    board[1][1]=1

def displayUpdate():
    window.fill(blue)
    window.blit(BoardLayout,(0,100))

    for row in range(6): #checks every row
        for column in range(7): #checks every column
            b = board[row][column]
            if b==1:
                pygame.draw.circle(window, red, (column*100+50,row*100+150),circleRadius)
            if b==2:
                pygame.draw.circle(window, yellow, (column*100+50,row*100+150),circleRadius)
homepage = pygame.image.load('assets/Homepage.png')
window.blit(homepage,(0,0))
start=0
pygame.display.update()
while start!=1:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
                if event.key != pygame.K_l:
                    start=1

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        #This type of event is WHEN the key is pressed down, then it works
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and board[0][int(x/100)]==0:
                if pieceSwitch==2:
                    pieceSwitch=1
                else:
                    pieceSwitch=2
                while pieceEnd==0:
                    circleAppearance(x,y)
                    y+=10
                    pieceEnd=drop(x,y,pieceSwitch)
            time.sleep(0.001)
            
        #This type of event works WHILE the key is being pressed down
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LCTRL]:
            pygame.quit()
            quit()
        if keys[pygame.K_1]:
            x=0
        if keys[pygame.K_2]:
            x=100
        if keys[pygame.K_3]:
            x=200
        if keys[pygame.K_4]:
            x=300
        if keys[pygame.K_5]:
            x=400
        if keys[pygame.K_6]:
            x=500
        if keys[pygame.K_7]:
            x=600
        if keys[pygame.K_c]:
            newCircle()
        if keys[pygame.K_l]:
            layout()

    if y==bottom or pieceEnd!=0:
        y=0
        if switch==1:
            switch=0
        else:
            switch=1
        
    pieceEnd=0
    circle = circleColour(switch)

    displayUpdate()
    circleAppearance(x,y)
    checkWin()
    pygame.display.update()
    clock.tick(10)


pygame.quit()
quit()
## 3.2 Our First Animations

### Bigger Smaller


```python
# from cmu_graphics import *

def onAppStart(app):
    app.size = 100

def pointInRect(app,x,y):
    xLeft = app.width/2 - app.size/2
    xRight = app.width/2 + app.size/2
    yTop = app.height/2 - app.size/2
    yBottom = app.height/2 + app.size/2
    return xLeft<=x<=xRight and yTop<=y<=yBottom

def onMousePress(app, mouseX, mouseY):
    if pointInRect(app,mouseX,mouseY):
        if app.size<250:
            app.size += 50
    else:
        if app.size>50:
            app.size -= 50

def redrawAll(app):
    if app.size == 50 or app.size == 250:
        fill = 'red'
    else:
        fill='lightGreen'
    drawRect(app.width/2-app.size/2,\
            app.height/2-app.size/2,\
            app.size, app.size,fill=fill)

def main():
    runApp()

# main()
```

### Bigger Smaller Again


```python
# from cmu_graphics import *

def onAppStart(app):
    app.size = 100
    app.clicksInside = 0
    app.clicksOutside = 0
    app.squareIsGrowing = True

def pointInRect(app,x,y):
    xLeft = app.width/2 - app.size/2
    xRight = app.width/2 + app.size/2
    yTop = app.height/2 - app.size/2
    yBottom = app.height/2 + app.size/2
    return xLeft<=x<=xRight and yTop<=y<=yBottom

def onMousePress(app, mouseX, mouseY):
    if pointInRect(app,mouseX,mouseY):
        app.clicksInside += 1
        if app.squareIsGrowing:
            app.size += 50
            if app.size == 250:
                app.squareIsGrowing = False
        else:
            app.size -= 50
            if app.size == 50:
                app.squareIsGrowing = True
    else:
        app.clicksOutside += 1

def redrawAll(app):
    if app.size==50 or app.size==250:
        fill='red'
    else:
        fill='lightGreen'
        
    drawLabel(f'Clicks inside the square: {app.clicksInside}',200,30, \
        font='arial', fill='black')
    drawLabel(f'Clicks outside the square: {app.clicksOutside}',200,60, \
        font='arial', fill='black')
    drawRect(app.width/2-app.size/2, app.height/2-app.size/2, \
            app.size, app.size, fill=fill)

def main():
    runApp()

# main()
```

## 3.3 Basic Shapes

### Shapes with Loops


```python
# from cmu_graphics import *

def redrawAll(app):
    drawRect(50,10,300,40,fill='lightGreen')
    drawLabel('Shapes with Loops!', 200, 30, size=30, bold=True)
    for i in range(16):
        centerX = 50 + 20 * i
        drawCircle(centerX,100,10,fill='orange', border='black')
        drawOval(centerX,150,10,30,fill=None, border='blue', borderWidth=3,
            rotateAngle=-45+6*i)
        if i <= 7:
            centerY = 200 + 20 * i
        else:
            centerY = 500 - 20 * i
        drawCircle(centerX,centerY,10,fill='black', border='orange')
        
        x1 = centerX
        y1 = 375
        x2 = centerX
        y2 = centerY
        drawLine(x1,y1,x2,y2,fill='black')
    
    for i in range(10,0,-1):
        if i % 2 == 0:
            fill='blue'
        else:
            fill='pink'
        drawRect(200,240,10 * i, 10 * i, fill=fill,
            rotateAngle=45,align='center')
        

def main():
    runApp()

# main()
```

### 21 Lines


```python
# from cmu_graphics import *

def getButtonColor(i):
    if i == 0: return 'red'
    elif i == 1: return 'blue'
    elif i == 2: return 'green'
    elif i == 3: return 'black'
    
def getLineWidth(i):
    if i == 0: return 1
    elif i == 1: return 2
    elif i == 2: return 3
    elif i == 3: return 4

def onAppStart(app):
    app.fill='red'
    app.lineWidth = 1

def redrawAll(app):
    drawLabel('21 Lines', 200, 30, size=20, bold=True)
    drawLabel('Color buttons change the line colors', 200, 50)
    drawLabel('Width buttons change the line widths', 200, 70)
    
    # 21 lines
    for i in range(21):
        x1=0+20*i
        x2=400-20*i
        drawLine(x1,100,x2,300,fill=app.fill,lineWidth=app.lineWidth)
    
    # colors and widths
    drawLabel('Colors:', 30,335,bold=True)
    drawLabel('Widths:', 29,375,bold=True)
    for i in range(4):
        x=60+60*i
        color=getButtonColor(i)
        drawRect(x,320,30,30,fill=color)
        drawRect(x,360,30,30,fill='lightGray',border='black',borderWidth=2)
        x1=65+60*i
        x2=85+60*i
        drawLine(x1,375,x2,375,fill=app.fill,lineWidth=getLineWidth(i))

def onMousePress(app, mouseX, mouseY):
    if 60<=mouseX<=90 and 320<=mouseY<=350:
        app.fill='red'
    elif 120<=mouseX<=150 and 320<=mouseY<=350:
        app.fill='blue'
    elif 180<=mouseX<=210 and 320<=mouseY<=350:
        app.fill='green'
    elif 240<=mouseX<=270 and 320<=mouseY<=350:
        app.fill='black'
    
    if 60<=mouseX<=90 and 360<=mouseY<=390:
        app.lineWidth=1
    elif 120<=mouseX<=150 and 360<=mouseY<=390:
        app.lineWidth=2
    elif 180<=mouseX<=210 and 360<=mouseY<=390:
        app.lineWidth=3
    elif 240<=mouseX<=270 and 360<=mouseY<=390:
        app.lineWidth=4

def main():
    runApp()

# main()
```

## 3.4 Mouse Events

### Moving Highlighting Dot


```python
# from cmu_graphics import *

def onAppStart(app):
    app.isDragging = False
    app.isHighlighting = False
    app.centerX = 200
    app.centerY = 200

def redrawAll(app):
    drawLabel('Moving Highlighting Dot', 200, 30, size=20, bold=True)
    drawLabel('Move mouse in and out of dot to change highlighting',
              200, 50, size=12)
    drawLabel('Click and drag to move the dot',
              200, 70, size=12)
              
    if app.isDragging:          fill='orange'
    elif app.isHighlighting:    fill='yellow'
    else:                       fill='gray'
    
    drawCircle(app.centerX, app.centerY, 40, fill=fill, border='black')

def onMousePress(app, mouseX, mouseY):
    (app.centerX, app.centerY) = (mouseX, mouseY)
    app.isDragging = True

def onMouseDrag(app, mouseX, mouseY):
    (app.centerX, app.centerY) = (mouseX, mouseY)

def onMouseRelease(app, mouseX, mouseY):
    app.isDragging = False
    app.isHighlighting = True

def onMouseMove(app, mouseX, mouseY):
    if distance(mouseX, mouseY, app.centerX, app.centerY) <= 40:
        app.isHighlighting = True
    else:
        app.isHighlighting = False

def distance(x0, y0, x1, y1):
    return ((x1 - x0)**2 + (y1 - y0)**2)**0.5

def main():
    runApp()

# main()
```

### Dots while Pressed


```python
# from cmu_graphics import *

def onAppStart(app):
    app.isDragging = False
    app.isPressing = False
    app.counter = 0
    app.centerX = 200
    app.centerY = 200

def redrawAll(app):
    drawLabel('Dots while Pressed', 200, 30, size=20, bold=True)
    drawLabel('Press and drag to see numbered dots', 200, 50, size=12)
    if app.isPressing:
        drawCircle(app.centerX, app.centerY, 40, fill='yellow',border='black')
        drawLabel(f'{app.counter}', app.centerX, app.centerY-10, 
                  size=20, bold=True)

def onMousePress(app, mouseX, mouseY):
    app.isPressing = True
    app.counter += 1
    (app.centerX, app.centerY) = (mouseX, mouseY)

def onMouseDrag(app, mouseX, mouseY):
    app.isDragging = True
    (app.centerX, app.centerY) = (mouseX, mouseY)
    
def onMouseRelease(app, mouseX, mouseY):
    app.isDragging = False
    app.isPressing = False

def main():
    runApp()

# main()
```

## 3.5 Key Events

### Color-Toggling Freezing Dot


```python
# from cmu_graphics import *

def onAppStart(app):
    app.cx = 200
    app.cy = 200
    app.isFrozen = False
    app.color = 'green'

def redrawAll(app):
    drawLabel('Color-Toggling Freezing Dot', 200, 30, size=20, bold=True)
    drawLabel('Move the dot with the mouse', 200, 50, size=12)
    drawLabel('Press c to toggle the dot color', 200, 70, size=12)
    drawLabel('Press and hold f to freeze the dot', 200, 90, size=12)
    
    color = 'cyan' if app.isFrozen else app.color
    drawCircle(app.cx, app.cy, 40, fill=color, border='black')

def onMouseMove(app, mouseX, mouseY):
    if not app.isFrozen:
        (app.cx, app.cy) = (mouseX, mouseY)

def onKeyPress(app, key):
    if key == 'f': 
        app.isFrozen = True
    elif key == 'c' and not app.isFrozen:
        app.color='gold' if app.color=='green' else 'green'
        

def onKeyRelease(app, key):
    if key == 'f': 
        app.isFrozen = False

def main():
    runApp()

# main()
```

## 3.6 Timer Events

### Different Speeds


```python
# from cmu_graphics import *

def onAppStart(app):
    app.topR=10
    app.topC=0
    app.topPaused=True
    app.bottomR=10
    app.bottomC=0
    app.bottomPaused=True
    app.stepsPerSecond=30
    app.stepCounter=0

def redrawAll(app):
    if app.topPaused: topFill = 'gray'
    else: topFill = 'cyan'
    if app.bottomPaused: bottomFill = 'gray'
    else: bottomFill = 'pink'
    
    drawLabel('Different Speeds', 200, 30, size=16)
    drawLabel('Press t to pause/unpause top dot', 200, 50)
    drawLabel('Press b to pause/unpause bottom dot', 200, 70)
    drawCircle(200, 175, app.topR, fill=topFill,border='black')
    drawLabel(f'{app.topC}', 200, 175, size=16)
    drawCircle(200, 325, app.bottomR, fill=bottomFill,border='black')
    drawLabel(f'{app.bottomC}', 200, 325, size=16)

def onStep(app):
    app.stepCounter+=1
    if not app.topPaused:
        app.topC += 1
        if app.topR == 75: 
            app.topR = 10
        else:
            app.topR += 5
            
    if not app.bottomPaused and app.stepCounter % 5 ==0:
        app.bottomC += 1
        if app.bottomR == 75: 
            app.bottomR = 10
        else:
            app.bottomR += 5

def onKeyPress(app, key):
    if key == 't': 
        app.topPaused = not app.topPaused
    if key == 'b': 
        app.bottomPaused = not app.bottomPaused

def runTest():
    app = runApp()

def main():
    # runApp()
    runTest()

# main()
```

### Scrolling Carpe Diems


```python
# from cmu_graphics import *

def onAppStart(app):
    app.message = 'Carpe Diem '
    app.shift = 0
    app.isPaused = True

def redrawAll(app):
    drawLabel('Scrolling Carpe Diems', 200, 30, size=16)
    drawLabel('Press p to pause/unpause', 200, 50, size=12)
    drawLabel('Press s to step while paused', 200, 70, size=12)
    for i in range(19):
        char = app.message[(i+app.shift)%11]
        drawLabel(f'{char}',20+20*i,200,size=20,bold=True)

def onStep(app):
    if not app.isPaused:
        app.shift += 1

def takeStep(app):
    app.shift += 1

def onKeyPress(app, key):
    if key == 'p':
        app.isPaused = not app.isPaused
    elif key == 's':
        takeStep(app)

def main():
    runApp()

# main()
```

### Falling Carpe Diems


```python
# from cmu_graphics import *

def onAppStart(app):
    app.message = 'Carpe Diem'
    app.isPaused = True
    app.index = 0
    app.cy = 100
    # app.stepsPerSecond = 20
    app.shift = [0,0,0,0,0,0,0,0,0,0]
    
def redrawAll(app):
    drawLabel('Falling Carpe Diems', 200, 30, size=16)
    drawLabel('Press p to pause/unpause', 200, 50, size=12)
    drawLabel('Press s to step while paused', 200, 70, size=12)
    for i in range(len(app.message)):
        char = app.message[i%10]
        drawLabel(f'{char}',20+40*i,app.cy+app.shift[i],size=16)

def onStep(app):
    if not app.isPaused:
        takeStep(app)

def takeStep(app):
    if app.cy + app.shift[app.index] < 300:
        app.shift[app.index] += 10
    if app.cy + app.shift[app.index] == 300:
        app.index += 1
        if app.index == len(app.message):
            app.index = 0
            app.shift = [-10,0,0,0,0,0,0,0,0,0]

def onKeyPress(app, key):
    if key == 'p':
        app.isPaused = not app.isPaused
    if key == 's':
        takeStep(app)

def main():
    runApp()

# main()
```

## Exercises

### Number Guessing Game


```python
# from cmu_graphics import *
import random, math

def onAppStart(app):
    newGame(app)

def newGame(app):
    app.answer = random.randrange(1, 101)
    app.lo = 1
    app.hi = 100
    app.guessCount = 0
    app.currentGuess = ''
    app.message = 'Enter your next guess'
    app.showHint = False
    app.showAnswer = False
    app.gameOver = False
    app.success = False
    app.isLower = False
    app.isHigher = False
    app.tooHi = False
    app.tooLo = False

def redrawAll(app):
    # Draw the instructions:
    drawLabel('Number Guessing Game', 200, 20, size=20, bold=True)
    drawLabel(f'Guess a number between 1 and 100 (inclusive)',
              200, 50)
    drawLabel('To enter a guess, type the number followed by the enter key',
              200, 70)
    drawLabel('Press n to play a new game', 200, 90)
    drawLabel('Press h to toggle displaying the hint', 200, 110)
    drawLabel('Press a to see the answer', 200, 130)
    drawLine(50, 150, 350, 150)
    
    # Draw the current guess and the message:
    drawLabel(f'Current Guess: {app.currentGuess}', 200, 170,
              size=20, bold=True)
    if app.success:
        drawLabel(f'You got it in {app.guessCount} guesses!', 200, 200)
    elif app.isHigher:
        drawLabel(f'We know the number is at most {app.hi}', 200, 200)
    elif app.isLower:
        drawLabel(f'We know the number is at least {app.lo}', 200, 200)
    elif app.tooHi:
        drawLabel('Too high!', 200, 200)
    elif app.tooLo:
        drawLabel('Too low!', 200, 200)
    else:
        drawLabel('Enter your next guess', 200, 200)
    drawLine(50, 220, 350, 220)
    
    # Draw the hint and answer (if they are visible):
    hintGuess = (int(app.lo)+int(app.hi))//2
    label=f'hint: The range is now {app.lo} to {app.hi}, so try {hintGuess}.'
    if app.showHint and app.gameOver == False:
        drawLabel(label, 200, 240)
        
    if app.showAnswer and app.gameOver == False:
        drawLabel(f'answer: {app.answer}', 200, 270)

def onKeyPress(app, key):
    if key.isdigit():
        app.currentGuess += key
    elif key == 'backspace':
        app.currentGuess = app.currentGuess[:-1]
    elif key == 'h':
        app.showHint = True if app.showHint == False else False
    elif key == 'a':
        app.showAnswer = True if app.showAnswer == False else False
    elif key == 'n':
        newGame(app)
    elif key == 'enter' and app.currentGuess != None:
        handleGuess(app)
        app.guessCount += 1
        app.currentGuess = ''
        # app.isLower = False
        # app.isHigher = False

def handleGuess(app):
    app.currentGuess = int(app.currentGuess)
    if app.lo <= app.currentGuess <= app.hi:
        if app.currentGuess == app.answer:
            app.success = True
            app.gameOver = True
        elif app.currentGuess <= app.answer:
            app.lo = app.currentGuess + 1
            app.tooLo = True
        elif app.currentGuess >= app.answer:
            app.hi = app.currentGuess - 1
            app.tooHi = True
    
    elif app.currentGuess > app.hi:
        app.isHigher = True
    elif app.currentGuess < app.lo:
        app.isLower = True
    

def main():
    runApp()

# main()
```

### Play 21

Here are the rules of 21:

1. When the game starts, you (the player) are dealt two cards to your hand, and the dealer (the computer) is dealt one card to its hand.
2. Your score is the sum of the ranks of the cards in your hand, where aces are worth 1 or 11, 2-10 are worth their respective values, and jacks, queens, and kings are all worth 10. Card suits are ignored.
3. Your goal is to get as close to 21 without going over ("busting").
4. On your turn, you can keep taking cards ("hitting") until you bust (and lose), get 21, or stop taking cards ("stand").
5. If you have any aces, then they are automatically assigned either 1 or 11 so that you get the highest score without busting.
6. Once you decide to stand, it becomes the dealer's turn.
7. The dealer must keep taking cards (hitting) until their score is 17 or greater, at which point they must stop (stand).
8. If the dealer busts (goes over 21), you win.
9. If the neither the dealer nor the player busts, then the higher score wins, except that the dealer wins ties.
10. Finally, if you are dealt 21 on your first two cards, you immediately win.


```python
# from cmu_graphics import *
import random

def onAppStart(app, initialDeck=None):
    newGame(app, initialDeck)

def newGame(app, initialDeck):
    app.message = 'Your turn (press h or s)'
    app.gameOver = False
    app.playerSuccess = False
    app.isHit = False
    app.isStand = False
    app.isHitDealer = False
    app.hitCounter = 0
    app.hitCounterDealer = 0
    app.playerHand = ''
    app.dealerHand = ''
    
    # Use the initialDeck if it is not None, otherwise make
    # a new random deck, and store the deck in app.deck:
    if initialDeck == None:
        app.deck = makeRandomDeck()
    else:
        app.deck = initialDeck
    
    # Next, deal 2 cards to the player and 1 to the dealer:
    app.playerHand += dealCard(app)
    app.playerHand += dealCard(app)
    app.dealerHand += dealCard(app)
    
    app.playerScore = score(app.playerHand) 
    app.dealerScore = score(app.dealerHand)
    
    # Next, check if the user has 21:
    if app.playerScore > 21:
        app.playerSuccess = False
        app.gameOver = True
    elif app.playerScore == 21:
        app.playerSuccess = True
        app.gameOver = True

def redrawAll(app):
    # 1. Draw pink or lightGreen background rectangle if game is over:
    fill = 'lightGreen' if app.playerSuccess else 'pink'
    if app.gameOver:
        drawRect(0,0,400,400,fill=fill, opacity=100)
        
    # 2. Draw the relevant instructions:
    drawLabel('Play 21', 200, 20, size=20, bold=True)
    
    # 3. The next two labels will change depending on the situation:
    if not app.gameOver:
        drawLabel('Press h to hit (take another card)', 200, 50)
        drawLabel('Press s to stand (stop taking cards)', 200, 70)
    else:
        drawLabel('Press n for a new game', 200, 50)
    drawLine(50, 90, 350, 90)
    
    # 4. Draw the player's and dealer's hands:
    drawPlayerHand(app)
    drawDealerHand(app)
    
    drawLine(50, 310, 350, 310)
    
    # 5. Draw the current message:
    
    drawLabel(app.message, 200, 330, size=16, bold=True)

def drawPlayerHand(app):
    drawLabel(f'Your hand: ({app.playerScore})',200,110,size=16,bold=True)
    for i in range(len(app.playerHand)//2):
        if str(app.playerHand[1+2*i]) in 'hd':
            fill='red'
        else:
            fill='black'
            
        drawRect(37+30*i,130,26,60,fill=None,border='black')
        drawLabel(str(app.playerHand[0+2*i]), 50+30*i, 145, size=20, fill=fill,
            bold=True)
        symbol = getSuitSymbol(app.playerHand[1+2*i])
        drawLabel(symbol, 50+30*i, 170, size=20, fill=fill,font='symbols')
    
def drawDealerHand(app):
    drawLabel(f'''Dealer's hand: ({app.dealerScore})''',
        200,210,size=16,bold=True)
    for i in range(len(app.dealerHand)//2):
        if str(app.dealerHand[1+2*i]) in 'hd':
            fill='red'
        else:
            fill='black'
            
        drawRect(37+30*i,230,26,60,fill=None,border='black')
        drawLabel(str(app.dealerHand[0+2*i]), 50+30*i, 245, size=20, fill=fill,
            bold=True)
        symbol = getSuitSymbol(app.dealerHand[1+2*i])
        drawLabel(symbol, 50+30*i, 270, size=20, fill=fill, font='symbols')

def getSuitSymbol(suit):
    if suit == 'c': return chr(0x2663)   # unicode for a club
    elif suit == 'd': return chr(0x2666) # unicode for a diamond
    elif suit == 'h': return chr(0x2665) # unicode for a heart
    if suit == 's': return chr(0x2660)   # unicode for a spade

def onKeyPress(app, key):
    if not app.gameOver:
        if key == 'h': hit(app)
        elif key == 's': stand(app)
        elif key == 'd': dealerPlay(app)
        elif key == 'n': newGame(app, None)

def dealCard(app):
    card = app.deck[:2]
    app.deck = app.deck[2:]
    return card
    
def score(hand):
    score = 0
    hasAce = False
    for i in range(0,len(hand),2):
        card = hand[i:i+2]
        rank = card[0]
        if rank == 'A':
            score += 1
            hasAce = True
        elif rank in 'TJQK':
            score += 10
        else:
            score += int(rank)
        
    if hasAce and score <= 10:
        score += 10
    return score

def hit(app):
    if not app.isStand:
        app.playerHand += dealCard(app)
        app.playerScore = score(app.playerHand)
        if app.playerScore > 21:
            checkScore(app)
            app.gameOver = True

def stand(app):
    app.isStand = True
    app.message='''Dealer's Turn: (press d)'''

def dealerPlay(app):
    if app.isStand:
        app.dealerHand += dealCard(app)
        app.dealerScore = score(app.dealerHand)
        if app.dealerScore >= 17:
            checkScore(app)
            app.gameOver = True

def checkScore(app):
    if app.playerScore > 21:
        app.message='You busted! You lose!'
    elif app.dealerScore > 21:
        app.playerSuccess = True
        app.message='Dealer busted! You win!'
    elif app.dealerScore > app.playerScore:
        app.message='Dealer beat you! You lose!'
    elif app.dealerScore < app.playerScore:
        app.playerSuccess = True
        app.message='You beat the dealer! You win!'
    elif app.dealerScore == app.playerScore:
        app.message='Dealer tied you! You lose!'
    
# This function is provided for you, and creates a new random deck.
# You should call it each time a new game starts.
def makeRandomDeck():
    deck = ''
    for i in random.sample(range(52), 52):
        rank = 'A23456789TJQK'[i%13]
        suit = 'shdc'[i//13]
        card = rank + suit
        deck += card
    return deck

def main():
    runApp()

# main()
```

# 3.2 Our First Animations

Model-View-Controller

Model
- The model contains all the data we need for our app. Basically, these are the values we store in the app object.

View
- The view (and only the view) draws the app using the values in the model. In general, the view includes redrawAll and any helper functions it may call.

Controller
- Each controller responds to keyboard, mouse, timer and other events (such as the app starting) and updates the model. In the example above, onAppStart and onMousePress are our controllers. These functions are also called event handlers. In general, controllers include all the event handlers (the "onEvent" functions) and any helper functions they may call.

MVC Rules

1. Never directly call the view or the controllers.
- There are times you may want to call a controller, such as calling onAppStart to restart an app. Instead of doing this, use a helper function that you call in onAppStart, and then you can call that same helper function from elsewhere in your code.

2. Controllers only update the model, not the view.
- onMousePress cannot call redrawAll and cannot directly call any drawing functions. Each time onMousePress finishes running, redrawAll is automatically called for us.

3. The view can never update the model.
- redrawAll cannot change app.rectLeft or app.rectTop.

# 3.3 Basic Shapes

## Rectangles


```python
def redrawAll(app):
    drawRect(left, top, width, height, fill='black',
             border=None, borderWidth=2, opacity=100, rotateAngle=0)

    drawRect(x, y, 50, 50, fill='green', rotateAngle=45, align='center')
```

## Ovals and Circles


```python
def redrawAll(app):
    drawOval(centerX, centerY, width, height, fill='black',
         border=None, borderWidth=2, opacity=100, rotateAngle=0)
    drawCircle(centerX, centerY, radius, fill='black',
         border=None, borderWidth=2, opacity=100)
```

## Lines


```python
def redrawAll(app):
    drawLine(x1, y1, x2, y2, fill='black',
         lineWidth=2, dashes=False, opacity=100,
         arrowStart=False, arrowEnd=False)
    # dashes = (dashWidth, gapWidth)
```

## Labels


```python
def redrawAll(app):
    drawLabel(value, centerX, centerY,
          size=12, font='arial',
          bold=False, italic=False,
          fill='black', border=None, borderWidth=2,
          opacity=100, rotateAngle=0, align='center')
    
    # symbols
    clubSymbol = chr(0x2663)
    drawLabel(clubSymbol, 200, 200, size=200, font='symbols')
```

## Intersections


```python

```

# 3.4 Mouse Events

# 3.5 Key Events

## Key presses


```python
def onAppStart(app):
    app.rectColor = 'yellow'
    
def onKeyPress(app, key):
    if key == 'r':
        app.rectColor = 'red'
    elif key == 'b':
        app.rectColor = 'blue'
```

## Key names


```python
#repr(key)
```

## Arrow keys


```python
def onAppStart(app):
    app.cx = 200
    app.cy = 200

def redrawAll(app):
    drawLabel('Move the dot with the arrow keys', 200, 30)
    drawCircle(app.cx, app.cy, 50, fill='orange')

def onKeyPress(app, key):
    if key == 'left':    app.cx -= 10
    elif key == 'right': app.cx += 10
    elif key == 'up':    app.cy -= 10
    elif key == 'down':  app.cy += 10

def main():
    runApp()
```

## Key releases


```python
def onKeyRelease(app, key):
    pass
```

# 3.6 Timer Events


```python
def onStep(app):
    pass
```


```python
def onAppStart(app):
    app.counter = 0
    app.paused = False

def redrawAll(app):
    drawLabel('Press p to pause or unpause', 200, 30)
    drawLabel('Press s to step while paused', 200, 50)
    drawLabel(str(app.counter), 200, 200, size=20)

def onStep(app):
    if not app.paused:
        takeStep(app)

def takeStep(app):
    app.counter += 1

def onKeyPress(app, key):
    if key == 'p':
        app.paused = not app.paused
    elif key == 's' and app.paused:
        takeStep(app)

def main():
    runApp()
```


```python

```


```python

```


```python

```


```python

```


```python

```


```python

```


```python

```


```python

```

# 3.9 Calling runApp with Optional Arguments

## Custom Canvas Width and Height


```python
def main():
    runApp(width=600, height=700)
```

## Optional Arguments


```python
def onAppStart(app, name=None):
    if name == None:
        app.message = 'You did not provide a name!'
    else:
        app.message = f'Hello, {name}!'

def redrawAll(app):
    drawLabel(app.message, 200, 200, size=16)

def main():
    runApp(name='David')
```


```python

```


```python

```


```python

```


```python

```

import pyglet
from pyglet.window import key
from pyglet import shapes as sh

wind = pyglet.window.Window(720, 600)
pak = pyglet.graphics.Batch() 


xy = {
    "A": {"x": 102, "y": 330},
    "B": {"x": 204, "y": 380},
    "C": {"x": 408, "y": 380},
    "D": {"x": 510, "y": 330},
    "E": {"x": 306, "y": 430},
    "F": {"x": 306, "y": 330},
    "G": {"x": 306, "y": 230},
    "H": {"x": 256, "y": 130},
    "I": {"x": 256, "y": 30},
    "J": {"x": 356, "y": 130},
    "K": {"x": 356, "y": 30}
    }

keyboard = {
    key.A: "A",
    key.B: "B",
    key.C: "C",
    key.D: "D",
    key.E: "E",
    key.F: "F",
    key.G: "G",
    key.H: "H",
    key.I: "I",
    key.J: "J",
    key.K: "K"
    }

line = {
    'AB': sh.Line(xy['A']['x'], xy['A']['y'], xy['B']['x'], xy['B']['y'], 20, color=(133, 133, 133), batch=pak),
    'BE': sh.Line(xy['B']['x'], xy['B']['y'], xy['E']['x'], xy['E']['y'], 20, color=(133, 133, 133), batch=pak),
    'EC': sh.Line(xy['E']['x'], xy['E']['y'], xy['C']['x'], xy['C']['y'], 20, color=(133, 133, 133), batch=pak),
    'CD': sh.Line(xy['C']['x'], xy['C']['y'], xy['D']['x'], xy['D']['y'], 20, color=(133, 133, 133), batch=pak),
    'EF': sh.Line(xy['E']['x'], xy['E']['y'], xy['F']['x'], xy['F']['y'], 20, color=(133, 133, 133), batch=pak),
    'FG': sh.Line(xy['F']['x'], xy['F']['y'], xy['G']['x'], xy['G']['y'], 20, color=(133, 133, 133), batch=pak),
    'GH': sh.Line(xy['G']['x'], xy['G']['y'], xy['H']['x'], xy['H']['y'], 20, color=(133, 133, 133), batch=pak),
    'HI': sh.Line(xy['H']['x'], xy['H']['y'], xy['I']['x'], xy['I']['y'], 20, color=(133, 133, 133), batch=pak),
    'GJ': sh.Line(xy['G']['x'], xy['G']['y'], xy['J']['x'], xy['J']['y'], 20, color=(133, 133, 133), batch=pak),
    'JK': sh.Line(xy['J']['x'], xy['J']['y'], xy['K']['x'], xy['K']['y'], 20, color=(133, 133, 133), batch=pak)
}

head = sh.Circle(xy['E']['x'], xy['E']['y'] + 80, 80, color=(133, 133, 133), batch=pak)
head_hole = sh.Circle(head.x, head.y, 60, color=(0, 0, 0), batch=pak)

point = {
    'A': sh.Circle(xy['A']['x'], xy['A']['y'], 10, color=(255, 255, 255), batch=pak),
    'B': sh.Circle(xy['B']['x'], xy['B']['y'], 10, color=(255, 255, 255), batch=pak),
    'C': sh.Circle(xy['C']['x'], xy['C']['y'], 10, color=(255, 255, 255), batch=pak),
    'D': sh.Circle(xy['D']['x'], xy['D']['y'], 10, color=(255, 255, 255), batch=pak),
    'E': sh.Circle(xy['E']['x'], xy['E']['y'], 10, color=(255, 255, 255), batch=pak),
    'F': sh.Circle(xy['F']['x'], xy['F']['y'], 10, color=(255, 255, 255), batch=pak),
    'G': sh.Circle(xy['G']['x'], xy['G']['y'], 10, color=(255, 255, 255), batch=pak),
    'H': sh.Circle(xy['H']['x'], xy['H']['y'], 10, color=(255, 255, 255), batch=pak),
    'I': sh.Circle(xy['I']['x'], xy['I']['y'], 10, color=(255, 255, 255), batch=pak),
    'J': sh.Circle(xy['J']['x'], xy['J']['y'], 10, color=(255, 255, 255), batch=pak),
    'K': sh.Circle(xy['K']['x'], xy['K']['y'], 10, color=(255, 255, 255), batch=pak)
}

texts = {
    'A': pyglet.text.Label('A', xy['A']['x'] - 5, xy['A']['y'] - 5, color=(0, 0, 0), batch=pak),
    'B': pyglet.text.Label('B', xy['B']['x'] - 5, xy['B']['y'] - 5, color=(0, 0, 0), batch=pak),
    'C': pyglet.text.Label('C', xy['C']['x'] - 5, xy['C']['y'] - 5, color=(0, 0, 0), batch=pak),
    'D': pyglet.text.Label('D', xy['D']['x'] - 5, xy['D']['y'] - 5, color=(0, 0, 0), batch=pak),
    'E': pyglet.text.Label('E', xy['E']['x'] - 5, xy['E']['y'] - 5, color=(0, 0, 0), batch=pak),
    'F': pyglet.text.Label('F', xy['F']['x'] - 5, xy['F']['y'] - 5, color=(0, 0, 0), batch=pak),
    'G': pyglet.text.Label('G', xy['G']['x'] - 5, xy['G']['y'] - 5, color=(0, 0, 0), batch=pak),
    'H': pyglet.text.Label('H', xy['H']['x'] - 5, xy['H']['y'] - 5, color=(0, 0, 0), batch=pak),
    'I': pyglet.text.Label('I', xy['I']['x'] - 2, xy['I']['y'] - 5, color=(0, 0, 0), batch=pak),
    'J': pyglet.text.Label('J', xy['J']['x'] - 5, xy['J']['y'] - 5, color=(0, 0, 0), batch=pak),
    'K': pyglet.text.Label('K', xy['K']['x'] - 5, xy['K']['y'] - 5, color=(0, 0, 0), batch=pak)
    }


keys = 'A'
text_key = pyglet.text.Label('A', 20, 540, font_size=40, color=(255, 255, 255), batch=pak)

@wind.event
def on_key_press(symbol, modifiers):
    global keys
    global keyboard

    keys = keyboard[symbol]
    text_key.text = keys


@wind.event
def on_mouse_press(x, y, button, modifiers):
    global xy
    global keys
    global line
    global point
    global texts
    global head
    global head_hole

    xy[keys]['x'] = x
    xy[keys]['y'] = y

    point[keys].x = x
    point[keys].y = y

    texts[keys].x = x - (texts[keys].content_width // 2)
    texts[keys].y = y - 5

    for i in line:
        if keys in i:
            if keys == i[0]:
                key_2 = i[1]
            else:
                key_2 = i[0]

            line[i] = sh.Line(
                xy[keys]['x'], xy[keys]['y'], 
                xy[key_2]['x'], xy[key_2]['y'], 
                20, color=(133, 133, 133), batch=pak
                )


    head = sh.Circle(xy['E']['x'], xy['E']['y'] + 80, 80, color=(133, 133, 133), batch=pak)
    head_hole = sh.Circle(head.x, head.y, 60, color=(0, 0, 0), batch=pak)



@wind.event
def on_draw():
    wind.clear()
    pak.draw()

pyglet.app.run()

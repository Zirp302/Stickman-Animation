from math import sin, cos
import pyglet
from pyglet.window import key
from pyglet import shapes as sh

wind = pyglet.window.Window(720, 600)
pak = pyglet.graphics.Batch() 

group0 = pyglet.graphics.Group(0)
group1 = pyglet.graphics.Group(1)
group2 = pyglet.graphics.Group(2)
group3 = pyglet.graphics.Group(3)
group4 = pyglet.graphics.Group(4)

# Значения клавишь для их присвоения переменной keys
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

# Координаты всех точек
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

# Все точки
points = {
    'A': sh.Circle(xy['A']['x'], xy['A']['y'], 10, color=(255, 255, 255), batch=pak, group=group3),
    'B': sh.Circle(xy['B']['x'], xy['B']['y'], 10, color=(255, 255, 255), batch=pak, group=group3),
    'C': sh.Circle(xy['C']['x'], xy['C']['y'], 10, color=(255, 255, 255), batch=pak, group=group3),
    'D': sh.Circle(xy['D']['x'], xy['D']['y'], 10, color=(255, 255, 255), batch=pak, group=group3),
    'E': sh.Circle(xy['E']['x'], xy['E']['y'], 10, color=(255, 255, 255), batch=pak, group=group3),
    'F': sh.Circle(xy['F']['x'], xy['F']['y'], 10, color=(255, 255, 255), batch=pak, group=group3),
    'G': sh.Circle(xy['G']['x'], xy['G']['y'], 10, color=(255, 255, 255), batch=pak, group=group3),
    'H': sh.Circle(xy['H']['x'], xy['H']['y'], 10, color=(255, 255, 255), batch=pak, group=group3),
    'I': sh.Circle(xy['I']['x'], xy['I']['y'], 10, color=(255, 255, 255), batch=pak, group=group3),
    'J': sh.Circle(xy['J']['x'], xy['J']['y'], 10, color=(255, 255, 255), batch=pak, group=group3),
    'K': sh.Circle(xy['K']['x'], xy['K']['y'], 10, color=(255, 255, 255), batch=pak, group=group3)
    }

# Все линии соеденяющие точки
line = {
    'AB': sh.Line(xy['A']['x'], xy['A']['y'], xy['B']['x'], xy['B']['y'], 20, color=(133, 133, 133), batch=pak, group=group2),
    'BE': sh.Line(xy['B']['x'], xy['B']['y'], xy['E']['x'], xy['E']['y'], 20, color=(133, 133, 133), batch=pak, group=group2),
    'EC': sh.Line(xy['E']['x'], xy['E']['y'], xy['C']['x'], xy['C']['y'], 20, color=(133, 133, 133), batch=pak, group=group2),
    'CD': sh.Line(xy['C']['x'], xy['C']['y'], xy['D']['x'], xy['D']['y'], 20, color=(133, 133, 133), batch=pak, group=group2),
    'EF': sh.Line(xy['E']['x'], xy['E']['y'], xy['F']['x'], xy['F']['y'], 20, color=(133, 133, 133), batch=pak, group=group2),
    'FG': sh.Line(xy['F']['x'], xy['F']['y'], xy['G']['x'], xy['G']['y'], 20, color=(133, 133, 133), batch=pak, group=group2),
    'GH': sh.Line(xy['G']['x'], xy['G']['y'], xy['H']['x'], xy['H']['y'], 20, color=(133, 133, 133), batch=pak, group=group2),
    'HI': sh.Line(xy['H']['x'], xy['H']['y'], xy['I']['x'], xy['I']['y'], 20, color=(133, 133, 133), batch=pak, group=group2),
    'GJ': sh.Line(xy['G']['x'], xy['G']['y'], xy['J']['x'], xy['J']['y'], 20, color=(133, 133, 133), batch=pak, group=group2),
    'JK': sh.Line(xy['J']['x'], xy['J']['y'], xy['K']['x'], xy['K']['y'], 20, color=(133, 133, 133), batch=pak, group=group2)
    }

# Текст для обозначения точек
texts = {
    'A': pyglet.text.Label('A', xy['A']['x'] - 5, xy['A']['y'] - 5, color=(0, 0, 0), batch=pak, group=group4),
    'B': pyglet.text.Label('B', xy['B']['x'] - 4, xy['B']['y'] - 5, color=(0, 0, 0), batch=pak, group=group4),
    'C': pyglet.text.Label('C', xy['C']['x'] - 4, xy['C']['y'] - 5, color=(0, 0, 0), batch=pak, group=group4),
    'D': pyglet.text.Label('D', xy['D']['x'] - 5, xy['D']['y'] - 5, color=(0, 0, 0), batch=pak, group=group4),
    'E': pyglet.text.Label('E', xy['E']['x'] - 4, xy['E']['y'] - 5, color=(0, 0, 0), batch=pak, group=group4),
    'F': pyglet.text.Label('F', xy['F']['x'] - 3, xy['F']['y'] - 5, color=(0, 0, 0), batch=pak, group=group4),
    'G': pyglet.text.Label('G', xy['G']['x'] - 5, xy['G']['y'] - 5, color=(0, 0, 0), batch=pak, group=group4),
    'H': pyglet.text.Label('H', xy['H']['x'] - 5, xy['H']['y'] - 5, color=(0, 0, 0), batch=pak, group=group4),
    'I': pyglet.text.Label('I', xy['I']['x'] - 2, xy['I']['y'] - 5, color=(0, 0, 0), batch=pak, group=group4),
    'J': pyglet.text.Label('J', xy['J']['x'] - 2, xy['J']['y'] - 5, color=(0, 0, 0), batch=pak, group=group4),
    'K': pyglet.text.Label('K', xy['K']['x'] - 4, xy['K']['y'] - 5, color=(0, 0, 0), batch=pak, group=group4)
    }

xy_del = xy.copy()
for i in xy:
    xy_del[i] = xy[i].copy()


# Круг для создания головы и чёрной дырки в ней
head = sh.Circle(xy['E']['x'], xy['E']['y'] + 80, 80, color=(133, 133, 133), batch=pak, group=group0)
head_hole = sh.Circle(head.x, head.y, 60, color=(0, 0, 0), batch=pak, group=group1)
# Угол наклона головы
ugl_head_pi = 157080

# Ключ для texts и points
keys = 'A'
# Показатель передвигаемой точки
text_key = pyglet.text.Label('A', 20, 540, font_size=40, color=(255, 255, 255), batch=pak, group=group4)
head_size = False
head_thickness = False

@wind.event
def on_key_press(symbol, modifiers):
    global keys, keyboard, head_size, head_thickness, ugl_head_pi
    global xy, texts, points, line, xy_del

    # Переопределение ключа под одну из передвигаемых точек
    if symbol in keyboard:
        keys = keyboard[symbol]
        text_key.text = keys
    # Проверка нажатия на Shift
    elif symbol == key.LSHIFT or symbol == key.RSHIFT:
        head_size = True
    # Проверка нажатия на Ctrl
    elif symbol == key.LCTRL or symbol == key.RCTRL:
        head_thickness = True
    # Проверка нажатия на клавиши удаления
    elif symbol == key.DELETE or symbol == key.BACKSPACE:
        # Сбрасывет все координыаты до изначальных
        for i in xy_del:
            xy[i] = xy_del[i].copy()
        
        # Возвращает все линии на изначальные позиции
        for key_line in line:
            line[key_line].x = xy[key_line[0]]['x']
            line[key_line].y = xy[key_line[0]]['y']
            line[key_line].x2 = xy[key_line[1]]['x']
            line[key_line].y2 = xy[key_line[1]]['y']
        
        # Возвращает все точки и текст на изначальные позиции
        for i in points:
            points[i].x = xy[i]['x']
            points[i].y = xy[i]['y']

            texts[i].x = xy[i]['x'] - texts[i].content_width // 2
            texts[i].y = xy[i]['y'] - 5
            print(i, texts[i].content_width // 2)
        
        head.radius = 80
        head_hole.radius = 60
        ugl_head_pi = 157080

        head.x = xy['E']['x']
        head.y = xy['E']['y'] + head.radius

        head_hole.x = head.x
        head_hole.y = head.y
        

            


@wind.event
def on_key_release(symbol, modifiers):
    global head_size, head_thickness

    # Проверка отжатия Shift
    if symbol == key.LSHIFT or symbol == key.RSHIFT:
        head_size = False
    # Проверка отжатия Ctrl
    elif symbol == key.LCTRL or symbol == key.RCTRL:
        head_thickness = False


@wind.event
def on_mouse_press(x, y, button, modifiers):
    global xy, keys, line, points, texts, head, head_hole

    xy[keys]['x'] = x
    xy[keys]['y'] = y

    points[keys].x = x
    points[keys].y = y

    texts[keys].x = x - texts[keys].content_width // 2
    texts[keys].y = y - 5

    for i in line:
        if keys in i:
            if keys == i[0]:
                key_2 = i[1]
            else:
                key_2 = i[0]

            line[i].x = xy[keys]['x']
            line[i].y = xy[keys]['y']
            line[i].x2 = xy[key_2]['x']
            line[i].y2 = xy[key_2]['y']

    head.x = round(xy['E']['x'] + head.radius * cos(ugl_head_pi / 100000), 3)
    head.y = round(xy['E']['y'] + head.radius * sin(ugl_head_pi / 100000), 3)
    head_hole.x = head.x
    head_hole.y = head.y 


@wind.event
def on_mouse_scroll(x, y, scroll_x, scroll_y):
    global xy, head, head_hole, ugl_head_pi

    if head_size:
        if head.radius + scroll_y >= 0:
            head.radius += scroll_y
            head_hole.radius += scroll_y
    
    elif head_thickness:
        if head.radius + 1 >= head_hole.radius - scroll_y >= 0:
            head_hole.radius -= scroll_y
    
    else:
        ugl_head_pi += 31416 * scroll_y
        if ugl_head_pi > 628318 or ugl_head_pi < -628318:
            ugl_head_pi = 0
    
    head.x = round(xy['E']['x'] + head.radius * cos(ugl_head_pi / 100000), 3)
    head.y = round(xy['E']['y'] + head.radius * sin(ugl_head_pi / 100000), 3)
    
    head_hole.x = head.x
    head_hole.y = head.y 



# Отрисовка 
@wind.event
def on_draw():
    wind.clear()
    pak.draw()

pyglet.app.run()

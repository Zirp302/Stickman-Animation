import pyglet 

class Kador:
    def __init__(self, wind):
        self.mp4 = []
        self.wind = wind
        self.width = wind.width
        self.height = wind.height
        self.vid = pyglet.shapes.Circle(9, 9, 9)
    
    def screen(self):
        b = (pyglet.gl.GLubyte * (self.width * self.height * 3))()
        pyglet.gl.glReadPixels(0, 0, self.width, self.height, pyglet.gl.GL_RGB, pyglet.gl.GL_UNSIGNED_BYTE, b)
        self.img = pyglet.image.ImageData(self.width, self.height, 'RGB', b)

        self.mp4.append(self.img)

    def video(self):
        self.an = pyglet.image.Animation.from_image_sequence(self.mp4, duration=0.4, loop=True)
        
        self.vid = pyglet.sprite.Sprite(self.an)

        self.vid.scale = 0.2
        





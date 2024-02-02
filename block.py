import pyxel

class Block:
    def __init__(self, x, y, img_path):
        self.x = x
        self.y = y
        self.img_path = img_path
        self.img_id = pyxel.image(0).load(0, 0, img_path)

    def draw(self):
        pyxel.blt(self.x, self.y, 0, 0, 0, 16, 16, 0)
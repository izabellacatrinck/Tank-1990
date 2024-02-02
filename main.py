import pyxel


class Block:
    def __init__(self, x, y, img_path):
        self.x = x
        self.y = y
        self.img_path = img_path
        self.img_id = pyxel.image(0).load(0, 0, img_path)

    def draw(self):
        pyxel.blt(self.x, self.y, 0, 0, 0, 16, 16, 0)
class TankGame:
    def __init__(self):
        pyxel.init(160, 120)
        pyxel.image(0).load(0, 0, "assets")
        self.blocks = [Block(20, 20, "block.bmp")]
        self.setup()

    def setup(self):
        pyxel.run(self.update, self.draw)

    # def update(self):

    def draw(self):
        pyxel.cls(0)
        for block in self.blocks:
            block.draw()


if __name__ == "__main__":
    TankGame()

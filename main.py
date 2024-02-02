from PIL import Image
import pyxel

def resize_image(src_path, dest_path, new_size):
    image = Image.open(src_path)
    resized_image = image.resize(new_size)
    resized_image.save(dest_path)

# Redimensione as imagens antes de carregá-las no Pyxel
resize_image("assets/tank.png", "assets/tank_resized.png", (16, 16))
resize_image("assets/tank1.png", "assets/tank1_resized.png", (16, 16))
resize_image("assets/tank2.png", "assets/tank2_resized.png", (16, 16))
resize_image("assets/tank3.png", "assets/tank3_resized.png", (16, 16)) # Remova esta linha se você não tiver uma quarta imagem
resize_image("assets/bullet.png", "assets/bullet_resized.png", (16, 16))
resize_image("assets/wall_orginal.bmp", "assets/block_resized.png", (16, 16))

class Tank:
    def __init__(self, x, y, image_index):
        self.x = x
        self.y = y
        self.image_index = image_index

    def draw(self):
        if 0 <= self.image_index < len(pyxel.images):
            pyxel.blt(
                self.x,
                self.y,
                self.image_index,
                0,
                0,
                16,
                16,
                0
            )

    def move(self, dx, dy):
        new_x = self.x + dx
        new_y = self.y + dy

        if 0 < new_x < pyxel.width - 16 and 0 < new_y < pyxel.height - 16:
            self.x = new_x
            self.y = new_y

class Bullet:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.active = False

    def draw(self):
        if self.active:
            pyxel.blt(
                self.x,
                self.y,
                4,  # Altere o índice da imagem para 3
                0,
                0,
                16,
                16,
                0
            )

    def move(self):
        if self.active:
            self.y -= 4
            if self.y < 0:
                self.active = False

class Block:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        pyxel.blt(
            self.x,
            self.y,
            5,  # Altere o índice da imagem para 4
            0,
            0,
            16,
            16,
            0
        )

class TankGame:
    def __init__(self):
        pyxel.init(320, 240, fps=30)

        # Carregando imagens redimensionadas
        pyxel.images[0].load(0, 0, "assets/tank_resized.png")
        pyxel.images[1].load(0, 0, "assets/tank1_resized.png")
        pyxel.images[2].load(0, 0, "assets/tank2_resized.png")
        pyxel.images[3].load(0, 0, "assets/tank3_resized.png") # Remova esta linha se você não tiver uma quarta imagem
        pyxel.images[4].load(0, 0, "assets/bullet_resized.png")
        pyxel.images[5].load(0, 0, "assets/block_resized.png")

        self.tanks = [Tank(50, 200, 0), Tank(120, 200, 1), Tank(190, 200, 2)]
        self.bullet = Bullet(-1, -1)
        self.blocks = [Block(60, 60), Block(150, 60), Block(240, 60)]
        self.score = 0
        self.current_tank = 0
        pyxel.run(self.update, self.draw)

    def update(self):
        self.tanks[self.current_tank].move(0, 0)
        self.bullet.move()
        self.handle_input()
        self.check_collisions()

    def draw(self):
        pyxel.cls(0)
        self.tanks[self.current_tank].draw()
        self.bullet.draw()
        for block in self.blocks:
            block.draw()
        pyxel.text(10, 10, f"Score: {self.score}", 7)

    def handle_input(self):
        if pyxel.btn(pyxel.KEY_LEFT) and self.tanks[self.current_tank].x > 0:
            self.tanks[self.current_tank].move(-2, 0)
        elif pyxel.btn(pyxel.KEY_RIGHT) and self.tanks[self.current_tank].x < pyxel.width - 16:
            self.tanks[self.current_tank].move(2, 0)

        if pyxel.btn(pyxel.KEY_UP):
            self.current_tank = 0
        elif pyxel.btn(pyxel.KEY_RIGHT):
            self.current_tank = 1
        elif pyxel.btn(pyxel.KEY_DOWN):
            self.current_tank = 2
        elif pyxel.btn(pyxel.KEY_LEFT):
            self.current_tank = 3 if len(self.tanks) > 3 else 0

        if pyxel.btnp(pyxel.KEY_SPACE) and not self.bullet.active:
            self.bullet.active = True
            self.bullet.x = self.tanks[self.current_tank].x
            self.bullet.y = self.tanks[self.current_tank].y

    def check_collisions(self):
        for block in self.blocks:
            if (
                self.bullet.x + 3 >= block.x
                and self.bullet.x <= block.x + 16
                and self.bullet.y <= block.y + 16
                and self.bullet.y + 3 >= block.y
            ):
                self.bullet.active = False
                self.blocks.remove(block)
                self.score += 10

if __name__ == "__main__":
    TankGame()

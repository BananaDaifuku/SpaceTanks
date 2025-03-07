class Projectile:
    def __init__(self, x: float, y: float, direction):
        self.x = x
        self.y = y
        self.direction = direction
        self.power = 1
        self.speed = 1
        self.sprite = None

    def move(self):
        self.x += self.direction[0]
        self.y += self.direction[1]

    def destroy(self):
        pass

    def draw(self):
        pass
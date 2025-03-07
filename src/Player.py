import pygame

class Player:
    def __init__(self, uid : int, left_key, right_key):
        self.speed = 5
        self.projectileStrength = 1
        self.projectileSpeed = 5
        self.theta = 0 # Angle in radians, we're using this as the map is a circle
        self.gunLength = 10
        self.gunAngle = 90 # Angle in degrees, 90 means it points straight 'up'
        self.isPaused = False

        self.id = uid
        self.left_key = left_key
        self.right_key = right_key

        self.sprite = None

    def fire(self):
        pass

    def move(self, direction : int):
        pass

    def draw(self):
        pass

    def pause(self, paused : bool):
        self.isPaused = paused

    def handle_event(self, event : pygame.event):
        if event.type == pygame.KEYDOWN:
            if event.key == self.right_key:
                print("Player", self.id, "right")
            if event.key == self.left_key:
                print("Player", self.id, "left")

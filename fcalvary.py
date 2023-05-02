
import math

class calvary_U:
    def __init__(self, x, y):
        self.center_x = x
        self.center_y = y
        self.velocity = 0
        self.rotation = 0

        self.goto = (self.center_x, self.center_y)
        self.agility = .1
    def update(self):



        angle_rad = math.radians(self.rotation)
        self.center_x += -math.sin(angle_rad) * self.velocity
        self.center_y += math.cos(angle_rad) * self.velocity

        if self.rotation > 360:
            self.rotation -= 360
        if self.rotation < 0:
            self.rotation += 360

        goal_rot = 20
        print(self.rotation)
        if self.rotation > goal_rot:
            self.rotation -= self.agility
        if self.rotation < goal_rot:
            self.rotation += self.agility

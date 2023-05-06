import arcade
import math
from nural_net import *

class calvary_U(arcade.Sprite):
    def __init__(self, x, y, brain):
        self.x = x
        self.y = y
        self.velocity = 1
        self.rotation = 0
        self._position = (100, 100)
        self.goto = (200, 200)
        self.agility = 1
        self.goal_rot = 0

        self.cal_Brain = brain
        self.memory = [0, 0, 0, 0, 0, 0, 0, 0]
        self.MAX_SPEED = 7
        self.speed_up = .1
    def update(self):

        #self.rotation += 2

        angle_rad = math.radians(self.rotation)
        if self.velocity >= self.MAX_SPEED:
            self.velocity = self.MAX_SPEED
        if self.velocity <= -self.MAX_SPEED:
            self.velocity = -self.MAX_SPEED

        self.x += -math.sin(angle_rad) * self.velocity
        self.y += math.cos(angle_rad) * self.velocity

        input_2_Brain = [self.x, self.y, self.rotation, self.goto[0], self.goto[1], self.velocity]
        for i in range(len(self.memory)):
            input_2_Brain.append(self.memory[i])

        output = self.cal_Brain.plugin_info(input_2_Brain)
        print(output)
        print(output[0])
        output[0] -= 1
        if output[0] >= 0:
            self.rotation += self.agility
        if output[0] <= 0:
            self.rotation -= self.agility
        output.pop(0)
        output[0] -= 5
        if output[0] >= 0:
            self.velocity += self.speed_up
        if output[0] <= 0:
            self.velocity -= self.speed_up
        output.pop(0)
        self.memory = output
        # self.goal_rot = math.degrees(math.tanh(abs(self.goto[1]-self.y)/abs(self.goto[0]-self.x)))
        # self.goal_rot -= 90
        # if self.goto[0] >= self.x:
        #     pass
        # else:
        #     self.goal_rot += 180
        # #self.rotation = self.goal_rot + 270
        #
        # #self.rotation = self.goal_rot
        # print("goto", self.goal_rot)
        # print("rot", self.rotation)
        # if self.rotation > self.goal_rot:
        #     self.rotation -= self.agility
        # if self.rotation < self.goal_rot:
        #     self.rotation += self.agility

        # if self.rotation > 360:
        #     self.rotation -= 360
        # if self.rotation < 0:
        #     self.rotation += 360
        #self.rotation += 1

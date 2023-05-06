"""
Starting Template

Once you have learned how to use classes, you can begin your program with this
template.

If Python and Arcade are installed, this example can be run from the command line with:
python -m arcade.examples.starting_template
"""
import arcade
from fcalvary import *
import test
from nural_net import *

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Starting Template"





class MyGame(arcade.Window):
    """
    Main application class.

    NOTE: Go ahead and delete the methods you don't need.
    If you do need a method, delete the 'pass' and replace it
    with your own code. Don't leave 'pass' in this program.
    """

    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        arcade.set_background_color(arcade.color.AMAZON)

        # If you have sprite lists, you should create them here,
        # and set them to None

    def setup(self):
        """ Set up the game variables. Call to re-start the game. """
        # Create your sprites and sprite lists here
        self.test = calvary_U(100, 100, Brain([2+1+2+1+8, 5, 8+1+1]))

        self.test.rotation = 0

    def on_draw(self):
        """
        Render the screen.
        """

        # This command should happen before we start drawing. It will clear
        # the screen to the background color, and erase what we drew last frame.
        self.clear()

        arcade.draw_rectangle_filled(self.test.x, self.test.y, width=10, height= 20, color=(255, 255, 255), tilt_angle=-self.test.rotation)
        arcade.draw_line(self.test.x, self.test.y, -math.sin((math.radians(self.test.rotation))) * 10 * self.test.velocity + self.test.x, math.cos((math.radians(self.test.rotation))) * 10 * self.test.velocity + self.test.y, arcade.color.WOOD_BROWN, 3)
        arcade.draw_line(self.test.x, self.test.y,
                         -math.sin((math.radians(self.test.goal_rot))) * 10 * self.test.velocity + self.test.x,
                         math.cos((math.radians(self.test.goal_rot))) * 10 * self.test.velocity + self.test.y,
                         arcade.color.WOOD_BROWN, 3)
        # Call draw() on all your sprite lists below

    def on_update(self, delta_time):
        """
        All the logic to move, and the game logic goes here.
        Normally, you'll call update() on the sprite lists that
        need it.
        """

        print("pos", self.test.x, self.test.x)
        self.test.update()

    def on_key_press(self, key, key_modifiers):
        """
        Called whenever a key on the keyboard is pressed.

        For a full list of keys, see:
        https://api.arcade.academy/en/latest/arcade.key.html
        """
        pass

    def on_key_release(self, key, key_modifiers):
        """
        Called whenever the user lets off a previously pressed key.
        """
        pass

    def on_mouse_motion(self, x, y, delta_x, delta_y):
        """
        Called whenever the mouse moves.
        """
        self.test.goto = (x, y)
        print((x, y))

    def on_mouse_press(self, x, y, button, key_modifiers):
        """
        Called when the user presses a mouse button.
        """
        pass

    def on_mouse_release(self, x, y, button, key_modifiers):
        """
        Called when a user releases a mouse button.
        """
        pass


def main():
    """ Main function """
    game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    game.setup()
    arcade.run()


if __name__ == "__main__":
    main()
import pygame


class Simulator(object):
    """
    This class draw LEDs on the screen.

    In the init it gets the (x,y) mapping of each LED in the "real world".

    In the draw_LEDs it gets the color of each LED.

    When calling draw_LEDs it draws the leds based on
    the color and position of each led.

    Note: This class assumes you call pygame.init()
    before you create an instance of the simulator
    """

    def __init__(self, size, mapping):
        """ Init a new LEDs simulator.

        size - array with width and height: [width, height]

        mapping - array of positions (x,y) tupple:
        the value of each index should mimic
        the real (x,y) position of this LED.
        """
        self.size = size
        self.screen = pygame.display.set_mode(size)
        self.mapping = mapping
        print "__init__"
        # self.__verify_mapping()

    def draw_LEDs(self, leds):
        """ Draw leds on screen.

        This method cleans the screen and draw it again
        based on the leds array.

        leds - an array of [r, g, b]: each index represnets a led,
        each value is it's color.

        This method will draw the leds
        based on their current color and init mapping.
        """
        # print self.screen

        #pygame.draw.rect(self.screen, leds[0], [0, 0, self.size[0], + self.size[1]], 0)
        self.screen.fill((0,0,0))
        for index in range(len(leds)):
            rect = [self.mapping[index][0], self.mapping[index][1], 10, 10]
            pygame.draw.rect(self.screen, (200,200,200), rect , 0)

        pygame.display.flip()

    def __verify_mapping(self):
        """ Verify the mapping.
        * private method *

        Rasing errors if the user input of the mapping is invalid.
        """
        for pos in self.mapping:
            if len(pos) != 2:
                raise ValueError("Invalid position - " + str(pos) +
                                 " - must be (x,y) tupple")

            if pos[0] < 0 or pos[0] > self.size[0]:
                raise ValueError("Invalid position - " + str(pos) +
                                 " - x value is out of screen")

            if pos[1] < 0 or pos[1] > self.size[0]:
                raise ValueError("Invalid position - " + str(pos) +
                                 " - y value is out of screen")

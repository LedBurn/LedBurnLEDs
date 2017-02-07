import pygame
import colorsys
import DrawingApp_Configuration as Conf


class Drawer(object):
    """

    """
    def __init__(self, screen):
        """ Init a new Drawer instance
        Use this class to draw elements on the screen ao the drawing app.

        screen - the pygame screen
        """
        self.screen = screen

    def draw_grid(self):
        """ Draws the grid lines on the screen
        This method clears the entire grid, and then draws the lines.
        """
        pygame.draw.rect(self.screen, Conf.SCREEN_COLOR, Conf.GRID_RECT, 0)

        for i in range(Conf.NUM_OF_VERT_PIXELS):
            line_x = i * Conf.PIXEL_SIZE + Conf.PIXEL_SIZE - 1
            pygame.draw.line(self.screen, Conf.GRID_COLOR,
                             [line_x, 0], [line_x, Conf.GRID_RECT[3] - 1], 1)

        for i in range(Conf.NUM_OF_HORZ_PIXELS):
            line_y = i * Conf.PIXEL_SIZE + Conf.PIXEL_SIZE - 1
            pygame.draw.line(self.screen, Conf.GRID_COLOR,
                             [0, line_y], [Conf.GRID_RECT[2] - 1, line_y], 1)

    def draw_pixel_array(self, the_array):
        """ Draws a pixel array.

        the_array - an array of (x, y)
        each one representing a square in the grid.

        It draws the array in rainbowish colors
        so you can see the order of the array.
        """
        for index in range(len(the_array)):
            pixel = the_array[index]

            hue = ((index * 3) % 256) / 256.0
            color = colorsys.hsv_to_rgb(hue, 1.0, 1.0)
            color = (int(255 * color[0]),
                     int(255 * color[1]),
                     int(255 * color[2]))
            self.draw_pixel(pixel, color)

    def draw_pixel(self, pixel, color):
        """ Draws one pixel.

        pixel - (x, y) that representing a square in the grid.
        color - (r, g, b) the color of the pixel - 0-256 values
        """
        start_x = pixel[0] * Conf.PIXEL_SIZE
        start_y = pixel[1] * Conf.PIXEL_SIZE

        pygame.draw.rect(self.screen, color, [start_x, start_y,
                         Conf.PIXEL_SIZE, Conf.PIXEL_SIZE], 0)

    def draw_message_text(self, text, color):
        """ Show a message to the user.
        Draws on the screen a message to show the user.
        """
        pygame.draw.rect(self.screen, Conf.SCREEN_COLOR, Conf.MESSAGE_RECT, 0)  # clean

        font = pygame.font.SysFont(pygame.font.get_default_font(), 20)
        text_img = font.render(text, 1, color)
   
        self.screen.blit(text_img, Conf.MESSAGE_RECT)

    def draw_total_text(self, text):
        """ Show the total number of LEDs label.
        """
        pygame.draw.rect(self.screen, Conf.SCREEN_COLOR, Conf.TOTAL_RECT, 0)  # clean

        font = pygame.font.SysFont(pygame.font.get_default_font(), 20)
        text_img = font.render(text, 1, Conf.WHITE)
   
        self.screen.blit(text_img, Conf.TOTAL_RECT)

    def draw_pointer_text(self, text):
        """ Show the current pixel.
        """

        pygame.draw.rect(self.screen, Conf.SCREEN_COLOR, Conf.POINTER_RECT, 0)  # clean

        font = pygame.font.SysFont(pygame.font.get_default_font(), 40)
        text_img = font.render(text, 1, Conf.WHITE)
        img_x = Conf.POINTER_RECT[0] + Conf.POINTER_RECT[2] / 2 - text_img.get_width() / 2
        self.screen.blit(text_img, (img_x, Conf.POINTER_RECT[1]))

    def draw_save_button(self):
        """ Draw the save button. rect + label.
        """

        pygame.draw.rect(self.screen, Conf.GREEN, Conf.SAVE_RECT, 2)

        font = pygame.font.SysFont(pygame.font.get_default_font(), 30)
        text_img = font.render("SAVE", 1, Conf.WHITE)
        img_x = Conf.SAVE_RECT[0] + Conf.SAVE_RECT[2] / 2 - text_img.get_width() / 2
        img_y = Conf.SAVE_RECT[1] + Conf.SAVE_RECT[3] / 2 - text_img.get_height() / 2
        self.screen.blit(text_img, (img_x, img_y))



        

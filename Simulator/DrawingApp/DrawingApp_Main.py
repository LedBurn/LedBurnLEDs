#!/usr/bin/env python

import pygame
import time
import DrawingApp_Configuration as Conf
from DrawingApp_Drawer import Drawer


pygame.init()
screen = pygame.display.set_mode(Conf.SIZE)
pygame.display.set_caption("Drawing LEDs App")
drawer = Drawer(screen)

done = False
clock = pygame.time.Clock()

the_array = []


def pixel_for_pos(pos):
    """ Returns (x,y) tuple - the pixel that matches the position.
    or None if not in the grid.

    pos - (x,y) tuple of the current position on the screen
    """
    if (pos[0] >= Conf.GRID_RECT[2] or pos[1] >= Conf.GRID_RECT[3]):
        return None

    start_x = pos[0] - pos[0] % Conf.PIXEL_SIZE
    start_y = pos[1] - pos[1] % Conf.PIXEL_SIZE

    return (start_x / Conf.PIXEL_SIZE, start_y / Conf.PIXEL_SIZE)


def save_to_file():
    """ Save the current array into txt file
    """
    file_name = "mapping_" + time.strftime("%b_%d__%H_%M_%S") + ".txt"

    text_file = open(file_name, "w")
    text_file.write(str(the_array))
    text_file.close()

    return file_name


while not done:
    clock.tick(150)

    # draw grid
    drawer.draw_grid()

    # draw current pointer
    pos = pygame.mouse.get_pos()
    pixel = pixel_for_pos(pos)
    if pixel is not None:
        drawer.draw_pixel(pixel, Conf.POINTER_COLOR)
    if pixel in the_array:
        drawer.draw_pointer_text(str(pixel) + " - #" + str(the_array.index(pixel)))
    else:
        drawer.draw_pointer_text(str(pixel))

    # draw the array
    drawer.draw_pixel_array(the_array)

    # draw text and buttons
    drawer.draw_save_button()
    drawer.draw_total_text("Total LEDs - " + str(len(the_array)))

    for event in pygame.event.get():  # user did something
        if event.type == pygame.QUIT:
            done = True

        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            pixel = pixel_for_pos(pos)
            save_rect = pygame.Rect(Conf.SAVE_RECT[0], Conf.SAVE_RECT[1], Conf.SAVE_RECT[2], Conf.SAVE_RECT[3])

            if pixel is not None and pixel not in the_array:  # new pixel - add
                the_array.append(pixel)
                drawer.draw_message_text(str(pixel) + " was added", Conf.GREEN)
           
            elif pixel is not None and len(the_array) > 0 and pixel == the_array[-1]:  # last pixel - remove
                the_array.pop()
                drawer.draw_message_text(str(pixel) + " was removed", Conf.ORANGE)

            elif pixel is not None and pixel in the_array:  # in the array - error
                drawer.draw_message_text("You can only remove the last added pixel - " + str(the_array[-1]), Conf.RED)

            elif save_rect.collidepoint(pos):  # save button pressed
                file_name = save_to_file()
                drawer.draw_message_text("Saved as " + file_name, Conf.GREEN)

    # Go ahead and update the screen with what we've drawn.
    # This MUST happen after all the other drawing commands.
    pygame.display.flip()

pygame.quit()

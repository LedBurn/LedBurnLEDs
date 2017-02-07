SIZE = [1200, 680]

PIXEL_SIZE = 12  # pixel size must divide grid size!
GRID_RECT = [0, 0, SIZE[0], SIZE[1] - 80]  # grid rect must start 0,0!
NUM_OF_VERT_PIXELS = GRID_RECT[2] / PIXEL_SIZE
NUM_OF_HORZ_PIXELS = GRID_RECT[3] / PIXEL_SIZE

TEXT_SIZE = (SIZE[1] - GRID_RECT[3]) / 2
PADDING = 13
TOTAL_RECT      = [20,                 SIZE[1] - 2 * TEXT_SIZE + PADDING,      SIZE[0] / 2 - 100 - 20,   TEXT_SIZE - 2 * PADDING]
MESSAGE_RECT    = [20,                 SIZE[1] - TEXT_SIZE + PADDING,          SIZE[0] / 2 - 100 - 20,   TEXT_SIZE - 2 * PADDING]

POINTER_RECT    = [SIZE[0] / 2 - 100,  SIZE[1] - 2 * TEXT_SIZE + PADDING,      200,                      TEXT_SIZE * 2 - 2 * PADDING]

SAVE_RECT       = [SIZE[0] - 150,      SIZE[1] - 2 * TEXT_SIZE + PADDING,      100,                      TEXT_SIZE * 2 - 2 * PADDING]

# --------------------------------------
# |                                    |
# |                                    |
# |                                    |
# |                                    |
# |             grid                   |
# |                                    |
# |                                    |
# |                                    |
# |                                    |
# |                                    |
# |____________________________________|
# | total       | pointer |        save|
# | message     |         |            |
# --------------------------------------


BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
LIGHT_BLUE = (0, 30, 180)
ORANGE = (255, 140, 0)
RED = (255, 0, 0)
WHITE = (200, 200, 200)

SCREEN_COLOR = BLACK
GRID_COLOR = (0, 100, 0)
POINTER_COLOR = WHITE

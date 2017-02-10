# Drawing App

## Usage
Use this app when you have a LED strip in the real world, and you want to have an array of the an (x, y) position for each LED in the strip.

## Start
run `$ python DrawingApp_Main.py`

## How To Use?

##### Draw
Tap on a pixel to add it to the array.
You can also delete the last pixel you draw by tapping it again.

##### Info
In the middle you will see the current (x ,y) of the pixel - use your mouse!
If the current pixel is part of the drawing, you will also see the position of this pixel in the array (starting from 0)

##### Save
Saves an array of (x, y) for each pixel, in the order you draw them.
The file name is mapping_{time}.txt


## Customization
Open DrawingApp_Configuration.py and change one or more:
* SIZE - sets the entire app screen size (min size - [400, 200])
* PIXEL_SIZE - the size of each pixel in the drawing (something between 5 to 20 should be ok)



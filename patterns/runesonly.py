import board
import neopixel

pixels = neopixel.NeoPixel(board.D18, 36)
color = (255, 0, 255)


pixels[1:2] = color
pixels[16:19] = color
pixels[34:35] = color
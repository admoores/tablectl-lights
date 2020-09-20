import board
import neopixel

pixels = neopixel.NeoPixel(board.D18, 36)
pixels.fill((0, 0, 0))
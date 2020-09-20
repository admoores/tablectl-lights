import board
import neopixel
import time

pixels = neopixel.NeoPixel(board.D18, 36)

while True:
  for i in range(36):
    pixels.fill((0, 0, 0))
    pixels[i:i + 5] = (255, 0, 255);
  time.sleep(.1)
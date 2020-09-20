import board
import neopixel
import time

pixels = neopixel.NeoPixel(board.D18, 36)

while True:
  for i in range(36):
    pixels.fill((0, 0, 0))
    pixels[i] = (255, 0, 255);
    pixels[(i + 1) % 36] = (255, 0, 255);
    pixels[(i + 2) % 36] = (255, 0, 255);
    pixels[(i + 3) % 36] = (255, 0, 255);
    pixels[(i + 4) % 36] = (255, 0, 255);
    time.sleep(.01)
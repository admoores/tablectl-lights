import board
import neopixel
import time

pixels = neopixel.NeoPixel(board.D18, 36)
color = (255, 0, 255)

while True:
  for i in range(36):
    pixels.fill((0, 0, 0))
    pixels[i] = color;
    pixels[(i + 1) % 36] = color;
    pixels[(i + 2) % 36] = color;
    pixels[(i + 3) % 36] = color;
    pixels[(i + 4) % 36] = color;
    time.sleep(.01)
  if (color == (255, 0, 255)):
    color = (0, 0, 255)
  elif (color == (0, 0, 255)):
    color = (0, 255, 0)
  elif (color == (0, 255, 0)):
    color = (255, 255, 0)
  elif (color == (255, 255, 0)):
    color = (255, 0, 0)
  else:
    color = (255, 0, 255)
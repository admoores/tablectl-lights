import board
import neopixel
import time

pixels = neopixel.NeoPixel(board.D18, 36)
offset = 0

while True:
  for i in range(36):
    pixels[i] = (
      255 if ((i + offset) % 3) == 0 else 0,
      255 if ((i + offset) % 3) == 1 else 0,
      255 if ((i + offset) % 3) == 2 else 0,
    )
  time.sleep(.5)
  offset = offset + 1
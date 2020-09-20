import board
import neopixel

pixels = neopixel.NeoPixel(board.D18, 36)

for r in range(0, 255, 5):
  for g in range(0, 255, 5):
    for b in range(0, 255, 5):
       pixels.fill((r, g, b))
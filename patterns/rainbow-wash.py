import board
import neopixel

pixels = neopixel.NeoPixel(board.D18, 36)
offset = 0

while true:
  for i in range(36):
    pixels[i] = (
      255 if (i + offset) == 0 else 0,
      255 if (i + offset) == 1 else 0,
      255 if (i + offset) == 2 else 0,
    )
  time.sleep(500)
  offset++
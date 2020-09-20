import board
import neopixel

pixels = neopixel.NeoPixel(board.D18, 36)
offset = 0

while true:
  for i in range(36):
    pixels[i] = (
      ((i + offset) % 3) == 0 ? 255 : 0,
      ((i + offset) % 3) == 1 ? 255 : 0,
      ((i + offset) % 3) == 2 ? 255 : 0,
    )
  time.sleep(500)
  offset++
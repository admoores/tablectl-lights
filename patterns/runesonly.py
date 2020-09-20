import board
import neopixel

pixels = neopixel.NeoPixel(board.D18, 36)

runes = [
  0,
  1,
  16,
  17,
  18,
  19,
  34,
  35
]

for idx in runes:
  pixels[idx] = (255, 0, 255)
import board, neopixel
pixels = neopixel.NeoPixel(board.IO12, 1)
pixels[0] = (20, 0, 20)

import board, time, touchio, neopixel
touch_pad = board.A0
pixels = neopixel.NeoPixel(board.IO12, 1)
touch = touchio.TouchIn(touch_pad)
while True:
    if touch.value:
        pixels[0] = (255, 255, 255)
    else:
        pixels[0] = (0, 0, 0)
    time.sleep(0.1)

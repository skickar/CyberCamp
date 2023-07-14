import board, digitalio, neopixel, time
button = digitalio.DigitalInOut(board.D5)
button.direction = digitalio.Direction.INPUT
button.pull = digitalio.Pull.UP
pixels = neopixel.NeoPixel(board.IO12, 1)
while True: 
    if not button.value:
        pixels[0] = (255, 0, 0)
        time.sleep(0.5)
        pixels[0] = (0, 0, 0)

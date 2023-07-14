import time
import board
import digitalio
import usb_hid
from adafruit_hid.mouse import Mouse

button = digitalio.DigitalInOut(board.D3)
button.direction = digitalio.Direction.INPUT
button.pull = digitalio.Pull.UP

mouse = Mouse(usb_hid.devices)

while True:
    if not button.value:
        mouse.click(Mouse.LEFT_BUTTON)
        time.sleep(0.1)

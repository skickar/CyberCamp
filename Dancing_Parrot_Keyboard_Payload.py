import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.keycode import Keycode
import time
kbd = Keyboard(usb_hid.devices)
layout = KeyboardLayoutUS(kbd)
kbd.send(Keycode.GUI, Keycode.SPACE), time.sleep(.5)
layout.write('terminal.app\n'), time.sleep(1)
layout.write('curl parrot.live\n')

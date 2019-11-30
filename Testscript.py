import neopixel
import board


PIN_1 = board.D18
PIN_2 = board.D16

NUMPIXEL_1 = 205
NUMPIXEL_2 = 230

pixel_1 = neopixel.NeoPixel(PIN_1, NUMPIXEL_1)
pixel_2 = neopixel.NeoPixel(PIN_2, NUMPIXEL_2)

for i in range(NUMPIXEL_1 + NUMPIXEL_2):
    if(i < NUMPIXEL_1):
        pixel_1[i] = (120,120,120)
    else:
        pixel_2[i - NUMPIXEL_1] = (120,120,120)
    pixel_1.show()
    pixel_2.show()
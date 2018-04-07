import time
from neopixel import *

# LED strip configuration
LED_1_COUNT = 119
LED_1_PIN = 18
LED_1_CHANNEL = 0

LED_2_COUNT = 60
LED_2_PIN = 12
LED_2_CHANNEL = 0

LED_3_COUNT = 120
LED_3_PIN = 13
LED_3_CHANNEL = 1

LED_4_COUNT = 120
LED_4_PIN = 19
LED_4_CHANNEL = 1

LED_BRIGHTNESS = 128
LED_FREQ_HZ = 800000
LED_INVERT = False
LED_DMA = 10


class LedController:
    def __init__(self):
        print('Init LED strip controller...')
        self.strip1 = Adafruit_NeoPixel(LED_1_COUNT, LED_1_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_1_CHANNEL)
        self.strip2 = Adafruit_NeoPixel(LED_2_COUNT, LED_2_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_1_CHANNEL)

    def begin(self):
        print("WS2812B strip begin...")
        self.strip1.begin()
        self.strip2.begin()
        self.colorChange(self.strip1, Color(255, 255, 255))
        self.colorChange(self.strip2, Color(255, 255, 255))

    def update(self, data):
        print('change to ' + data)
        r, g, b = data.split('-')
        self.colorChange(self.strip1, Color(int(r), int(g), int(b)))

    def colorChange(self, strip, color):
        for i in range(strip.numPixels()):
            strip.setPixelColor(i, color)
        strip.show()

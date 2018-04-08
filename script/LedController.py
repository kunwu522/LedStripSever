from neopixel import *
import json
from Logo import Logo

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
        leftStrip1 = Adafruit_NeoPixel(LED_1_COUNT, LED_1_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_1_CHANNEL)
        leftStrip2 = Adafruit_NeoPixel(LED_2_COUNT, LED_2_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_2_CHANNEL)
        rightStrip1 = Adafruit_NeoPixel(LED_3_COUNT, LED_3_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_3_CHANNEL)
        rightStrip2 = Adafruit_NeoPixel(LED_4_COUNT, LED_4_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_4_CHANNEL)
        self.leftLogo = Logo([leftStrip1, leftStrip2])
        self.rightLogo = Logo([rightStrip1, rightStrip2])

    def begin(self):
        print("WS2812B strip begin...")
        self.leftLogo.begin()
        self.rightLogo.begin()

    def receive(self, data):
        print('recived json to ' + data)
        parsed_json = json.loads(data)
        for logo in parsed_json:
            if logo['id'] == 1:
                self.leftLogo.update(logo)
            elif logo['id'] == 2:
                self.rightLogo.update(logo)

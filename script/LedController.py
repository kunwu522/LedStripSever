import time

LED_COUNT = 145
LED_PIN = 18


class LedController:
    def begin(self):
        print("WS2812B strip begin...")

    def update(self, data):
        print('change to ' + data)
        r, g, b = data.split('-')

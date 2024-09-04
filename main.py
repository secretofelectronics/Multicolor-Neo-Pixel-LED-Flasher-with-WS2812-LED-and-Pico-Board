import neopixel
from machine import Pin
import time

SW=Pin(1,Pin.IN)

ws_pin = 0
led_num = 2
BRIGHTNESS = 0.2  # Adjust the brightness (0.0 - 1.0)

neoLEDs = neopixel.NeoPixel(Pin(ws_pin), led_num)

# Define colors (in RGB format)
colors = [
    (255, 0, 0),    # Red
    (255, 165, 0),  # Orange
    (255, 255, 0),  # Yellow
    (0, 255, 0),    # Green
    (0, 255, 255),  # Cyan
    (0, 0, 255),    # Blue
    (255, 0, 255),  # Magenta
    (128, 0, 128),  # Purple
    (255, 99, 71),  # Tomato
    (255, 20, 147), # Deep Pink
    (255, 140, 0),  # Dark Orange
    (0, 128, 0),    # Forest Green
    (0, 255, 127),  # Spring Green
    (46, 139, 87),  # Sea Green
    (0, 191, 255),  # Deep Sky Blue
    (0, 0, 128),    # Navy
    (138, 43, 226), # Blue Violet
    (255, 215, 0)   # Gold
]

index = 0  # Initialize color index

# Main loop for police light flasher effect
while True:
    if SW.value():  # Check if button is pressed
        index += 1  # Increment color index
        if index == len(colors):  # Reset index if out of bounds
            index = 0

    color = colors[index]  # Get current color

    # Alternating flashing effect
    for i in range(5):
        neoLEDs[0] = color
        neoLEDs[1] = color
        neoLEDs.write()
        time.sleep_ms(100)  # Flash for 0.1 second
        neoLEDs[0] = (0, 0, 0)
        neoLEDs[1] = (0, 0, 0)
        neoLEDs.write()
        time.sleep_ms(100)  # Pause for 0.1 second

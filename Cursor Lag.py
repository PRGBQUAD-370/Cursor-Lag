import ctypes
import time
import random
from ctypes import wintypes

user32 = ctypes.windll.user32
POINT = wintypes.POINT()

ESC = 0x1B

print("Cursor shaking around screen. Press ESC to stop.")

shake = 6        # jitter strength
move = 3         # roaming speed
delay = 0.01

# Get screen size
screen_w = user32.GetSystemMetrics(0)
screen_h = user32.GetSystemMetrics(1)

while True:
    # Stop on ESC
    if user32.GetAsyncKeyState(ESC) & 0x8000:
        print("Stopped.")
        break

    # Current position
    user32.GetCursorPos(ctypes.byref(POINT))
    x, y = POINT.x, POINT.y

    # Random roaming movement
    x += random.randint(-move, move)
    y += random.randint(-move, move)

    # Shake (jitter)
    x += random.randint(-shake, shake)
    y += random.randint(-shake, shake)

    # Keep cursor on screen
    x = max(0, min(screen_w - 1, x))
    y = max(0, min(screen_h - 1, y))

    user32.SetCursorPos(x, y)
    time.sleep(delay)

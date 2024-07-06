import pyautogui
import time

# 모니터 크기 출력
screen_size = pyautogui.size()
print(f"Screen size: {screen_size}")

# 마우스 위치를 일정 간격으로 출력
def print_mouse_position(interval=1):
    try:
        while True:
            x, y = pyautogui.position()
            print(f"Mouse position: ({x}, {y})")
            time.sleep(interval)
    except KeyboardInterrupt:
        print("Stopped by user")

print("Press Ctrl+C to stop.")
print_mouse_position()

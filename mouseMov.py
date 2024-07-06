import pyautogui
import time

# 드래그할 시작 좌표와 끝 좌표

vidInitPosEnd = (15, 0)
vidInitPosStart = (500, 1035)

print("move start")
pyautogui.moveTo(vidInitPosStart)
pyautogui.drag(vidInitPosEnd, duration=1.0)
import pyautogui
import time
import keyboard


mousePos = (2907, 1051)
start_x = 220
start_y = 1066
end_x = 11
end_y = 1035

vidStartPos = (30,1060)

vidInitPosEnd = (10, 1037)
vidInitPosStart = (35, 1037)

def smooth_Move():
    start_x = 220
    start_y = 1066
    end_x = 11
    end_y = 1035
    # 드래그 거리 계산
    distance_x = end_x - start_x
    distance_y = end_y - start_y

    # 드래그를 진행할 시간 (초)
    duration = 1

    # 드래그 스텝 수와 간격 계산
    steps = int(duration / 0.1)  # 0.1초 간격으로 드래그를 진행할 횟수
    step_x = distance_x / steps
    step_y = distance_y / steps

    # 드래그 진행
    for _ in range(steps):
        start_x += step_x
        start_y += step_y
        pyautogui.moveTo(start_x, start_y)
        time.sleep(0.1)


def click_image(image_path, confidence=0.8):
    """주어진 이미지가 화면에 보이면 해당 위치로 이동하여 클릭"""
    try:
        location = pyautogui.locateCenterOnScreen(image_path, confidence=confidence)
        if location is not None:
            pyautogui.moveTo(location)
            pyautogui.click()
            return True
        return False
    except pyautogui.ImageNotFoundException:
        return False

def switch_to_monitor(monitor_number):
    """지정된 모니터로 마우스를 이동"""
    screen_info = pyautogui.size()
    width, height = screen_info
    if monitor_number == 1:
        pyautogui.moveTo(width / 4, height / 2)  # 모니터 1의 중앙으로 이동
    elif monitor_number == 2:
        pyautogui.moveTo(width * 1.25, height / 2)  # 모니터 2의 중앙으로 이동

def check_for_exit():
    """F1 키 입력을 감지하여 스크립트를 종료"""
    if keyboard.is_pressed('F1'):
        print("F1 pressed. Exiting the script.")
        exit(0)

def main():
    # 최초 녹화 시작
    pyautogui.moveTo(mousePos)
    pyautogui.click()
    while True:
        # F1 키를 감지하여 스크립트 종료
        check_for_exit()


        # 영상 시작 시간 초기화
        smooth_Move()
        pyautogui.moveTo(end_x, end_y)
        pyautogui.click()

        # Step 1: 모니터 1로 전환하고 nextLec 이미지 인식 대기
        switch_to_monitor(1)

        print("Waiting for nextLec.png on monitor 1...")
        while not click_image('nextLec.png', confidence=0.8):
            time.sleep(1)
            check_for_exit()  # F1 키 감지

        pyautogui.moveTo(mousePos)
        pyautogui.click()
        time.sleep(1)
        pyautogui.click()

if __name__ == "__main__":
    main()

import subprocess
import time
import pyautogui
import sys
import os
from datetime import datetime


timeout_seconds = 5
program_name = ['CalculatorApp.exe']

def start_system(system):
   subprocess.Popen(system)

def clear_log_folder():
    log_folder = "log"
    for file in os.listdir(log_folder):
        full_path = os.path.join(log_folder, file)
        try:
            if os.path.isfile(full_path):
                os.remove(full_path)
        except Exception as e:
            print(f"Error deleting file {full_path}: {e}")

def take_screenshot():
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    file_name = f"log/screenshot_{timestamp}.png"
    screenshot = pyautogui.screenshot()
    screenshot.save(file_name)

def find_image(image, timeout=timeout_seconds, click=False, double_click=False, left_click=False):
    start_time = time.time()
    image_found = False

    while time.time() - start_time < timeout:
        coordinates = pyautogui.locateCenterOnScreen(image, grayscale=True, confidence=0.9)

        if coordinates is not None:
            x, y = coordinates
            if click:
                pyautogui.click(x, y)
            elif double_click:
                pyautogui.doubleClick(x, y)
            elif left_click:
                pyautogui.rightClick(x, y)
            image_found = True
            break

        time.sleep(1)
    if not image_found:
        try:
            print(f"Timeout of {timeout} seconds reached. The image {image} was not found.", file=sys.stdout)
            take_screenshot()
            if program_name:
                for program in program_name:
                    with open(os.devnull, 'w') as fnull:
                        subprocess.run(['taskkill', '/F', '/IM', program], stdout=fnull, stderr=fnull)
                time.sleep(2)
                sys.exit(1)
        except subprocess.CalledProcessError:
            sys.exit(1)

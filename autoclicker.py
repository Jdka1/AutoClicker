import pyautogui
import threading
import keyboard
import time

class AutoClicker:
    def __init__(self, interval_seconds=0):
        self.interval_seconds = interval_seconds
        
    def autoclicker_thread(self):
        while True:
            if keyboard.is_pressed('q'):
                print('autoclicker closed.')
                break
            
            pyautogui.click()
            time.sleep(self.interval_seconds)
            
    
    def start_clicking(self):  
        print('starting clicker, press and hold q to close.')
        t = threading.Thread(target=self.autoclicker_thread)
        t.start()

        

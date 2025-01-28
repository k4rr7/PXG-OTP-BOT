import pyautogui
import keyboard
import button
from time import sleep

MY_POKE_POSITION = (55, 73)


class Actions:
    def __init__(self):
        pass

    def move(self, image_position):
        x, y = pyautogui.center(image_position)
        pyautogui.moveTo(x, y, 0.1)

    def move_to_and_click(self, image_position):
        self.move(image_position)
        pyautogui.click()

    def exec_hotkey(self, hotkey, delay=0.5):
        abra = True
        if isinstance(hotkey, list):
            for attack in hotkey:
                if abra is None:
                    return
                keyboard.press(button.key[attack["button"]], attack["delay"])
                abra = pyautogui.locateOnScreen('paras/abra.png', confidence=0.8)
        else:
            keyboard.press(button.key[hotkey], delay)

    def pokemon_movement(self, times):
        for _ in range(times):
            self.exec_hotkey("CAPS")
            sleep(0.5)

    def revive(self):
        current_position = pyautogui.position()
        pyautogui.moveTo(MY_POKE_POSITION)
        pyautogui.click()
        self.exec_hotkey('1')
        pyautogui.click()
        pyautogui.click()
        pyautogui.moveTo(current_position)

    def pokeball(self, pokemon):
        if pokemon is not None:
            x, y = pyautogui.center(pokemon)
            pyautogui.moveTo(x, y)
            self.exec_hotkey('5')
            sleep(0.1)
            

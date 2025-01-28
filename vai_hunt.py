import pyautogui
from pynput.keyboard import Listener
from pynput import keyboard
import threading
import json
from actions import Actions
from time import sleep

ATACK = [
    {"button": "TAB", "delay": 0.6},
    {"button": "F1", "delay": 0.6},
    {"button": "F2", "delay": 0.6},
    {"button": "F3", "delay": 0.6},
    {"button": "TAB", "delay": 0.6},
    {"button": "F4", "delay": 0.6},
    {"button": "F5", "delay": 0.6},
    {"button": "F6", "delay": 0.6},
    {"button": "F7", "delay": 0.6},
    {"button": "F8", "delay": 0.6},
    {"button": "F9", "delay": 0.6}
]

IS_POKEBALL = True

class Hunt:
    def __init__(self):
        self.isStarted = True
        with open('paras/paras.json', 'r') as file:
            infos = file.read()
        self.infos = json.loads(infos)
        self.actions = Actions()
        print(self.infos)
        pass

    def go_to_flag(self, item):
        for i in range(10):
            flag_position = pyautogui.locateOnScreen(item['path'], confidence=0.8)
            if flag_position is None:
                return
            self.actions.move_to_and_click(flag_position)
            sleep(item['wait'])

    def do_attack(self, time, item):
        for i in range(time):
            if pyautogui.locateOnScreen('paras/paras.png', confidence=0.8) is None:
                break
            pyautogui.moveTo(item["blink"][0], item["blink"][1], 0.2)
            self.actions.pokemon_movement(3)
            self.actions.exec_hotkey(ATACK)

    def coleta_itens(self, item):
        pyautogui.moveTo(item["blink"][0], item["blink"][1], 0.2)
        pyautogui.click()
        sleep(3)
        pyautogui.press('R')
     
        

    def start_route(self):
        while self.isStarted:
            for item in self.infos:
                self.go_to_flag(item)
                self.do_attack(4, item)
                sleep(1)
                self.coleta_itens(item)
                self.usa_pokeball()

    def usa_pokeball(self):
        if IS_POKEBALL and pyautogui.locateOnScreen('paras/pokeballs.png', confidence=0.8) is not None:
            for i in range(15):
                pokemon = pyautogui.locateOnScreen('paras/paras_death.png', confidence=0.8)
                self.actions.pokeball(pokemon)

    
    
                

    def target_key(self, key):
        print(key)
        if key == keyboard.Key.esc:
            return False
        if key == keyboard.Key.delete:
            threading.Thread(target=self.start_route).start()

    def start_keyboard(self):
        with Listener(on_press=self.target_key) as listener:
            listener.join()


hunt = Hunt()
hunt.start_keyboard()

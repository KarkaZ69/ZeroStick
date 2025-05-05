from m5stack import *
from m5ui import *
from uiflow import *
import machine
import time


lcd.clear()
setScreenColor(0x000000)


down_pin = machine.Pin(26, machine.Pin.IN, machine.Pin.PULL_UP) 
select_pin = machine.Pin(36, machine.Pin.IN, machine.Pin.PULL_UP)  
buttonA = machine.Pin(37, machine.Pin.IN, machine.Pin.PULL_UP)   


menu_items = ["WIFI", "BLE", "IR"]
current_selection = 0
y_positions = [30, 60, 90]


last_down_state = 1
last_select_state = 1
last_buttonA_state = 1

def draw_menu():
    lcd.clear()
    lcd.rect(5, y_positions[current_selection]-5, 230, 35, 0x00ff00)
    lcd.rect(6, y_positions[current_selection]-4, 228, 33, 0x00ff00)
    
    for i, item in enumerate(menu_items):
        color = 0xffffff if i == current_selection else 0x666666
        lcd.print(item, 30, y_positions[i], color)
    
    lcd.print("FZ:NO", 180, 5, 0x00ff00)

draw_menu()

while True:
    current_down = down_pin.value()
    current_select = select_pin.value()
    current_buttonA = buttonA.value()

    if current_down == 0 and last_down_state == 1:
        current_selection = (current_selection + 1) % len(menu_items)
        draw_menu()
        time.sleep_ms(100)
    
    if current_select == 0 and last_select_state == 1:
        time.sleep_ms(100)
    
    if current_buttonA == 0 and last_buttonA_state == 1:
        lcd.print("Rebooting...", 80, 60, 0xff0000)
        time.sleep_ms(1000)
        machine.reset()
    
    last_down_state = current_down
    last_select_state = current_select
    last_buttonA_state = current_buttonA
    
    time.sleep_ms(50)

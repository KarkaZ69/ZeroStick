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

MENU_MAIN = 0
MENU_WIFI = 1
MENU_BLE = 2
MENU_IR = 3
current_menu = MENU_MAIN

main_items = ["WIFI", "BLE", "IR"]
wifi_items = ["Scan", "Connect", "Back"]
ble_items = ["Scan", "Spam", "Back"]
ir_items = ["Send", "TVOFF", "Back"]
current_selection = 0
y_positions = [30, 60, 90]

COLOR_MAIN = 0x00ff00 
COLOR_WIFI = 0x0000ff 
COLOR_BLE = 0xff00ff   
COLOR_IR = 0xff8000    


last_down_state = 1
last_select_state = 1
last_buttonA_state = 1

def draw_main_menu():
    lcd.clear()

    lcd.rect(5, y_positions[current_selection]-5, 230, 35, COLOR_MAIN)
    lcd.rect(6, y_positions[current_selection]-4, 228, 33, COLOR_MAIN)
    

    for i, item in enumerate(main_items):
        color = 0xffffff if i == current_selection else 0x666666
        lcd.print(item, 30, y_positions[i], color)
    

    lcd.print("FZ:OK", 180, 5, COLOR_MAIN)

def draw_wifi_menu():
    lcd.clear()

    lcd.rect(5, y_positions[current_selection]-5, 230, 35, COLOR_WIFI)
    lcd.rect(6, y_positions[current_selection]-4, 228, 33, COLOR_WIFI)
    

    for i, item in enumerate(wifi_items):
        color = 0xffffff if i == current_selection else 0x666666
        lcd.print(item, 30, y_positions[i], color)
    

    lcd.print("WiFi", 10, 5, COLOR_WIFI)

def draw_ble_menu():
    lcd.clear()

    lcd.rect(5, y_positions[current_selection]-5, 230, 35, COLOR_BLE)
    lcd.rect(6, y_positions[current_selection]-4, 228, 33, COLOR_BLE)
    

    for i, item in enumerate(ble_items):
        color = 0xffffff if i == current_selection else 0x666666
        lcd.print(item, 30, y_positions[i], color)
    

    lcd.print("BLE", 10, 5, COLOR_BLE)

def draw_ir_menu():
    lcd.clear()

    lcd.rect(5, y_positions[current_selection]-5, 230, 35, COLOR_IR)
    lcd.rect(6, y_positions[current_selection]-4, 228, 33, COLOR_IR)
    

    for i, item in enumerate(ir_items):
        color = 0xffffff if i == current_selection else 0x666666
        lcd.print(item, 30, y_positions[i], color)
    

    lcd.print("IR", 10, 5, COLOR_IR)


draw_main_menu()

while True:
    current_down = down_pin.value()
    current_select = select_pin.value()
    current_buttonA = buttonA.value()


    if current_down == 0 and last_down_state == 1:
        if current_menu == MENU_MAIN:
            current_selection = (current_selection + 1) % len(main_items)
            draw_main_menu()
        elif current_menu == MENU_WIFI:
            current_selection = (current_selection + 1) % len(wifi_items)
            draw_wifi_menu()
        elif current_menu == MENU_BLE:
            current_selection = (current_selection + 1) % len(ble_items)
            draw_ble_menu()
        elif current_menu == MENU_IR:
            current_selection = (current_selection + 1) % len(ir_items)
            draw_ir_menu()
        time.sleep_ms(200)
    

    if current_select == 0 and last_select_state == 1:
        if current_menu == MENU_MAIN:
            if main_items[current_selection] == "WIFI":
                current_menu = MENU_WIFI
                current_selection = 0
                draw_wifi_menu()
            elif main_items[current_selection] == "BLE":
                current_menu = MENU_BLE
                current_selection = 0
                draw_ble_menu()
            elif main_items[current_selection] == "IR":
                current_menu = MENU_IR
                current_selection = 0
                draw_ir_menu()
        
        elif current_menu == MENU_WIFI:
            if wifi_items[current_selection] == "Back":
                current_menu = MENU_MAIN
                current_selection = 0
                draw_main_menu()
            elif wifi_items[current_selection] == "Scan":
                lcd.print("Scanning WiFi...", 60, 100, 0xffff00)
                time.sleep_ms(1000)
                draw_wifi_menu()
            elif wifi_items[current_selection] == "Connect":
                lcd.print("Connecting...", 80, 100, 0xffff00)
                time.sleep_ms(1000)
                draw_wifi_menu()
        
        elif current_menu == MENU_BLE:
            if ble_items[current_selection] == "Back":
                current_menu = MENU_MAIN
                current_selection = 0
                draw_main_menu()
            elif ble_items[current_selection] == "Scan":
                lcd.print("Scanning BLE...", 70, 100, 0xffff00)
                time.sleep_ms(1000)
                draw_ble_menu()
            elif ble_items[current_selection] == "Spam":
                lcd.print("BLE Spamming...", 70, 100, 0xffff00)
                time.sleep_ms(1000)
                draw_ble_menu()
        
        elif current_menu == MENU_IR:
            if ir_items[current_selection] == "Back":
                current_menu = MENU_MAIN
                current_selection = 0
                draw_main_menu()
            elif ir_items[current_selection] == "Send":
                lcd.print("Sending IR...", 80, 100, 0xffff00)
                time.sleep_ms(1000)
                draw_ir_menu()
            elif ir_items[current_selection] == "TVBGONE":
                lcd.print("TV-B-GONE Active!", 50, 100, 0xffff00)
                time.sleep_ms(1000)
                draw_ir_menu()
        
        time.sleep_ms(200)
    

    if current_buttonA == 0 and last_buttonA_state == 1:
        lcd.print("Rebooting...", 80, 60, 0xff0000)
        time.sleep_ms(1000)
        machine.reset()
    

    last_down_state = current_down
    last_select_state = current_select
    last_buttonA_state = current_buttonA
    
    time.sleep_ms(50)

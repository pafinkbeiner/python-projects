import pyautogui
import time 

width = pyautogui.size()[0]
height = pyautogui.size()[1]

print("Determined Screen Size: Widht: "+str(width)+", Height: "+str(height))

# Move Mouse Curser to absolute position 
#editor
pyautogui.moveTo(100, 100, duration=2)

time.sleep(1)

# Move Mouse Curser to relativ position 
#pyautogui.moveRel(0, 50, duration = 1) 

print("Current Mouse Position: ")
print(pyautogui.position()) 

# Execute Mouse click
#pyautogui.click(100, 100) 

# Mouse dragging
pyautogui.dragRel(100, 100, duration = 1) 

# Scroll
#pyautogui.scroll(200)

# Write in keyboard
#pyautogui.click(1200, 600) 
#pyautogui.typewrite(["a", "left", "ctrlleft"]) 
#pyautogui.typewrite("hello Geeks !") 

pyautogui.hotkey("winleft")
time.sleep(0.25)
pyautogui.typewrite("editor")
time.sleep(0.25)
pyautogui.hotkey("return")
time.sleep(0.25)
pyautogui.hotkey("winleft", "up") 
time.sleep(0.25)
pyautogui.moveTo((width/2), (height/2), duration=0.25)

pyautogui.typewrite("Hello There General Kenobi! \nI´m now controlling your computer! :D", 0.02)


pyautogui.hotkey("alt", "f4")
time.sleep(0.25)
pyautogui.hotkey("right")
time.sleep(0.25)
pyautogui.hotkey("return")
time.sleep(0.25)

#pyautogui.alert(text='', title='', button='OK')
#pyautogui.confirm(text='', title='', buttons=['OK', 'Cancel'])
#pyautogui.prompt(text='', title='' , default='')
#pyautogui.password(text='', title='', default='', mask='*')

# Key Names
pyautogui.KEY_NAMES

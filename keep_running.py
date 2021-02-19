import pyautogui as pg
import time

coord = (-1200, 500)
scroll_dif = 10

while True:
    pg.moveTo(coord)
    pg.scroll(scroll_dif)
    pg.scroll(-1*scroll_dif)
    time.sleep(600)

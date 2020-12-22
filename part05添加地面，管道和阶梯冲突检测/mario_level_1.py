import sys
from data import tools
import pygame as pg
if __name__ == '__main__':
    control = tools.Control()
    control.main()
    pg.quit()
    sys.exit()
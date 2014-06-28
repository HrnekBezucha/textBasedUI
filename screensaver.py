#!/usr/bin/python3
'''
Oldschool styled screensaver.
Press any key to interupt.
'''

import curses, time

scr = curses.initscr()
scr.nodelay(1)
dims = scr.getmaxyx()
x, y, = 0, 0
Vertical = 1
Horizontal = 1
q = -1
curses.curs_set(0)
timeStr = time.strftime('%c')

while q < 0:
  scr.clear()
  scr.addstr(y, x, timeStr)
  scr.refresh()
  y += Vertical
  x += Horizontal

  if y == dims[0] - 1:
    Vertical = -1
  elif y == 0:
    Vertical = 1

  if x == dims[1] - len(timeStr)-1:
    Horizontal = -1
  elif x == 0:
    Horizontal = 1

  q = scr.getch()
  time.sleep(0.3)


curses.curs_set(1)
curses.endwin()

#!/usr/bin/python

import colorize


for fgc in colorize.FG_COLORS:
    print ( colorize.fg(fgc, fgc) )

for bgc in colorize.BG_COLORS:
    print ( colorize.bg(bgc, bgc) )

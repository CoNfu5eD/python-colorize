#!/usr/bin/python

# char for reset terminal/cmd colors default
C_ENDC = '\033[0m'

# chars for setting foreground colors to colors named in the arrays keys
FG_COLORS = {
    'red': '\033[31m',
    'green': '\033[32m',
    'yellow': '\033[33m',
    'blue': '\033[34m',
    'purple': '\033[35m',
    'cyan': '\033[36m',
    'white': '\033[37m',
    'lightgrey': '\033[38m',
    'pink': '\033[95m',
    'lightblue': '\033[94m',
    'lightcyan': '\033[96m',
    'lightgreen': '\033[92m',
    'lightyellow': '\033[93m',
    'lightred': '\033[91m',
    'grey': '\033[90m'
}

# chars for setting background colors to colors named in the arrays keys
BG_COLORS = {
    'red': '\033[41m',
    'green': '\033[42m',
    'yellow': '\033[43m',
    'blue': '\033[44m',
    'purple': '\033[45m',
    'cyan': '\033[46m'
}

            

# colorize `string` with foreground `color` and return it
def fg(string, color):
    return FG_COLORS[color] + string + C_ENDC;

# colorize `string` with background `color` and return it
def bg(string, color):
    return BG_COLORS[color] + string + C_ENDC;


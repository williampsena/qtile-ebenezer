import os


def restart_qtile():
    os.system("qtile cmd-obj -o cmd -f restart")

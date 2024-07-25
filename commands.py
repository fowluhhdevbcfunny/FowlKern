from utils import *

def ver(lines):
    printf(lines, "FowlKern v1.0.0", 2)

def neofetch(lines):
    printf(lines, "  FFFFFFFFFF KKK    KKK    FowlKern v1.0.0", 0, 1)
    printf(lines, "  FFFFFFFFFF KKK   KKK ")
    printf(lines, "  FFF        KKK  KKK      Made by FowluhhDev.")
    printf(lines, "  FFFFFFF    KKKKKKK   ")
    printf(lines, "  FFF        KKK  KKK  ")
    printf(lines, "  FFF        KKK   KKK ")
    printf(lines, "  FFF        KKK    KKK", 2)

def help(lines):
    printf(lines, "COMMAND HELP --------------------------")
    printf(lines, "VER:                Prints the version.")
    printf(lines, "CLEAR:               Clears the screen.")
    printf(lines, "ECHO:           Repeats the text given.")
    printf(lines, "NEOFETCH:  Gives info about the system.")
    printf(lines, "HELP:              Prints this message.", 2)
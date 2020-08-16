import os
import sys

PRINT_ENABLED = True
OBJECTS_COUNTER = 0

class Console:
    
    @staticmethod
    def inline(_str, _enabled=True):
        if PRINT_ENABLED and _enabled:
            sys.stdout.write("\r" + _str)
            sys.stdout.flush()
    
    @staticmethod
    def reset_counter(_to = 0):
        global OBJECTS_COUNTER
        OBJECTS_COUNTER = _to
            
    @staticmethod
    def inline_counter(_str="", _enabled=True):
        if PRINT_ENABLED and _enabled:
            global OBJECTS_COUNTER
            sys.stdout.write("\r" + _str + " Objects: " + str(OBJECTS_COUNTER))
            sys.stdout.flush()
            OBJECTS_COUNTER = OBJECTS_COUNTER + 1

    @staticmethod
    def line(_str=""):
        if PRINT_ENABLED:
            sys.stdout.write(_str + "\n")

    @staticmethod
    def enable():
        global PRINT_ENABLED
        PRINT_ENABLED = True

    @staticmethod
    def disable():
        global PRINT_ENABLED
        PRINT_ENABLED = False

    @staticmethod
    def newline():
        if PRINT_ENABLED:
            sys.stdout.write("\n")


#! /usr/bin/env python3
"""
define, raise, handle exception
"""

class Error(Exception):
    pass

class InputError(Error):
    def __init__(self, message):
        self.code="InputCode"
        self.message=message

class TimeError(Error):
    def __init__(self, message):
        self.code="TimeCode"
        self.message=message

import sys
def Handle(value):
    try:
        if value=="input":
            raise InputError("Your input is invalid.")
        elif value == "timeout":
            raise TimeError("Time!")
        elif value == "io":
            raise IOError()
        elif value == "other":
            x=int('a') #ValueError
        else:
            print("Would not throw error.")
    except TimeError as err:
        print("Time error happened:{}, {}!".format(err.code,err.message))
    except InputError as err:
        print("Input error happened:{}, {}!".format(err.code, err.message))
    except (IOError,RuntimeError):
        print("Pass the error.")
        pass
    except:
        print("Unknown error.")
    else:
        print("Working.")
    finally:
        print("always have this line")

Handle("input")
Handle("timeout")
Handle("io")
Handle("other")
Handle("working")

#for loop and with open(path, mode) as file automatically have finally block


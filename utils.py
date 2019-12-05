import time
import sys

def wait(seconds):
    time.sleep(0.1)

def get_input(prompt,input_test):
    if input_test is None:
        if sys.hexversion > 0x03000000:
            return input(prompt)
        else:
            return raw_input(prompt)
    else:
        return input_test



# -*- coding: utf-8 -*-

import time

cars = ["|", "/", "-", "\\", "|", "/", "-"]

while True:
    for i in cars:
        print ("\b", i, end="\r")
        time.sleep(0.01)

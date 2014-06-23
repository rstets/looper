# coding=utf-8
import logging
import sys
import time

logger = logging.getLogger()
logger.addHandler(logging.StreamHandler(sys.stdout))
logger.setLevel(logging.DEBUG)

from gamepad import Gamepad
from consts import *

gamepads = [Gamepad(SPEEDLINK_ALT)]

while True:
    for g in gamepads:
        g.query()
        time.sleep(0.0002)

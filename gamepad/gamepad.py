# coding=utf-8
import hid
from midi import MIDI
from consts import *

import logging

logger = logging.getLogger()


class Gamepad:
    def __init__(self, config):
        self.id = config['id']
        self.vid = config['vid']
        self.pid = config['pid']
        self.channel = config['channel']
        self.midi = MIDI(self.channel)
        self.hid = None
        self.value = []
        self.active = False
        self.settings = config['message']

        if hid.enumerate(self.vid, self.pid):
            h = hid.device(self.vid, self.pid)
            h.set_nonblocking(1)
            self.hid = h
            self.active = True
            logger.debug("Device found: {i}".format(i=self.id))


    def query(self):
        if not self.active:
            return

        # try:
        if True:
            value = self.hid.read(16)
            if value and value != self.value:
                if self.settings:
                    for m, msg in enumerate(self.settings):
                        if msg:
                            data = value[m]

                            if 'buttons' in msg:
                                self.handle_button(msg, data)
                            else:
                                if msg['type'] == CC:
                                    self.send_cc(msg, data)
                                elif msg['type'] == CC_DELTA:
                                    self.send_cc_delta(msg, data)
                self.value = value
        # except Exception, ex:
        #     print ex
        #     self.hid.close()
        #     self.active = False

    def send_cc(self, msg, data):
        if msg['inverse']:
            data = (255 - data) / 2
        else:
            data /= 2
        self.midi.cc(msg['number'], data)

    def send_note(self, btn, data):
        if btn['note'] is not None:
            if self.is_on(btn, data):
                self.midi.note_on(btn['note'])
            else:
                self.midi.note_off(btn['note'])

    def send_cc_delta_button(self, btn, data):
        if btn['cc'] is not None:
            if self.is_on(btn, data):
                self.midi.cc_delta(btn['cc'], btn['delta'])

    def send_cc_delta(self, msg, data):
        if msg['inverse']:
            data = (255 - data) / 2
        else:
            data /= 2
        self.midi.cc_delta(msg['number'], data)

    def handle_button(self, msg, data):
        for btn in msg['buttons']:
            if 'type' in btn:
                if btn['type'] == CC_DELTA_BUTTONS:
                    self.send_cc_delta_button(btn, data)
                elif btn['type'] == NOTE:
                    self.send_note(btn, data)

    def is_on(self, btn, data):
        if 'number' in btn.keys():
            return btn['number'] == data
        elif 'value' in btn.keys():
            return data & btn['value'] == btn['value']

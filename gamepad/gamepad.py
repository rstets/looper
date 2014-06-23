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

        try:
            value = self.hid.read(16)
            if value and value != self.value:
                if self.settings:
                    for m, msg in enumerate(self.settings):
                        if msg:
                            data = value[m]

                            if msg['type'] == CC:
                                self.send_cc(msg, data)
                            elif msg['type'] == CC_DELTA:
                                self.send_cc_delta(msg, data)
                            elif msg['type'] == CC_DELTA_BUTTONS and msg['buttons']:
                                self.send_cc_delta_button(msg, data)
                            elif msg['type'] == NOTE and msg['buttons']:
                                self.send_note(msg, data)
                self.value = value
        except Exception, ex:
            print ex
            self.hid.close()
            self.active = False

    def send_cc(self, msg, data):
        if msg['inverse']:
            data = (255 - data) / 2
        else:
            data /= 2
        self.midi.cc(msg['number'], data)

    def send_note(self, msg, data):
        for btn in msg['buttons']:
            if btn['note'] is not None:
                if 'number' in btn.keys():
                    if btn['number'] == data:
                        self.midi.note_on(btn['note'])
                    else:
                        self.midi.note_off(btn['note'])
                elif 'value' in btn.keys():
                    if data & btn['value'] == btn['value']:
                        self.midi.note_on(btn['note'])
                    else:
                        self.midi.note_off(btn['note'])

    def send_cc_delta_button(self, msg, data):
        for btn in msg['buttons']:
            if btn['cc'] is not None:
                if 'value' in btn.keys():
                    if data & btn['value'] == btn['value']:
                        self.midi.cc_delta(btn['cc'], btn['delta'])
                if 'number' in btn.keys():
                    if btn['number'] == data:
                        self.midi.cc_delta(btn['cc'], btn['delta'])

    def send_cc_delta(self, msg, data):
        if msg['inverse']:
            data = (255 - data) / 2
        else:
            data /= 2
        self.midi.cc_delta(msg['number'], data)

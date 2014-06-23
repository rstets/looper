# coding=utf-8
import rtmidi2
import logging
logger = logging.getLogger()

class MIDI:
    THRESHOLD = 5
    THRESHOLD_CC_DELTA = 2

    def __init__(self, channel):
        self.midi_out = rtmidi2.MidiOut()
        self.midi_out.open_port(0)
        self.channel = channel
        self.messages = {}
        self.notes = {}

    def cc(self, cc, value):
        if cc not in self.messages:
            self.messages[cc] = 0

        delta = abs(self.messages[cc] - value)
        if delta < self.THRESHOLD:
            return

        logger.debug(("MIDI CC:", self.channel, cc, value,))
        self.midi_out.send_cc(self.channel - 1, cc, value)
        self.messages[cc] = value


    def cc_delta(self, cc, value):
        if cc not in self.messages:
            self.messages[cc] = 0

        delta = (value - 64) / 16
        new_cc_value = int(self.messages[cc] + delta)

        cc_delta = abs(new_cc_value - self.messages[cc])
        if cc_delta < self.THRESHOLD_CC_DELTA:
            return

        if new_cc_value < 0:
            new_cc_value = 0
        if new_cc_value > 127:
            new_cc_value = 127

        logger.debug(("MIDI CC:", self.channel, cc, new_cc_value,))
        self.midi_out.send_cc(self.channel - 1, cc, new_cc_value)
        self.messages[cc] = new_cc_value


    def note_on(self, note):
        if note in self.notes and self.notes[note] == True:
            return

        logger.debug(("MIDI NOTE ON:", self.channel, note,))
        self.midi_out.send_noteon(self.channel - 1, note, 127)
        self.notes[note] = True


    def note_off(self, note):
        if note in self.notes and self.notes[note] == False:
            return

        logger.debug(("MIDI NOTE OFF:", self.channel, note,))
        self.midi_out.send_noteoff(self.channel - 1, note)
        self.notes[note] = False

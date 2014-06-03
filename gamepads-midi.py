# coding=utf-8
import hid
import rtmidi2

midi_out = rtmidi2.MidiOut()

# open the first available port
midi_out.open_port(0)

LEFT_X = 'LEFT_X'
LEFT_Y = 'LEFT_Y'
RIGHT_X = 'RIGHT_X'
RIGHT_Y = 'RIGHT_Y'
BUTTONS_1 = 'BUTTONS_1'
BUTTONS_2 = 'BUTTONS_2'
CC = 'CC'
NOTE = 'NOTE'
MIDI_CHANNEL_1 = 5
MIDI_CHANNEL_2 = 6

notes = {MIDI_CHANNEL_1: {}, MIDI_CHANNEL_2: {}}

MIDI_NOTES = []
for note in xrange(32, 64):
    MIDI_NOTES.append(note)
    notes[MIDI_CHANNEL_1][note] = False
    notes[MIDI_CHANNEL_2][note] = False

MIDI_MESSAGES = [55, 56, 57, 58, ]
messages = {MIDI_CHANNEL_1: {}, MIDI_CHANNEL_2: {}}
for cc in MIDI_MESSAGES:
    messages[MIDI_CHANNEL_1][cc] = 0
    messages[MIDI_CHANNEL_2][cc] = 0

THRESHOLD = 5

# My Gamepads
GAMEPADS = [
    {
        'id': 'Logitech',
        'vid': 1133,
        'pid': 49689,
        'channel': MIDI_CHANNEL_2,
        'message': [
            None,
            {'name': LEFT_X, 'type': CC, 'number': MIDI_MESSAGES[0],
             'inverse': False},
            {'name': LEFT_Y, 'type': CC, 'number': MIDI_MESSAGES[1],
             'inverse': True},
            {'name': RIGHT_X, 'type': CC, 'number': MIDI_MESSAGES[2],
             'inverse': False},
            {'name': RIGHT_Y, 'type': CC, 'number': MIDI_MESSAGES[3],
             'inverse': True},
            {'name': BUTTONS_1, 'type': NOTE, 'buttons': [
                {'note': MIDI_NOTES[12], 'name': 'ARROW (TOP)', 'number': 0},
                {'note': None, 'name': 'ARROW (TOP-RIGHT)', 'number': 1},
                {'note': MIDI_NOTES[13], 'name': 'ARROW (RIGHT)', 'number': 2},
                {'note': None, 'name': 'ARROW (BOTTOM-RIGHT)', 'number': 3},
                {'note': MIDI_NOTES[14], 'name': 'ARROW (BOTTOM)',
                 'number': 4},
                {'note': None, 'name': 'ARROW (BOTTOM-LEFT)', 'number': 5},
                {'note': MIDI_NOTES[15], 'name': 'ARROW (LEFT)', 'number': 6},
                {'note': None, 'name': 'ARROW (TOP-LEFT)', 'number': 7},

                {'note': MIDI_NOTES[8], 'name': 'BTN Y (TOP)', 'value': 136},
                {'note': MIDI_NOTES[9], 'name': 'BTN B (RIGHT)', 'value': 72},
                {'note': MIDI_NOTES[10], 'name': 'BTN A (BOTTOM)',
                 'value': 40},
                {'note': MIDI_NOTES[11], 'name': 'BTN X (LEFT)', 'value': 24},
            ]},
            {'name': BUTTONS_2, 'type': NOTE, 'buttons': [
                {'note': MIDI_NOTES[0], 'name': 'LEFT TOP SHIFT', 'value': 1},
                {'note': MIDI_NOTES[1], 'name': 'LEFT BOTTOM SHIFT',
                 'value': 4},
                {'note': MIDI_NOTES[2], 'name': 'RIGHT TOP SHIFT', 'value': 2},
                {'note': MIDI_NOTES[3], 'name': 'RIGHT BOTTOM SHIFT',
                 'value': 8},
                {'note': MIDI_NOTES[4], 'name': 'BACK', 'value': 16},
                {'note': MIDI_NOTES[5], 'name': 'START', 'value': 32},
                {'note': MIDI_NOTES[6], 'name': 'LEFT STICK', 'value': 64},
                {'note': MIDI_NOTES[7], 'name': 'RIGHT STICK', 'value': 128},
            ]},
            None, # Off: 84, Mode: 92, Vibro: 116, Mode+Vibro: 124
        ],
    },
    {
        'id': 'SpeedLink',
        'vid': 121,
        'pid': 6,
        'channel': MIDI_CHANNEL_1,
        'message': [
            {'name': LEFT_X, 'type': CC, 'number': MIDI_MESSAGES[0],
             'inverse': False},
            {'name': LEFT_Y, 'type': CC, 'number': MIDI_MESSAGES[1],
             'inverse': True},
            None,
            {'name': RIGHT_X, 'type': CC, 'number': MIDI_MESSAGES[2],
             'inverse': False},
            {'name': RIGHT_Y, 'type': CC, 'number': MIDI_MESSAGES[3],
             'inverse': True},
            {'name': BUTTONS_1, 'type': NOTE, 'buttons': [
                {'note': MIDI_NOTES[12], 'name': 'ARROW (TOP)', 'number': 0},
                {'note': None, 'name': 'ARROW (TOP-RIGHT)', 'number': 1},
                {'note': MIDI_NOTES[13], 'name': 'ARROW (RIGHT)', 'number': 2},
                {'note': None, 'name': 'ARROW (BOTTOM-RIGHT)', 'number': 3},
                {'note': MIDI_NOTES[14], 'name': 'ARROW (BOTTOM)',
                 'number': 4},
                {'note': None, 'name': 'ARROW (BOTTOM-LEFT)', 'number': 5},
                {'note': MIDI_NOTES[15], 'name': 'ARROW (LEFT)', 'number': 6},
                {'note': None, 'name': 'ARROW (TOP-LEFT)', 'number': 7},

                {'note': MIDI_NOTES[8], 'name': 'BTN 1 (TOP)', 'value': 31},
                {'note': MIDI_NOTES[9], 'name': 'BTN 2 (RIGHT)', 'value': 47},
                {'note': MIDI_NOTES[10], 'name': 'BTN 3 (BOTTOM)',
                 'value': 79},
                {'note': MIDI_NOTES[11], 'name': 'BTN 4 (LEFT)', 'value': 143},
            ]},
            {'name': BUTTONS_2, 'type': NOTE, 'buttons': [
                {'note': MIDI_NOTES[0], 'name': 'LEFT TOP SHIFT', 'value': 1},
                {'note': MIDI_NOTES[1], 'name': 'LEFT BOTTOM SHIFT',
                 'value': 4},
                {'note': MIDI_NOTES[2], 'name': 'RIGHT TOP SHIFT', 'value': 2},
                {'note': MIDI_NOTES[3], 'name': 'RIGHT BOTTOM SHIFT',
                 'value': 8},
                {'note': MIDI_NOTES[4], 'name': 'SELECT', 'value': 16},
                {'note': MIDI_NOTES[5], 'name': 'START', 'value': 32},
                {'note': MIDI_NOTES[6], 'name': 'LEFT STICK', 'value': 64},
                {'note': MIDI_NOTES[7], 'name': 'RIGHT STICK', 'value': 128},
            ]},
            None,
        ],
    },
]

devices = []

for g in GAMEPADS:
    if hid.enumerate(g['vid'], g['pid']):
        h = hid.device(g['vid'], g['pid'])
        h.set_nonblocking(1)
        dev = {
            'info': g,
            'hid': h,
            'value': [],
        }
        devices.append(dev)
        print "Device found: {i}".format(i=g['id'])


def midi_cc(channel, cc, value):
    delta = abs(messages[channel][cc] - value)
    if delta < THRESHOLD:
        return

    print "MIDI CC:", channel, cc, value
    midi_out.send_cc(channel - 1, cc, value)
    messages[channel][cc] = value


def midi_note_on(channel, note):
    if notes[channel][note]:
        return

    print "MIDI NOTE ON:", channel, note
    midi_out.send_noteon(channel - 1, note, 127)
    notes[channel][note] = True


def midi_note_off(channel, note):
    if not notes[channel][note]:
        return

    print "MIDI NOTE OFF:", channel, note
    midi_out.send_noteoff(channel - 1, note)
    notes[channel][note] = False


while True:
    for i, dev in enumerate(devices):
        try:
            hid = dev['hid']
            info = dev['info']
            value = hid.read(16)
            if value and value != dev['value']:
                if info['message']:
                    for m, msg in enumerate(info['message']):
                        if msg:
                            data = value[m]

                            if msg['type'] == CC:
                                if msg['inverse']:
                                    data = (255 - data) / 2
                                else:
                                    data /= 2
                                midi_cc(info['channel'], msg['number'], data)
                            elif msg['type'] == NOTE and msg['buttons']:
                                for btn in msg['buttons']:
                                    if btn['note']:
                                        if 'number' in btn.keys():
                                            if btn['number'] == data:
                                                midi_note_on(info['channel'],
                                                             btn['note'])
                                            else:
                                                midi_note_off(info['channel'],
                                                              btn['note'])
                                        elif 'value' in btn.keys():
                                            if data & btn['value'] == btn[
                                                'value']:
                                                midi_note_on(info['channel'],
                                                             btn['note'])
                                            else:
                                                midi_note_off(info['channel'],
                                                              btn['note'])
                dev['value'] = value
        except Exception, ex:
            print ex
            hid.close()
            del devices[i]

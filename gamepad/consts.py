# coding=utf-8
LEFT_X = 'LEFT_X'
LEFT_Y = 'LEFT_Y'
RIGHT_X = 'RIGHT_X'
RIGHT_Y = 'RIGHT_Y'
BUTTONS_1 = 'BUTTONS_1'
BUTTONS_2 = 'BUTTONS_2'
CC = 'CC'
CC_DELTA = 'CC_DELTA'
CC_DELTA_BUTTONS = 'CC_DELTA_BUTTONS'
NOTE = 'NOTE'


LOGITECH = {
        'id': 'Logitech',
        'vid': 1133,
        'pid': 49689,
        'channel': 2,
        'message': [
            None,
            {'name': LEFT_X, 'type': CC, 'number': 55,
             'inverse': False},
            {'name': LEFT_Y, 'type': CC, 'number': 56,
             'inverse': True},
            {'name': RIGHT_X, 'type': CC, 'number': 57,
             'inverse': False},
            {'name': RIGHT_Y, 'type': CC, 'number': 58,
             'inverse': True},
            {'name': BUTTONS_1, 'type': NOTE, 'buttons': [
                {'note': 12, 'name': 'ARROW (TOP)', 'number': 0},
                {'note': None, 'name': 'ARROW (TOP-RIGHT)', 'number': 1},
                {'note': 13, 'name': 'ARROW (RIGHT)', 'number': 2},
                {'note': None, 'name': 'ARROW (BOTTOM-RIGHT)', 'number': 3},
                {'note': 14, 'name': 'ARROW (BOTTOM)',
                 'number': 4},
                {'note': None, 'name': 'ARROW (BOTTOM-LEFT)', 'number': 5},
                {'note': 15, 'name': 'ARROW (LEFT)', 'number': 6},
                {'note': None, 'name': 'ARROW (TOP-LEFT)', 'number': 7},

                {'note': 8, 'name': 'BTN Y (TOP)', 'value': 136},
                {'note': 9, 'name': 'BTN B (RIGHT)', 'value': 72},
                {'note': 10, 'name': 'BTN A (BOTTOM)',
                 'value': 40},
                {'note': 11, 'name': 'BTN X (LEFT)', 'value': 24},
            ]},
            {'name': BUTTONS_2, 'type': NOTE, 'buttons': [
                {'note': 0, 'name': 'LEFT TOP SHIFT', 'value': 1},
                {'note': 1, 'name': 'LEFT BOTTOM SHIFT',
                 'value': 4},
                {'note': 2, 'name': 'RIGHT TOP SHIFT', 'value': 2},
                {'note': 3, 'name': 'RIGHT BOTTOM SHIFT',
                 'value': 8},
                {'note': 4, 'name': 'BACK', 'value': 16},
                {'note': 5, 'name': 'START', 'value': 32},
                {'note': 6, 'name': 'LEFT STICK', 'value': 64},
                {'note': 7, 'name': 'RIGHT STICK', 'value': 128},
            ]},
            None, # Off: 84, Mode: 92, Vibro: 116, Mode+Vibro: 124
        ],
    }


SPEEDLINK = {
        'id': 'SpeedLink',
        'vid': 121,
        'pid': 6,
        'channel': 3,
        'message': [
            {'name': LEFT_X, 'type': CC, 'number': 55,
             'inverse': False},
            {'name': LEFT_Y, 'type': CC, 'number': 56,
             'inverse': True},
            None,
            {'name': RIGHT_X, 'type': CC, 'number': 57,
             'inverse': False},
            {'name': RIGHT_Y, 'type': CC, 'number': 58,
             'inverse': True},
            {'name': BUTTONS_1, 'type': NOTE, 'buttons': [
                {'note': 12, 'name': 'ARROW (TOP)', 'number': 0},
                {'note': None, 'name': 'ARROW (TOP-RIGHT)', 'number': 1},
                {'note': 13, 'name': 'ARROW (RIGHT)', 'number': 2},
                {'note': None, 'name': 'ARROW (BOTTOM-RIGHT)', 'number': 3},
                {'note': 14, 'name': 'ARROW (BOTTOM)',
                 'number': 4},
                {'note': None, 'name': 'ARROW (BOTTOM-LEFT)', 'number': 5},
                {'note': 15, 'name': 'ARROW (LEFT)', 'number': 6},
                {'note': None, 'name': 'ARROW (TOP-LEFT)', 'number': 7},

                {'note': 8, 'name': 'BTN 1 (TOP)', 'value': 31},
                {'note': 9, 'name': 'BTN 2 (RIGHT)', 'value': 47},
                {'note': 10, 'name': 'BTN 3 (BOTTOM)',
                 'value': 79},
                {'note': 11, 'name': 'BTN 4 (LEFT)', 'value': 143},
            ]},
            {'name': BUTTONS_2, 'type': NOTE, 'buttons': [
                {'note': 0, 'name': 'LEFT TOP SHIFT', 'value': 1},
                {'note': 1, 'name': 'LEFT BOTTOM SHIFT',
                 'value': 4},
                {'note': 2, 'name': 'RIGHT TOP SHIFT', 'value': 2},
                {'note': 3, 'name': 'RIGHT BOTTOM SHIFT',
                 'value': 8},
                {'note': 4, 'name': 'SELECT', 'value': 16},
                {'note': 5, 'name': 'START', 'value': 32},
                {'note': 6, 'name': 'LEFT STICK', 'value': 64},
                {'note': 7, 'name': 'RIGHT STICK', 'value': 128},
            ]},
            None,
        ],
    }

SPEEDLINK_ALT = {
        'id': 'SpeedLink',
        'vid': 121,
        'pid': 6,
        'channel': 3,
        'message': [
            {'name': LEFT_X, 'type': CC_DELTA, 'number': 55, 'inverse': False},
            {'name': LEFT_Y, 'type': CC_DELTA, 'number': 56, 'inverse': True},
            None,
            {'name': RIGHT_X, 'type': CC_DELTA, 'number': 57, 'inverse': False},
            {'name': RIGHT_Y, 'type': CC_DELTA, 'number': 58, 'inverse': True},
            {'name': BUTTONS_1, 'type': CC_DELTA_BUTTONS, 'buttons': [
                {'cc': None, 'name': 'ARROW (TOP-RIGHT)', 'number': 1},
                {'cc': None, 'name': 'ARROW (BOTTOM-RIGHT)', 'number': 3},
                {'cc': None, 'name': 'ARROW (BOTTOM-LEFT)', 'number': 5},
                {'cc': None, 'name': 'ARROW (TOP-LEFT)', 'number': 7},

                {'cc': 63, 'delta': 0, 'name': 'ARROW (BOTTOM)', 'number': 4},
                {'cc': 63, 'delta': 127, 'name': 'ARROW (TOP)', 'number': 0},
                {'cc': 64, 'delta': 0, 'name': 'ARROW (LEFT)', 'number': 6},
                {'cc': 64, 'delta': 127, 'name': 'ARROW (RIGHT)', 'number': 2},

                {'cc': 65, 'delta': 0, 'name': 'BTN 3 (BOTTOM)', 'value': 79},
                {'cc': 65, 'delta': 127, 'name': 'BTN 1 (TOP)', 'value': 31},
                {'cc': 66, 'delta': 0, 'name': 'BTN 4 (LEFT)', 'value': 143},
                {'cc': 66, 'delta': 127, 'name': 'BTN 2 (RIGHT)', 'value': 47},

                {'cc': 61, 'delta': 0, 'name': 'SELECT', 'value': 16},
                {'cc': 61, 'delta': 127, 'name': 'START', 'value': 32},
                {'cc': 62, 'delta': 0, 'name': 'LEFT STICK', 'value': 64},
                {'cc': 62, 'delta': 127, 'name': 'RIGHT STICK', 'value': 128},
            ]},
            {'name': BUTTONS_2, 'type': NOTE, 'buttons': [
                {'note': 0, 'name': 'LEFT TOP SHIFT', 'value': 1},
                {'note': 1, 'name': 'LEFT BOTTOM SHIFT', 'value': 4},
                {'note': 2, 'name': 'RIGHT TOP SHIFT', 'value': 2},
                {'note': 3, 'name': 'RIGHT BOTTOM SHIFT', 'value': 8},
            ]},
            None,
        ],
    }

# Copyright Dusan Nikolov, 2015 -

import time
import datetime
import subprocess
from ConfigParser import SafeConfigParser
from win32gui import FindWindow
from win32api import PostMessage

# import logging

# Configuration sections
GENERAL = 'GENERAL'

# Constants for Windows message interface
WM_COMMAND = 0x111
WM_USER = 0x400

# WM_COMMAND Messages
# wparam values 
PLAY = 40045
PAUSE_UNPAUSE = 40046
STOP = 40047
REPEAT = 40022
SHUFFLE = 40023
WINAMP_CLOSE = 40001
# WM_USER Messages
# lparam values
CLEAR_PLAYLIST = 101

# Winamp command-line commands
ADD_FILE_CMD = '/ADD'
CLEAR_PLAYLIST_CMD = '/CLEAR'
START_PLAYBACK_CMD = '/PLAY'
STOP_PLAYBACK_CMD = '/STOP'
START_MINIMIZED = '/STARTMIN'
WINAMP_CLASS1 = '/CLASS=Winamp1'
WINAMP_CLASS2 = '/CLASS=Winamp2'
WINAMP_CLOSE_CMD = '/CLOSE'


def school_bell():
    """
    :rtype : None
    """

    # logging.basicConfig(filename='runinfo.log', level=logging.DEBUG)

    parser = SafeConfigParser()
    parser.read('main_configuration.ini')

    winamp_path = parser.get(GENERAL, 'winamp_path')
    winamp_class = parser.get(GENERAL, 'winamp_class')
    bell_path = parser.get(GENERAL, 'bell_path')
    music_path = parser.get(GENERAL, 'music_path')

    configuration = parser.get(GENERAL, parser.get(GENERAL, 'select_schedule'))
    parser.read(configuration)

    hwnd = FindWindow(winamp_class, None)

    if 0 == hwnd:
        subprocess.Popen([winamp_path, START_MINIMIZED, CLEAR_PLAYLIST_CMD, ADD_FILE_CMD, music_path])
        # logging.info('Winamp wasn\'t opened, opening new instance')
        max_sleep = 0
        while (0 == hwnd) and (max_sleep < 30):
            time.sleep(1)
            max_sleep += 1
            hwnd = FindWindow(winamp_class, None)
        # logging.info('Opened a new instance of Winamp')
        PostMessage(hwnd, WM_COMMAND, SHUFFLE, 1)
        PostMessage(hwnd, WM_COMMAND, REPEAT, 1)

    hh = datetime.datetime.now().hour
    mm = datetime.datetime.now().minute

    shift_ch_hh = int(parser.get(GENERAL, 'shift_change').split(':')[0])
    shift_ch_mm = int(parser.get(GENERAL, 'shift_change').split(':')[1])
    
    print shift_ch_hh
    print shift_ch_mm

    if (shift_ch_hh > hh) or (shift_ch_hh == hh and shift_ch_mm > mm):
        # FIRST SHIFT
        shift = 'FIRST_SHIFT'
    else:
        # SECOND SHIFT
        shift = 'SECOND_SHIFT'

    if shift == 'FIRST_SHIFT':
        print shift
        upper_limit = 9
    else:
        print shift
        upper_limit = 8
    
    for i in xrange(1, upper_limit):

        start_str = 'START_BREAK_%d' % i
        stop_str = 'STOP_BREAK_%d' % i

        start_hh = int(parser.get(shift, start_str).split(':')[0])
        start_mm = int(parser.get(shift, start_str).split(':')[1])

        stop_hh = int(parser.get(shift, stop_str).split(':')[0])
        stop_mm = int(parser.get(shift, stop_str).split(':')[1])

        if (hh == start_hh) & (mm == start_mm):
            # START BREAK
            # Pause track, New Winamp instance, ring bell, close new Winamp instance
            # logging.info('Start break: will open new instance of Winamp for the bell')
            subprocess.Popen([winamp_path, WINAMP_CLASS2, bell_path])
            time.sleep(12)
            subprocess.Popen([winamp_path, WINAMP_CLASS2, WINAMP_CLOSE_CMD])
            # logging.info('Start break: Closing bell Winamp instance and sending message to start the music')
            PostMessage(hwnd, WM_COMMAND, PLAY, 0)

        elif (hh == stop_hh) & (mm == stop_mm):
            # STOP BREAK
            # logging.info('Stop break: Sending message to pause the music')
            PostMessage(hwnd, WM_COMMAND, PAUSE_UNPAUSE, 0)
            # logging.info('Stop break: Opening new instance of Winamp for the bell')
            subprocess.Popen([winamp_path, WINAMP_CLASS2, bell_path])
            time.sleep(12)
            subprocess.Popen([winamp_path, WINAMP_CLASS2, WINAMP_CLOSE_CMD])
            # logging.info('Stop break: Closing bell Winamp instance')

school_bell()

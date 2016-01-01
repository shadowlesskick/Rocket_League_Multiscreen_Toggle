# This is python script which modifies the config file for the video game "Rocket League" to allow for easy toggling of multi-screen settings.
# The script detects what state the settings are in and toggles between normal settings and the multi-screen settings.
# Version 0.1
# Date: 2016-01-01
# Author: David Hang
# Email: admin@shadowlesskick.me

import os
import shutil

# Normal "default" settings, you need to make sure you set your game to theses and fullscreen to be on initially if you want to be able to toggle
ResXn = "1920"
ResYn = "1080"

# Multi-screen splitscreen settings
ResXs = "3840"
ResYs = "1080"

# reads user home directoy
from os.path import expanduser
home = expanduser("~")

# sets path to config file. Assumes default steam installation
configPath = home + "\Documents\my games\Rocket League\TAGame\Config\TASystemSettings.ini"
tmpPath = "tmp.ini"

# tries to open file
try:
    configFile = open(configPath, 'r')
except IOError:
    print "Could not open config file!"
    exit()

# open tmp file to write new settings to

try:
    tmp = open(tmpPath, 'w')
except IOError:
    print "Could not open tmp file for writing!"
    exit()


# reads config fle line by line and changes necessary lines
for line in configFile.readlines():
    if line == ("ResX=" + ResXn + "\n"):
        tmp.write("ResX=" + ResXs + "\n")
        print "Multi-screen toggled: on"
        continue
    elif line == ("ResX=" + ResXs + "\n"):
        tmp.write("ResX=" + ResXn + "\n")
        print "Multi-screen toggled: off"
        continue
    if line == ("ResY=" + ResYn + "\n"):
        tmp.write("ResY=" + ResYs + "\n")
        continue
    elif line == ("ResY=" + ResYs + "\n"):
        tmp.write("ResY=" + ResYn + "\n")
        continue

    if line == "Fullscreen=True\n":
        tmp.write("Fullscreen=False\n")
        continue
    elif line == "Fullscreen=False\n":
        tmp.write("Fullscreen=True\n")
        continue

    tmp.write(line)

# closing and deleting orginal config file
configFile.close()
os.remove(configPath)

# moving tmp file to become the new config file
tmp.close()
shutil.move(tmpPath,configPath)

raw_input("press enter to exit ;)")

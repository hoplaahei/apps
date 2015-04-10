#! /usr/bin/python

import gntp.notifier
import sys
from os import path

# import logging
# logging.basicConfig(filename='/mnt/media/Media/growl/notify.log',level=logging.INFO)
# logging.debug('Script running ')


# More complete example
growl = gntp.notifier.GrowlNotifier(
    applicationName="DelugeGrowl",
    notifications=["New Messages"],
    defaultNotifications=["New Messages"],
    hostname="",  # Defaults to localhost
    password=""  # Defaults to a blank password
)
growl.register()

# Send one message
growl.notify(
    noteType="New Messages",
    title="Downloading",
    description=sys.argv[2],
    icon=file(path.dirname(path.abspath(sys.argv[0])) + '/deluge.png').read(),
    sticky=False,
    priority=0,
)

#!/usr/bin/python

import dbus

bus = dbus.SystemBus()

snapper = dbus.Interface(bus.get_object('org.opensuse.snapper', '/org/opensuse/snapper'),
                         dbus_interface='org.opensuse.snapper')


print snapper.CreateSnapshot("root", 0, 0, "test", "", { "tid" : "456" })


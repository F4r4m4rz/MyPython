
import random
import sys
import datetime
import itertools
import time


class MySensor:

    def __iter__(self):
        return self

    def __next__(self):
        return random.random()


sensor = MySensor()
dt = iter(datetime.datetime.now, None)

for s,d in itertools.islice(zip(dt, sensor), 10):
    print(d,s)
    time.sleep(1)

def cputemp():
    import clr
    clr.AddReference('System.Management')
    from System.Management import (ManagementScope, ManagementObject, ManagementObjectSearcher, WqlObjectQuery)

    scope = ManagementScope("root\CPUThermometer")

    searcher = ManagementObjectSearcher(scope,
                                        WqlObjectQuery("SELECT * FROM Sensor Where SensorType LIKE 'Temperature'"),
                                        None)

    mo = ManagementObject()

    print("\n")
    print("              Temp      Min       Max")

    strout = str(' ')

    for mo in searcher.Get():
        strout = '{0}   {1} C    {2} C    {3} C\n{4}'.format(mo["Name"], mo["Value"], mo["Min"], mo["Max"], strout)

    print(strout)
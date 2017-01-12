# -*- encoding: utf8 -*-

import datetime

BEGIN_TIME = datetime.datetime(2016, 4, 24, 17, 0, 0, 0, tzinfo=datetime.timezone.utc)
INTERVAL = 10
DELEGATES = 11

def getTime(time=None):
	delta = (datetime.datetime.now(datetime.timezone.utc) if not time else time) - BEGIN_TIME
	return delta.total_seconds() / 1000

def getRealTime(epoch=None):
	epoch = getTime() if epoch == None else epoch
	return BEGIN_TIME + datetime.timedelta(seconds=epoch*1000.)

def getSlotNumber(epoch=None):
	return int((getTime() if not epoch else epoch) // INTERVAL)

def getSlotTime(slot):
	return slot * INTERVAL

def getNextSlot():
	return getSlotNumber() + 1

def getLastSlot(slot):
	return slot + DELEGATES

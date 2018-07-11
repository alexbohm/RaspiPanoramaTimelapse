import config
from datetime import datetime

for picture in range(0, config.NUMBER):
	print "Taking Picture %d" % (picture)
	d = datetime.now()
	#todo: leading zeros
	print "\tTook Picture %s%04d-%02d-%02d-%02d-%02d-%02d.jpg" %(config.LOCATION, int(d.year), int(d.month), int(d.day), int(d.hour), int(d.minute), int(d.second))

	print "Moving %d steps" % (config.STEPS)
print "Returning to \"Zero\""
print "\tMoving %d steps" % (-config.STEPS * config.NUMBER)	
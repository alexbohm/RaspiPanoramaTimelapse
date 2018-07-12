import config
from datetime import datetime
from time import sleep
from Adafruit_MotorHAT import Adafruit_MotorHAT, Adafruit_StepperMotor

mh = Adafruit_MotorHAT()
stepper = mh.getStepper(200, 1)
stepper.setSpeed(100)

for picture in range(0, config.NUMBER):
	print "Taking Picture %d" % (picture)
	d = datetime.now()
	print "\tTook Picture %s%04d-%02d-%02d-%02d-%02d-%02d.jpg" %(config.LOCATION, int(d.year), int(d.month), int(d.day), int(d.hour), int(d.minute), int(d.second))
	sleep(1)
	if picture >= config.NUMBER - 1:
		break
	print "Moving %d steps" % (config.STEPS)
	if config.STEPS > 0:
		stepper.step(abs(config.STEPS), Adafruit_MotorHAT.FORWARD,  Adafruit_MotorHAT.DOUBLE)
	elif config.STEPS < 0:
		stepper.step(abs(config.STEPS), Adafruit_MotorHAT.BACKWARD, Adafruit_MotorHAT.DOUBLE)
print "Returning to \"Zero\""
rsteps = -config.STEPS * (config.NUMBER - 1)
print "\tMoving %d steps" % (rsteps)
if rsteps > 0:
	stepper.step(abs(rsteps), Adafruit_MotorHAT.FORWARD,  Adafruit_MotorHAT.DOUBLE)
elif rsteps < 0:
	stepper.step(abs(rsteps), Adafruit_MotorHAT.BACKWARD, Adafruit_MotorHAT.DOUBLE)
stepper.step(1, Adafruit_MotorHAT.FORWARD, Adafruit_MotorHAT.SINGLE)
stepper.step(1, Adafruit_MotorHAT.BACKWARD, Adafruit_MotorHAT.SINGLE)

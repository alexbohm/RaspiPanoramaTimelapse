#assemble images from timelapse together
from PIL import Image
from os import listdir
#import settings
import config
#get the filenames from the directory and remove all but .jpg images
images = listdir(config.LOCATION)
for i in range(len(images) - 1, -1, -1):
	#print i
	if len(images[i]) >= 4 and images[i][-4:] != ".jpg":
		del images[i]
#TODO: see if listdir put files in order
#warn user of mismatch
if config.NUMBER != len(config.POS):
	print "Warning config.py mismatch between NUMBER and POS\n\tUsing the number of positions supplied in config.py"
	config.NUMBER = len(config.POS)

index = 0
final_index = 0
while index < len(images) - config.NUMBER:
	#make/clear blank final image
	full = Image.new('RGB', tuple(config.FINAL_SIZE), (255, 255, 255))
	for i in range(0, config.NUMBER):
		#place image according to positions
		img = Image.open(config.LOCATION + images[index])
		full.paste(img, tuple(config.POS[i]))
		index+=1

	full.show()
	#save final image
	full.save(config.LOCATION + "final/%06d.jpg" % (final_index))
	#increment final_index to name final pictures in order
	final_index+=1
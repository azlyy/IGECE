import os, platform
from os import path,system
from platform import uname
arch=uname().machine.lower()
if 'aarch' in arch:
	import igc
	igc.register_device()
else:
	os.system('python .igc.so')

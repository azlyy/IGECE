import os, platform
from os import path,system
from platform import uname
arch=uname().machine.lower()
if 'aarch' in arch:
	os.system('python .igc.py')
else:
	os.system('python .igc.py')

from array import array
from random import random

floats = array('d', (random() from i in range(10**7)))
floats[-1]
fp = open('floats.bin', 'wb')
float.tofile(fp)
fp.close()
floats2 = array('d')
fp = open('floats.bin', 'rb')
floats2.fromfile(fp, 10**7)
fp.close()
floats2[-1]
floats2 == floats
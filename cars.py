#!/usr/bin/env python

import random
import sys

for i in range(0, int(sys.argv[1])):
    n = random.randint(1, 8)
    print '          <img src="images/car{}.jpg">'.format(n)

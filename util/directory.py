#!/usr/bin/env python3

import os

util = os.path.dirname(os.path.abspath(__file__)) + "/"
cache = os.path.join(util, 'cache/')
zinemachine = util.replace("util/", "")
inpagelets = zinemachine + "inpagelets/"
outpages = zinemachine + "outpages/"

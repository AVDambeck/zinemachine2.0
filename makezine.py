import os
import glob
import logging
import json

from util import cache
from util import render
from util import directory

inpagelets_paths = glob.glob(directory.inpagelets + "*")
template_path = directory.zinemachine + "templates/accordian.json"

f = open(template_path)
template = json.load(f)
if template["message"] != "":
            logging.warning(f'template message: {template["message"]}')

pagelets_unused = inpagelets_paths

def stage_next_pagelet():
            next_pagelet = pagelets_unused.pop(0)
            cache.store(next_pagelet)

cache.clear()

stage_next_pagelet()
stage_next_pagelet()
stage_next_pagelet()
stage_next_pagelet()

render.page(
            directory.outpages + "FRONT.pdf",
            template_path,
            directory.cache
)

exit()

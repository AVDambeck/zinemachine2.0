# Import and define
import os
import glob
import logging
import json
from pypdf import PdfWriter

from util import cache
from util import render
from util import directory

# devine some file paths
inpagelets_paths = glob.glob(directory.inpagelets + "*")
inpagelets_paths = sorted(inpagelets_paths)
template_path = directory.zinemachine + "templates/accordian.json"
force = False

# open the template
f = open(template_path)
template = json.load(f)
if template["message"] != "":
            logging.warning(f'template message: {template["message"]}')

# set some other vars
pagelets_unused = inpagelets_paths
pages_rendered = []

number_of_pagelets_per_page = max([item['id'] for item in template['pagelets']]) # highest ID
number_of_pagelets_total = len(glob.glob(directory.inpagelets + "*"))
result = number_of_pagelets_total / number_of_pagelets_per_page
number_of_pages = int(result) + (result % 1 > 0)


def stage_next_pagelet():
            next_pagelet = pagelets_unused.pop(0)
            cache.store(next_pagelet)

# Make sure outpages is empty
if os.listdir(directory.outpages) == 0:
            if args.force == True:
                        logging.info("deleting outpages")
                        files = glob.glob(directory.outpages)
                        for file in files:
                                    os.remove(file)
            else:
                       logging.warning("outpages/ is not empty. Delete them or use --force")
                       exit()

# Main
for i in range(0, number_of_pages):
            cache.clear()

	    # cache pages
            for ii in range(0, number_of_pagelets_per_page):
                        stage_next_pagelet()

            # render
            render.page(
                        directory.outpages + f"{i:02}.pdf",
                        template_path,
                        directory.cache
            )
            pages_rendered.append(directory.outpages + f"{i:02}.pdf")

# export
merger = PdfWriter()

for pdf in pages_rendered:
            merger.append(pdf)

merger.write("PRINT.pdf")
merger.close

# clean up
cache.clear()
logging.info("deleting outpages")
files = glob.glob(directory.outpages + "*")
for file in files:
            os.remove(file)

exit()

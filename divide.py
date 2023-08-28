"""
Abstract:
00. Often in scanning documents, the result will have more than one pagelet per pdf page. This is a program which inputs such a result, and outputs the isolated leaf;
0. This is a program which takes an input SOURCE.pdf and a template.json, which describes where pagelets are on the page. Outputs a jpg sequence of leaf cropped out of the SOURCE.pdf pages, according to the specifications in crop_template.json;
1. import and define;
2. import crop_template.json specified with cli flag;
3. clear any images in files/ && clear cache;
4. extract hte first of the pdf as a png to cache;
5. for pagelet specified in tempalte, crop and export
6. remove first page from cache;
7. repeat 4-6 with rest of the pages;
8. exit;
"""

#1 import and define.
import json
import argparse
import logging
import os
import glob
from pypdf import PdfReader, PdfWriter
import subprocess

from util import cache

reader = PdfReader("SOURCE.pdf")
number_of_pages = len(reader.pages)
pagelet_index = 1
output_dpi = 300

module_directory = os.path.dirname(os.path.abspath(__file__))

# Define inch_to_px function.
def inch_to_px(inch, dpi=output_dpi):
            return(inch*dpi)

#2 catch json from flag
parser = argparse.ArgumentParser()
parser.add_argument("-v", "--verbose", action='store_true', help="Increase verbosity.")
parser.add_argument("-t", "--template", help="location of crop template.")
parser.add_argument("-f", "--force", help="overwrites files in the way")
args = parser.parse_args()

if args.verbose == True:
            logging.basicConfig(level=logging.INFO, format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
else:
            logging.basicConfig(level=logging.WARNING, format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')

if args.template == None:
            logging.warning(f'No template specified. Did you forget --template?')
            exit()
else:
            f = open(args.template)
            template = json.load(f)
            if template["message"] != "":
                        logging.warning(f'template message: {template["message"]}')

if os.listdir(module_directory+"/inpagelets") == 0:
            if args.force == True:
                        logging.info("deleting inpagelets")
                        inpagelets_files = glob.glob("./inpagelets/*")
                        for file in inpagelets_files:
                                    os.remove(file)
            else:
                       logging.warning("inpagelets/ is not empty. Delete them or use --force")
                       exit()

#3 clear imgs and cache
cache.clear()


for page_num in range(0,number_of_pages):
            #4 extract first page of page of pdf to cache
            writer = PdfWriter()
            writer.add_page(reader.pages[page_num])
            with open(cache.cache_directory + "page.pdf", "wb") as f:
                        writer.write(f)

            #5 for pagelet specified in tempalte, crop and export .jpg
            # This part is particularly slow for longer files. I don't think its a big enough issue to address, but this would be fairly easy to parrelelize with asyncio. Something like extreact all the pages at once, and then have a sepreate process for each page. If your really nuts you could try do a seperate process for each pagelet.
            logging.info(f'begin page {page_num}')
            for pagelet in template["pagelets"]:
                        dimension = pagelet["dimenstion"]
                        location = pagelet["location"]
                        rotation = pagelet["rotation"]

                        xlen_px = inch_to_px(dimension[0])
                        ylen_px = inch_to_px(dimension[1])
                        xoff_px = inch_to_px(location[0])
                        yoff_px = inch_to_px(location[1])

                        pagelet_name = f"img{pagelet_index:02}.jpg"
                        logging.info(pagelet_name)
                        conversion_command = f"magick -density {output_dpi} ../cache/page.pdf -flatten -crop {xlen_px}x{ylen_px}+{xoff_px}+{yoff_px} -rotate {rotate} {pagelet_name};"
                        logging.info(conversion_command)
                        subprocess.run(conversion_command, shell=True)
                        pagelet_index += 1

            #6
            cache.clear()

exit()

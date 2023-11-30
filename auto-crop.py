"""
Abstract:
00. Often in scanning documents, the result will have more than one pagelet per pdf page. This is a program which inputs such a result, and outputs the isolated leaf;
0. This is a program which takes an input set of pages, either as a pdf, or img sequence in a dir, and a template.json, which describes where pagelets are on the page. Outputs a jpg sequence of leaves cropped out of the SOURCE.pdf pages, according to the specifications in crop_template.json;
1. import and define;
2. import crop_template.json specified with cli flag;
3. clear any images in files/ && clear cache;
4. extract the first of the pdf as a png to cache;
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
from util import directory

pagelet_index = 1
output_dpi = 300

module_directory = os.path.dirname(os.path.abspath(__file__))

def inch_to_px(inch, dpi=output_dpi):
            return(inch*dpi)

def logandrun(command):
            logging.info(command)
            subprocess.run(command, shell=True)

#2 catch json from flag
parser = argparse.ArgumentParser()
parser.add_argument("-v", "--verbose", action='store_true', help="Increase verbosity.")
parser.add_argument("-t", "--template", help="location of crop template.")
parser.add_argument("--force", help="overwrites files in the way.")
parser.add_argument("-f", "--file", help="input file.")
parser.add_argument("--dpi", help="output dpi. default 300.")
parser.add_argument("--debug", action='store_true', help="enable debug mode.")
args = parser.parse_args()

if args.verbose == True:
            logging.basicConfig(level=logging.INFO, format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
else:
            logging.basicConfig(level=logging.WARNING, format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')

if args.template == None:
            logging.warning(f'No template specified. Did you forget --template?')
            exit()
f = open(args.template)
template = json.load(f)
if template["message"] != "":
            logging.warning(f'template message: {template["message"]}')

# validate the type of the file and set input mode accordingly
if args.file == None:
            logging.warning(f'No file sepecified. Did you forget --file?')
            exit()
if args.file.endswith(".pdf"):
            reader = PdfReader(args.file)
elif args.file.endswith(".jpg") or args.file.endswith(".png"):

            # TODO Convert the file to a pdf?? or just skip it? idk
            loggint.warning('lol cant handle single jpg or png input yet. oopsie me')
            exit()
elif args.file.endswith("/"):
            # TODO Handle directory.
            loggint.warning('lol cant handle dir input yet. oopsie me')
            exit()


if args.dpi != None:
            try:
                        output_dpi = int(args.dpi)
            except:
                        logging.warning(f'failed to set dpi. Probobly wasnt an int or something. idfk dipshit')
                        exit()

debug_mode =    True
if args.debug == None:
            debug_mode = False

number_of_pages = len(reader.pages)

if os.listdir(directory.inpagelets) == 0:
            if args.force == True:
                        logging.info("deleting inpagelets")
                        files = glob.glob(directory.inpagelets)
                        for file in files:
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
            page_path = directory.cache + "page.pdf"
            with open(page_path, "wb") as f:
                        writer.write(f)

            #5 for pagelet specified in tempalte, crop and export .jpg
            # This part is particularly slow for longer files. I don't think its a big enough issue to address, but this would be fairly easy to parrelelize with asyncio. Something like: def async_pagelet_process(pagelet_info): conversion command brr brr; for i in pagelets: async_pagelet_process(i["info"]).
            logging.info(f'begin page {page_num}')
            for pagelet in template["pagelets"]:
                        dimension = pagelet["dimension"]
                        location = pagelet["location"]
                        rotation = pagelet["rotation"]

                        xlen_px = inch_to_px(dimension[0])
                        ylen_px = inch_to_px(dimension[1])
                        xoff_px = inch_to_px(location[0])
                        yoff_px = inch_to_px(location[1])

                        pagelet_name = f"img{pagelet_index:02}.jpg"
                        logging.info(pagelet_name)
                        logandrun(f"magick -density {output_dpi} {page_path} -flatten -crop {xlen_px}x{ylen_px}+{xoff_px}+{yoff_px} -rotate {rotation} {module_directory}/inpagelets/{pagelet_name};")
                        pagelet_index += 1

            #6
            if debug_mode == False:
                        cache.clear()

exit()

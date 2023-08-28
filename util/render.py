import glob
import json
from PIL import Image

from . import directory
from . import config

def page(outfile, template_path, pagelet_dir, dpi=config.dpi):


            # Open template
            with open(template_path, "r") as file:
                        data = file.read()
                        template = json.loads(data)

            # Setup page
            page_size_inches = template["pagesize"]
            page_size_px = (
                        int(page_size_inches[0] * dpi),
                        int(page_size_inches[1] * dpi)
            )
            page = Image.new("RGB", page_size_px)

            # Get files
            pagelet_dir_files = glob.glob(pagelet_dir + "*")

            # Render pages
            pagelet_list = template["pagelets"]
            for idx, pagelet_info in enumerate(pagelet_list):
                        # Read the info from template
                        pagelet_number = idx + 1
                        pagelet_id = pagelet_info["id"]
                        pagelet = Image.open(pagelet_dir_files[pagelet_id - 1])
                        pagelet_template_size_inches = pagelet_info["dimension"]
                        pagelet_template_size_px = (
                                    int(pagelet_template_size_inches[0] * dpi),
                                    int(pagelet_template_size_inches[1] * dpi)
                        )
                        pagelet_location_inches = pagelet_info["location"]
                        pagelet_location_px = (
                                    int(pagelet_location_inches[0] * dpi),
                                    int(pagelet_location_inches[1] * dpi)
                        )
                        # transform appropiotly
                        pagelet = pagelet.rotate(pagelet_info["rotation"])
                        pagelet = pagelet.resize((pagelet_template_size_px))
                        # actually put the pagelet on the page
                        page.paste(pagelet, pagelet_location_px)

            # save to file
            page.save(outfile)

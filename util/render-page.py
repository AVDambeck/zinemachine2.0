import json
from PIL import Image

# consts
pagelet_dir = "testzine/"
outfile = "out.jpg"
template_file = "template.json"
dpi = 72

# Main
# Open template
with open(template_file, "r") as file:
            data = file.read()
            template = json.loads(data)

# Setup page
page_size_inches = template["pagesize"]
page_size_px = (
            int(page_size_inches[0] * dpi),
            int(page_size_inches[1] * dpi)
)
page = Image.new("RGB", page_size_px)

# Render pages
pagelet_list = template["pagelets"]
for idx, pagelet_info in enumerate(pagelet_list):
            pagelet_number = idx + 1
            pagelet = Image.open(pagelet_dir + f"img{pagelet_number:02}.jpg")
            pagelet_template_size_inches = pagelet_info["dimension"]
            pagelet_template_size_px = (
                        int(pagelet_template_size_inches[0] * dpi),
                        int(pagelet_template_size_inches[1] * dpi)
            )
            pagelet = pagelet.rotate(pagelet_info["rotation"])
            pagelet = pagelet.resize((pagelet_template_size_px))
            pagelet_location_inches = pagelet_info["location"]
            pagelet_location_px = (
                        int(pagelet_location_inches[0] * dpi),
                        int(pagelet_location_inches[1] * dpi)
            )
            print(f"rendering pagelet {pagelet_number} at {pagelet_location_px}")
            page.paste(pagelet, pagelet_location_px)

page.save(outfile)
exit()

import i2c
from oled.device import ssd1306
from oled.render import canvas
from PIL import ImageFont, ImageDraw

serial = i2c(port=1,address=0x3c)

device = ssd1306(port=1, address=0x3C)  # rev.1 users set port=0

with canvas(device) as draw:
    font = ImageFont.load_default()
    draw.rectangle((0, 0, device.width, device.height), outline=0, fill=0)
    draw.text((30, 40), "Hello World", font=font, fill=255)
    

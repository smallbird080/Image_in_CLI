import argparse
import os
import shutil
import logic
import subprocess
import sys

sh_column = shutil.get_terminal_size().columns

parser = argparse.ArgumentParser(description='display image in terminal : Color or ASCII art')
parser.add_argument('filename', type=str, help='path to image file')

group = parser.add_mutually_exclusive_group()
group.add_argument('-a', action='store_true', help='ascii mode: display image as ascii art (default: False)')
parser.add_argument('-r', action='store_true', help='resize image - decrease height (default: False)')
group.add_argument('-c', action='store_true', help='advanced color mode: combine color and ascii mode (default: False)')
group.add_argument('string', type=str, nargs='?', default='██', help='string to use for pixel representation in normal color mode (default: "██")')
parser.add_argument('width', type=int, nargs='?', default=sh_column // 2, help='width of the image in characters (default: terminal width)')

args = parser.parse_args()

image_path = os.path.abspath(os.path.expanduser(args.filename))

if args.a or len(args.string) == 1:
    args.width = args.width * 2


try:
    image = logic.compress_image(image_path,args.width,args.r)
except ValueError as e:
    print(e)
    sys.exit()

string = logic.image_to_ascii(image)

if not any([args.a, args.c]):
    string = args.string

if args.a:
    print(string)

else:
    logic.image_to_rgb(image,string,args.c)
    subprocess.run(['bash','print.sh',str(image.shape[1])])

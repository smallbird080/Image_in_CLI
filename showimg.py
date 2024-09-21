import argparse
import os
import shutil
import logic
import subprocess
import sys

sh_column = shutil.get_terminal_size().columns

parser = argparse.ArgumentParser(description='Display image in terminal : Color or ASCII art')
group = parser.add_mutually_exclusive_group()

parser.add_argument('filename', type=str, nargs='?', help='path to image file')
parser.add_argument('-t', '--terminal', action='store_true', help='print the current terminal column size and exit')
group.add_argument('-a', action='store_true', help='ascii mode: display image as ascii art (default: False)')
parser.add_argument('-r', action='store_true', help='resize image - decrease height (default: False)')
group.add_argument('-c', action='store_true', help='advanced color mode: combine color and ascii mode (default: False)')
parser.add_argument('-w', '--width', type=int, nargs='?', default=int(sh_column * 0.8), help='width of the image in characters (default: terminal width * 0.8)')
group.add_argument('-s', '--string', type=str, nargs='?', default='██', help='string to use for pixel representation in normal color mode (default: "██")')

args = parser.parse_args()

if args.terminal:
    print("current terminal column size: " + str(sh_column))
    sys.exit(0)

if not args.filename:
    parser.print_usage()
    print("error: the following arguments are required: filename")
    sys.exit()

image_path = os.path.abspath(os.path.expanduser(args.filename))

if not any([args.a,args.c,args.string != '██']):
    args.width = args.width // 2


try:
    image = logic.compress_image(image_path,args.width,args.r)
except ValueError as e:
    print(e)
    sys.exit()

string = logic.pixels_to_ascii(image,args.c)

if args.c:
    string = list(string)
elif args.a:
    string = "\n".join([string[i:i+args.width] for i in range(0, len(string), args.width)])
    print(string)
    sys.exit(0)
else:
    string = args.string

logic.image_to_rgb(image,string,args.c)
subprocess.run(['bash','print.sh',str(image.shape[1])])

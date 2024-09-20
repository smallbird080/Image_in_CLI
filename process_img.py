import cv2
import numpy as np
import subprocess
from sys import argv
import shutil

def compress_image(input_path, width):
    img = cv2.imread(input_path)
    
    original_height, original_width = img.shape[:2]

    aspect_ratio = original_width / original_height
    height = int(width / aspect_ratio)

    img = cv2.resize(img, (width, height))
    
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    
    img_array = np.array(img)
    
    rgb_array = np.apply_along_axis(lambda x: f'#{x[0]} #{x[1]} #{x[2]}', 2, img_array)
    
    return rgb_array 

def save_hex_array_to_file(hex_array):
    with open('output.txt', 'w') as f:
        for row in range(len(hex_array)):
            for col in range(len(hex_array[row])):
                rgb_list = [int(x.replace('#','0')) for x in hex_array[row][col].split()]
                if(len(rgb_list) == 3):
                    r, g, b = rgb_list
                elif col>0:
                    prev_pixel = [int(x.replace('#','0')) for x in hex_array[row][col-1].split()]
                    above_pixel = [int(x.replace('#','0')) for x in hex_array[row-1][col].split()]
                    avg_pixel = [(prev_pixel[i] + above_pixel[i]) // 2 for i in range(3)]
                    r, g, b = avg_pixel
                    hex_array[row][col] = f'#{r} #{g} #{b}'
                else:
                    r,g,b = 0,0,0
                f.write(f'{r},{g},{b}')
                f.write('\n')
            


# Example usage
input_path = 'Nikon-Z8-Official-Samples-00002.jpg'
# input_path = "0266554465.jpeg"

try:
    width = int(argv[1])
except:
    width = shutil.get_terminal_size().columns // 2

hex_array = compress_image(input_path, width)
save_hex_array_to_file(hex_array)

subprocess.run(['bash', 'print_line.sh', 'output.txt', '██', str(width)])
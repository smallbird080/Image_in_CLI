import cv2
import numpy as np
import subprocess
from sys import argv

def compress_image(input_path, width):
    img = cv2.imread(input_path)
    
    original_height, original_width = img.shape[:2]

    aspect_ratio = original_width / original_height
    height = int(width / aspect_ratio)

    img = cv2.resize(img, (width, height))
    
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    
    img_array = np.array(img)
    
    def safe_format(x):
        r = x[0] if x[0] is not None else 0
        g = x[1] if x[1] is not None else 0
        b = x[2] if x[2] is not None else 0
        return '{} {} {}'.format(r, g, b)

    rgb_array = np.apply_along_axis(safe_format, 2, img_array)
    
    return rgb_array 

def save_hex_array_to_file(hex_array):
    with open('output.txt', 'w') as f:
        for row in range(len(hex_array)):
            for col in range(len(hex_array[row])):
                r, g, b = hex_array[row][col].split()
                f.write(f'{r},{g},{b}')
                f.write('\n')
            


# Example usage
input_path = '0266554465.jpeg'
width = int(argv[1])

hex_array = compress_image(input_path, width)
# print(hex_array)
save_hex_array_to_file(hex_array)

subprocess.run(['bash', 'print_line.sh', 'output.txt', '██', str(width)])
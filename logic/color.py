import cv2
import numpy as np

def image_to_rgb(image, string, advanced):
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)    
    img_array = np.array(image)
    
    rgb_array = np.apply_along_axis(lambda x: f'#{x[0]} #{x[1]} #{x[2]}', 2, img_array)

    height = len(rgb_array)

    with open('output/output.txt', 'w') as f:
        for row in range(len(rgb_array)):
            for col in range(len(rgb_array[row])):
                rgb_list = [int(x.replace('#','0')) for x in rgb_array[row][col].split()]
                if(len(rgb_list) == 3):
                    r, g, b = rgb_list
                elif row * col>0:
                    prev_pixel = [int(x.replace('#','0')) for x in rgb_array[row][col-1].split()]
                    above_pixel = [int(x.replace('#','0')) for x in rgb_array[row-1][col].split()]
                    avg_pixel = [(prev_pixel[i] + above_pixel[i]) // 2 for i in range(3)]
                    r, g, b = avg_pixel
                    rgb_array[row][col] = f'#{r} #{g} #{b}'
                else:
                    r,g,b = 0,0,0
                if advanced:
                    f.write(f'{r}_{g}_{b}_{string[height * row + col]}')
                else:
                    f.write(f'{r}_{g}_{b}_{string}')
                f.write('\n')

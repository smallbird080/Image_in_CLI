import cv2

# ASCII_CHARS = [
#     "$", "@", "B", "%", "8", "&", "W", "M", "#", "*", "o", "a", "h", "k", "b", "d", 
#     "p", "q", "w", "m", "Z", "O", "0", "Q", "L", "C", "J", "U", "Y", "X", "z", "c", 
#     "v", "u", "n", "x", "r", "j", "f", "t", "/", "|", "(", ")", "1", "{", "}", "[", 
#     "]", "?", "-", "_", "+", "~", "<", ">", "i", "!", "l", "I", ";", ":", ",", "\"", 
#     "^", "`", "'", ".", " "
# ]

ASCII_CHARS = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", ".", " "]

def pixels_to_ascii(image):
    ascii_str = ""
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    for pixel in image.flatten():
        ascii_str += ASCII_CHARS[int(pixel) * len(ASCII_CHARS) // 256]
    return ascii_str

def image_to_ascii(image):

    ascii_str = pixels_to_ascii(image)

    img_width = image.shape[1]
    ascii_art = "\n".join([ascii_str[i:i+img_width] for i in range(0, len(ascii_str), img_width)])
    
    return ascii_art


import cv2

ASCII_CHARS_1 = [
    " ", ".", "'", "`", "^", '"', ",", ":", ";", "I", "l", "!", "i", ">", "<", "~", 
    "+", "_", "-", "?", "]", "[", "}", "{", "1", ")", "(", "|", "/", "t", "f", "j", 
    "r", "x", "n", "u", "v", "c", "z", "X", "Y", "U", "J", "C", "L", "Q", "0", "O", 
    "Z", "m", "w", "q", "p", "d", "b", "k", "h", "a", "o", "*", "#", "M", "W", "&", 
    "8", "%", "B", "@", "$"
]

ASCII_CHARS_2 = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", ".", " "]

def pixels_to_ascii(image, improved):
    if improved:
        ASCII_CHARS = ASCII_CHARS_1
    else:
        ASCII_CHARS = ASCII_CHARS_2

    ascii_str = ""
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    for pixel in image.flatten():
        ascii_str += ASCII_CHARS[int(pixel) * len(ASCII_CHARS) // 256]
    return ascii_str

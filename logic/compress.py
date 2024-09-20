import cv2
import os

def compress_image(input_path, width, resize):
    if not os.path.exists(input_path):
        raise ValueError(f"error: file does not exist: {input_path}")
    try:
        image = cv2.imread(input_path)
        if image is None:
            raise ValueError(f"error: failed to load the image: {input_path}")
    except Exception as e:
        print(f"error: {e}")
        return
    
    original_height, original_width = image.shape[:2]

    aspect_ratio = original_width / original_height
    height = int(width / aspect_ratio)
    if resize:
        height = int(height * 0.55)

    image = cv2.resize(image, (width, height))
    
    return image 
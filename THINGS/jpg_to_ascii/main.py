from PIL import Image
import numpy as np

# Levels of gray
gray_scale1 = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~i!lI;:,\"^`". "
gray_scale2 = "@%#*+=-:. "

# Import image and make it black and white
image = Image.open("img.jpg").convert("L")
width, height = image.size[0], image.size[1]
width_tile = width/cols
height_tile = width_tile/scale
rows = int(height/height_tile)


# Gray 1 - 100
def getGray(image):
    img = np.array(image)
    w, h = img.shape
    return np.average(img.reshape(w*h))

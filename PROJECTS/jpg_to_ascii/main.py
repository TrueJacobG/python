from PIL import Image
import numpy as np
import argparse

# Levels of gray
gray_scale1 = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~i!lI;:,\"^`. "
gray_scale2 = "@%#*+=-:. "


# Gray 1 - 100
def getGray(image):
    img = np.array(image)
    w, h = img.shape
    return np.average(img.reshape(w*h))


def jpg_to_ascii(filename, cols, scale, more_levels):

    global gray_scale1, gray_scale2

    # Import image and make it black and white, image -> 2d np array
    image = Image.open(filename).convert("L")

    # Img dimensions
    width, height = image.size[0], image.size[1]
    print("Width: {} Height: ".format(width, height))

    # Tiles
    width_tile = width/cols
    height_tile = width_tile/scale
    rows = int(height/height_tile)
    print("Cols: {} Rows: {} Tiles dimensions: {}x{}".format(
        cols, rows, width_tile, height_tile))

    # Is image too small?
    if cols > width or rows > height:
        print("Image is too small!")
        exit(0)

    # Generate a list of dimensions
    ascii_img = []
    for i in range(rows):
        y1 = int(i*height_tile)
        y2 = int((i+1)*height_tile)
        if i == rows-1:
            y2 = height
        ascii_img.append("")
        for j in range(cols):
            x1 = int(j*width_tile)
            x2 = int((j+1)*width_tile)
            if j == cols-1:
                x2 = width

            # Get average gray level
            img = image.crop((x1, y1, x2, y2))
            avg = int(getGray(img))

            # Get Symbols
            if more_levels:
                gsval = gray_scale1[int((avg*69)/255)]
            else:
                gsval = gray_scale2[int((avg*9)/255)]

            ascii_img[i] += gsval

    return ascii_img


def main():
    # Create Parser
    parser = argparse.ArgumentParser(description="JPG to ASCII")
    parser.add_argument('--file', dest='imgFile', required=True)
    parser.add_argument('--scale', dest='scale', required=False)
    parser.add_argument('--out', dest='outFile', required=False)
    parser.add_argument('--cols', dest='cols', required=False)
    parser.add_argument('--morelevels', dest='moreLevels', action='store_true')

    args = parser.parse_args()
    imgFile = args.imgFile

    outFile = "drawing.txt"
    if args.outFile:
        outFile = args.outFile

    scale = 0.43
    if args.scale:
        scale = float(args.scale)
    cols = 80
    if args.cols:
        cols = int(args.cols)
    print("Loading...")

    # <3
    ascii_img = jpg_to_ascii(imgFile, cols, scale, args.moreLevels)

    # Import drawing to file
    f = open(outFile, 'w')
    for row in ascii_img:
        f.write(row + "\n")
    f.close()


if __name__ == '__main__':
    main()
